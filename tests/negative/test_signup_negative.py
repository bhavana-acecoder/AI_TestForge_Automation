import re

import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.login_page import LoginPage

pytestmark = [pytest.mark.ui, pytest.mark.negative]


def test_signup_with_existing_email_shows_error(page, registered_user):
    """
    Signing up again with an email that is already registered
    should show an error and stay on the signup page.
    """

    home = HomePage(page)
    login = LoginPage(page)

    home.open()
    home.click_signup_login()

    login.signup(registered_user["name"], registered_user["email"])

    expect(login.element(login.SIGNUP_ERROR)).to_have_text("Email Address already exist!")
    expect(page).to_have_url(re.compile("/signup"))
