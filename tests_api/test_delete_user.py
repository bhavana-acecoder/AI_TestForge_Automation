import pytest

from api.users_api import UsersAPI

pytestmark = pytest.mark.api


def test_delete_user():
    """
    Verify Delete User API.
    """

    users = UsersAPI()

    response = users.delete_user(1)

    print("Status Code:", response.status_code)

    assert response.status_code == 200
