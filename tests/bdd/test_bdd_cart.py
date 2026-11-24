
import pytest
from playwright.sync_api import expect
from pytest_bdd import given, when, then, parsers, scenarios

from pages.home_page import HomePage


# Danh dau cac test thuoc nhom BDD va UI
pytestmark = [pytest.mark.bdd, pytest.mark.ui]

# Doc kich ban Gherkin
scenarios("cart.feature")


# Step 1: Mo trang chu
@given("I am on the home page", target_fixture="home")
def home(page):
    home = HomePage(page).open()
    expect(home.product_names.first).to_be_visible()
    return home


# Step 2: Mo san pham
@when(
    parsers.parse('I open the product "{product}"'),
    target_fixture="product_page"
)
def open_product(home, product):
    return home.open_product(product)


# Step 3: Them san pham vao gio hang
@when(
    parsers.parse("I add it to the cart with quantity {quantity:d}"),
    target_fixture="unit_price"
)
def add_to_cart(product_page, quantity):
    unit = product_page.price()
    product_page.add_to_cart(quantity=quantity)
    expect(product_page.cart_quantity).to_have_text(str(quantity))
    return unit


# Step 4: Mo gio hang
@when("I open the cart", target_fixture="cart")
def open_cart(product_page):
    return product_page.go_to_cart()


# Step 5: Kiem tra san pham trong gio
@then(parsers.parse('the cart contains "{product}"'))
def cart_contains(cart, product):
    expect(cart.product_titles).to_have_count(1)
    expect(cart.product_titles.first).to_have_text(product)


# Step 6: Kiem tra gia dong san pham
@then(
    parsers.parse(
        "the line price equals the unit price times {quantity:d}"
    )
)
def check_line_price(cart, unit_price, quantity):
    actual = cart.line_totals()[0]
    expected = unit_price * quantity
    assert actual == pytest.approx(expected)


# Step 7: Kiem tra tong tien gio hang
@then("the cart total equals the sum of the line prices")
def check_cart_total(cart):
    actual = cart.total_value()
    expected = sum(cart.line_totals())
    assert actual == pytest.approx(expected)
