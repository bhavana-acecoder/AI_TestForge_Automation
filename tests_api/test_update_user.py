import pytest

from api.users_api import UsersAPI
from utilities.json_reader import JsonReader

pytestmark = pytest.mark.api


def test_update_user():
    """
    Verify Update User API.
    """

    # Read JSON
    data = JsonReader.read_json("testdata/api_data.json")

    payload = data["updated_user"]

    # Create API Object
    users = UsersAPI()

    # Update User 1
    response = users.update_user(1, payload)

    print("Status Code:", response.status_code)
    print("Response:", response.json())

    # Validate Status Code
    assert response.status_code == 200

    response_data = response.json()

    # Validate Response
    assert response_data["name"] == payload["name"]
    assert response_data["username"] == payload["username"]
    assert response_data["email"] == payload["email"]
