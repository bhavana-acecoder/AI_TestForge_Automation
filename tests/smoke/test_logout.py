import re

import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.login_page import LoginPage

pytestmark = [pytest.mark.ui, pytest.mark.smoke]


def test_logout(logged_in_page):
    """
    Verify user can logout successfully.
    """

    page = logged_in_page

    home = HomePage(page)
    login = LoginPage(page)

    home.click_logout()

    expect(page).to_have_url(re.compile("/login"))
    expect(home.element(home.LOGGED_IN_USER)).to_be_hidden()
    expect(login.element(login.LOGIN_BUTTON)).to_be_visible()
