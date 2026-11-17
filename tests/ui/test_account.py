
"""Sprint 2 - Account UI testing with Playwright.

Fixtures: logged_in_page (see conftest.py)

Run: pytest tests/ui/test_account.py -v
"""
import re

import pytest
from playwright.sync_api import expect

from pages.account_page import AccountPage


# ---------------------------------------------------------------- Account
@pytest.mark.ui
@pytest.mark.smoke
def test_account_logged_in_user_sees_account_page(logged_in_page):
    """Goal: verify authenticated account access.
    Precondition: logged_in_page uses saved storage_state.
    Expected: account page and navigation are visible."""
    account = AccountPage(logged_in_page).open()

    expect(logged_in_page).to_have_url(re.compile(r"/account$"))
    expect(account.title).to_be_visible()
    expect(account.nav_profile).to_be_visible()
    expect(account.nav_invoices).to_be_visible()
