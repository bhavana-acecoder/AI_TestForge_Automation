import re

import pytest
from playwright.sync_api import expect

from pages.delete_account_page import DeleteAccountPage
from pages.home_page import HomePage

pytestmark = [pytest.mark.ui, pytest.mark.smoke]


def test_delete_account(logged_in_page):
    """
    Verify a logged-in user can delete their account.
    """

    page = logged_in_page

    home = HomePage(page)
    delete = DeleteAccountPage(page)

    delete.click_delete_account()

    expect(delete.element(delete.ACCOUNT_DELETED_MESSAGE)).to_have_text(
        re.compile("account deleted", re.IGNORECASE)
    )

    delete.click_continue()

    expect(home.element(home.LOGGED_IN_USER)).to_be_hidden()
