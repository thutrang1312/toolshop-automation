
"""Sprint 2 - Search UI tests using Playwright.

Run: pytest tests/ui/test_search.py -v
"""
import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage


# ---------------------------------------------------------------- B1.2
@pytest.mark.ui
def test_search_unknown_keyword_shows_no_results(page):
    """Goal: search for a nonexistent product.
    Precondition: homepage is available.
    Expected: no results message and zero products."""
    home = HomePage(page).open()
    home.search("zzz-no-such-tool")

    expect(home.no_results).to_have_text("There are no products found.")
    expect(home.product_names).to_have_count(0)


# ---------------------------------------------------------------- B1.7
@pytest.mark.ui
def test_products_sort_price_ascending(page):
    """Goal: sort products by ascending price.
    Precondition: products are available.
    Expected: prices are sorted from low to high."""
    home = HomePage(page).open()
    home.sort_by("price,asc")

    expect(home.sorting_completed).to_be_visible()

    prices = home.prices()
    assert prices, "no product prices found"
    assert prices == sorted(prices)
