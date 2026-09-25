import re

import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utilities.json_reader import JsonReader

pytestmark = [pytest.mark.ui, pytest.mark.negative]

TEST_DATA = JsonReader.read_json("testdata/negative_login.json")

INVALID_CREDENTIALS = TEST_DATA["invalid_credentials"]
INVALID_INPUTS = TEST_DATA["invalid_inputs"]


@pytest.mark.parametrize(
    "case", INVALID_CREDENTIALS, ids=[case["id"] for case in INVALID_CREDENTIALS]
)
def test_login_with_invalid_credentials_shows_error(page, registered_user, case):
    """
    Wrong password for a registered user, or an email that is not registered:
    the site should show an error and the user should stay logged out.
    """

    email = registered_user["email"] if case["use_registered_email"] else case["email"]

    home = HomePage(page)
    login = LoginPage(page)

    home.open()
    home.click_signup_login()

    login.login(email, case["password"])

    expect(login.element(login.LOGIN_ERROR)).to_have_text(
        "Your email or password is incorrect!"
    )
    expect(home.element(home.LOGGED_IN_USER)).to_be_hidden()


@pytest.mark.parametrize(
    "case", INVALID_INPUTS, ids=[case["id"] for case in INVALID_INPUTS]
)
def test_login_form_blocks_invalid_input(page, case):
    """
    Empty or badly formatted input: the browser's form validation
    (required / type=email) should block the login request.
    """

    home = HomePage(page)
    login = LoginPage(page)

    home.open()
    home.click_signup_login()

    login.login(case["email"], case["password"])

    field = login.LOGIN_EMAIL if case["invalid_field"] == "email" else login.LOGIN_PASSWORD

    assert login.is_field_valid(field) is False, (
        f"Expected the {case['invalid_field']} field to be invalid"
    )

    # The form was not submitted: still on the login page and not logged in
    expect(page).to_have_url(re.compile("/login"))
    expect(home.element(home.LOGGED_IN_USER)).to_be_hidden()
