import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.login_page import LoginPage

pytestmark = [pytest.mark.ui, pytest.mark.smoke]


def test_valid_login(page, registered_user):
    """
    Verify that a registered user can log in successfully.
    """

    home = HomePage(page)
    login = LoginPage(page)

    home.open()
    home.click_signup_login()

    login.login(registered_user["email"], registered_user["password"])

    # Web-first assertion: waits until the text appears (or times out)
    expect(home.element(home.LOGGED_IN_USER)).to_have_text(
        f"Logged in as {registered_user['name']}"
    )
