import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_valid_user_can_login(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    login_page.assert_logged_in()


@pytest.mark.regression
def test_locked_out_user_sees_error(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    # Locked-out accounts should stay on login page and show a clear block message
    login_page.login("locked_out_user", "secret_sauce")
    login_page.assert_error_contains("locked out")
