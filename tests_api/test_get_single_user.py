import pytest

from api.users_api import UsersAPI
from utilities.api_assertions import APIAssertions

pytestmark = pytest.mark.api


def test_get_single_user():

    users = UsersAPI()

    response = users.get_single_user(1)

    APIAssertions.assert_status_code(response, 200)

    APIAssertions.assert_response_value(
        response,
        "id",
        1
    )

    APIAssertions.assert_response_value(
        response,
        "name",
        "Leanne Graham"
    )

    APIAssertions.assert_response_key(
        response,
        "email"
    )
