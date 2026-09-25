import pytest
from playwright.sync_api import expect

from api.auth_api import AuthAPI
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utilities.json_reader import JsonReader
from utilities.random_data import RandomData


@pytest.fixture
def test_user():
    """
    Demo user data from testdata/register.json with a new unique email.

    After the test, the account is deleted through the API (if it exists),
    so every test starts clean and no test depends on another test.
    """

    user = JsonReader.read_json("testdata/register.json")["user"]
    user["email"] = RandomData.generate_email()

    yield user

    # Cleanup: returns "not found" if the test already deleted the account
    AuthAPI().delete_account(user["email"], user["password"])


@pytest.fixture
def registered_user(test_user):
    """
    Creates the test user through the API before the test.
    Using the API for setup is faster and more stable than using the UI.
    """

    response = AuthAPI().create_account(test_user)

    assert "User created!" in response.text, (
        f"Test setup failed, account not created: {response.text}"
    )

    return test_user


@pytest.fixture
def logged_in_page(page, registered_user):
    """
    Logs in with the registered user through the UI before the test.
    """

    home = HomePage(page)
    login = LoginPage(page)

    home.open()
    home.click_signup_login()

    login.login(registered_user["email"], registered_user["password"])

    expect(home.element(home.LOGGED_IN_USER)).to_be_visible()

    return page
