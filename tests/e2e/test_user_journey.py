import re

import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_registration_page import AccountRegistrationPage
from pages.delete_account_page import DeleteAccountPage

pytestmark = [pytest.mark.ui, pytest.mark.e2e]


def test_complete_user_journey(page, test_user):
    """
    Complete End-to-End User Journey

    Register -> Logout -> Login Again -> Delete Account
    """

    home = HomePage(page)
    login = LoginPage(page)
    registration = AccountRegistrationPage(page)
    delete = DeleteAccountPage(page)

    # Register
    home.open()
    home.click_signup_login()

    login.signup(test_user["name"], test_user["email"])

    registration.fill_registration_form(test_user)
    registration.click_create_account()

    expect(registration.element(registration.ACCOUNT_CREATED_MESSAGE)).to_have_text(
        re.compile("account created", re.IGNORECASE)
    )

    registration.click_continue()

    expect(home.element(home.LOGGED_IN_USER)).to_be_visible()

    # Logout
    home.click_logout()

    expect(page).to_have_url(re.compile("/login"))

    # Login Again
    login.login(test_user["email"], test_user["password"])

    expect(home.element(home.LOGGED_IN_USER)).to_have_text(
        f"Logged in as {test_user['name']}"
    )

    # Delete Account
    delete.click_delete_account()

    expect(delete.element(delete.ACCOUNT_DELETED_MESSAGE)).to_have_text(
        re.compile("account deleted", re.IGNORECASE)
    )

    delete.click_continue()
