import pytest

from api.auth_api import AuthAPI
from utilities.api_assertions import APIAssertions

pytestmark = pytest.mark.api


def test_verify_login_with_valid_credentials(registered_user):
    """
    A registered user with the correct password is found.
    """

    response = AuthAPI().verify_login(registered_user["email"], registered_user["password"])

    APIAssertions.assert_response_code(response, 200)
    APIAssertions.assert_message(response, "User exists!")


@pytest.mark.parametrize("case", ["wrong_password", "unregistered_email"])
def test_verify_login_with_invalid_credentials_returns_404(registered_user, case):
    """
    Wrong password, or an email that is not registered, is rejected.
    """

    if case == "wrong_password":
        email, password = registered_user["email"], "Wrong@12345"
    else:
        email, password = "not.registered.qa.user@example.com", registered_user["password"]

    response = AuthAPI().verify_login(email, password)

    APIAssertions.assert_response_code(response, 404)
    APIAssertions.assert_message(response, "User not found!")


@pytest.mark.parametrize("missing_field", ["email", "password"])
def test_verify_login_with_missing_field_returns_400(missing_field):
    """
    A required field is missing from the request.
    """

    if missing_field == "email":
        response = AuthAPI().verify_login(password="Demo@12345")
    else:
        response = AuthAPI().verify_login(email="qa.user@example.com")

    APIAssertions.assert_response_code(response, 400)
    APIAssertions.assert_message(
        response, "Bad request, email or password parameter is missing in POST request."
    )
