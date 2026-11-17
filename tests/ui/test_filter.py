
"""Sprint 2 - Product filter UI tests.

Run: pytest tests/ui/test_filter.py -v
"""
import re

import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage


# ---------------------------------------------------------------- Filter Hammer
@pytest.mark.ui
def test_products_filter_hammer_returns_matching_names(page):
    """Goal: filter products by Hammer category.
    Precondition: Hammer products exist.
    Expected: all displayed names contain hammer."""
    home = HomePage(page).open()
    home.filter_hammer()

    expect(home.product_names.first).to_contain_text(
        re.compile("hammer", re.IGNORECASE)
    )

    names = home.product_names.all_inner_texts()
    assert names, "no Hammer products found"
    assert all("hammer" in name.lower() for name in names), names
