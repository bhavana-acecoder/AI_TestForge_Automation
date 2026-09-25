import pytest

from api.users_api import UsersAPI
from utilities.api_assertions import APIAssertions

pytestmark = pytest.mark.api


def test_get_users():
    """
    Verify GET Users API.
    """

    users = UsersAPI()

    response = users.get_users()

    print(response.status_code)
    print(response.json())

    APIAssertions.assert_status_code(response, 200)

    data = response.json()

    assert len(data) > 0
