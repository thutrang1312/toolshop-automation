
"""Sprint 2 - Cart UI testing with Playwright.

Run: pytest tests/ui/test_cart.py -v
"""
import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage


# ---------------------------------------------------------------- B1.4
@pytest.mark.ui
def test_cart_line_total_equals_unit_price_times_quantity(page):
    """Goal: verify cart calculations.
    Precondition: Combination Pliers exists.
    Expected: line total equals unit price times quantity."""
    product = HomePage(page).open().open_product("Combination Pliers")

    unit_price = product.price()

    product.add_to_cart(quantity=2)

    cart = product.go_to_cart()

    expect(cart.product_titles).to_have_count(1)

    assert cart.line_totals() == [
        pytest.approx(unit_price * 2)
    ]

    assert cart.total_value() == pytest.approx(
        sum(cart.line_totals())
    )


# ---------------------------------------------------------------- B1.6
@pytest.mark.ui
def test_cart_continue_shopping_returns_to_product_list(page):
    """Goal: continue shopping after adding a product.
    Precondition: Hammer has been added to the cart.
    Expected: product list becomes visible again."""
    product = HomePage(page).open().open_product("Hammer")
    product.add_to_cart()

    cart = product.go_to_cart()
    expect(cart.product_titles.first).to_have_text("Hammer")

    cart.continue_shopping.click()

    expect(HomePage(page).product_names.first).to_be_visible()
