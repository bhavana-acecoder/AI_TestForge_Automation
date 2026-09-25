import pytest

from api.users_api import UsersAPI
from utilities.json_reader import JsonReader

pytestmark = pytest.mark.api


def test_create_user():
    """
    Verify Create User API.
    """

    # Read JSON test data
    data = JsonReader.read_json("testdata/api_data.json")

    payload = data["new_user"]

    # Create API object
    users = UsersAPI()

    # Send POST request
    response = users.create_user(payload)

    print("Status Code:", response.status_code)
    print("Response:", response.json())

    # Validate status code
    assert response.status_code == 201

    # Convert response to dictionary
    response_data = response.json()

    # Validate response
    assert response_data["name"] == payload["name"]
    assert response_data["username"] == payload["username"]
    assert response_data["email"] == payload["email"]

    # Verify id exists
    assert "id" in response_data
