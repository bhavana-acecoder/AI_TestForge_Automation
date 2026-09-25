from api.base_api import BaseAPI
from config.config import Config


class UsersAPI(BaseAPI):
    """
    API methods for Users (JSONPlaceholder practice API).
    """

    def __init__(self):
        super().__init__(Config.JSONPLACEHOLDER_URL)

    def get_users(self):
        return self.get("/users")

    def get_single_user(self, user_id):
        return self.get(f"/users/{user_id}")

    def create_user(self, payload):
        return self.post("/users", payload)

    def update_user(self, user_id, payload):
        return self.put(f"/users/{user_id}", payload)

    def delete_user(self, user_id):
        return self.delete(f"/users/{user_id}")
