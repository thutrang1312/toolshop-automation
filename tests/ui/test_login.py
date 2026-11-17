
"""Sprint 2 - Login UI testing with Playwright.

Run: pytest tests/ui/test_login.py -v
"""
import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage


# ---------------------------------------------------------------- B1.5
@pytest.mark.ui
def test_login_empty_form_shows_required_field_errors(page):
    """Goal: validate required login fields.
    Precondition: email and password are empty.
    Expected: both required-field errors appear."""
    login = LoginPage(page).open()

    login.submit_button.click()

    expect(login.email_error).to_contain_text("Email is required")
    expect(login.password_error).to_contain_text("Password is required")
