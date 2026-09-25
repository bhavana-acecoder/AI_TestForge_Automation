import pytest

from api.auth_api import AuthAPI
from utilities.api_assertions import APIAssertions

pytestmark = pytest.mark.api


def test_account_lifecycle(test_user):
    """
    Create an account, read it back, delete it, and confirm it is gone.
    """

    auth = AuthAPI()

    # Create
    response = auth.create_account(test_user)
    APIAssertions.assert_response_code(response, 201)
    APIAssertions.assert_message(response, "User created!")

    # Read back and compare with the data that was sent
    response = auth.get_user_detail_by_email(test_user["email"])
    APIAssertions.assert_response_code(response, 200)

    user = APIAssertions.get_json(response)["user"]
    assert user["email"] == test_user["email"]
    assert user["name"] == test_user["name"]
    assert user["city"] == test_user["city"]

    # Delete
    response = auth.delete_account(test_user["email"], test_user["password"])
    APIAssertions.assert_response_code(response, 200)
    APIAssertions.assert_message(response, "Account deleted!")

    # The deleted user can no longer log in
    response = auth.verify_login(test_user["email"], test_user["password"])
    APIAssertions.assert_response_code(response, 404)


def test_create_account_with_existing_email_returns_400(registered_user):
    """
    Creating a second account with an email that already exists is rejected.
    """

    response = AuthAPI().create_account(registered_user)

    APIAssertions.assert_response_code(response, 400)
    APIAssertions.assert_message(response, "Email already exists!")
