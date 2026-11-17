
"""Sprint 2 - Product detail UI testing with Playwright.

Run: pytest tests/ui/test_product_detail.py -v
"""
import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage


# ---------------------------------------------------------------- Product detail
@pytest.mark.ui
def test_product_detail_shows_correct_name_and_price(page):
    """Goal: verify product details.
    Precondition: Claw Hammer exists.
    Expected: correct product name and price > 0."""
    home = HomePage(page).open()
    product = home.open_product("Claw Hammer")

    expect(product.name).to_have_text("Claw Hammer")
    expect(product.unit_price).to_be_visible()

    assert product.price() > 0