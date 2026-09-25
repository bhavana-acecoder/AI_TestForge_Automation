from api.base_api import BaseAPI
from config.config import Config


class PostsAPI(BaseAPI):
    """
    API methods for Posts (JSONPlaceholder practice API).
    """

    def __init__(self):
        super().__init__(Config.JSONPLACEHOLDER_URL)

    def get_posts(self):
        return self.get("/posts")

    def get_single_post(self, post_id):
        return self.get(f"/posts/{post_id}")

    def create_post(self, payload):
        return self.post("/posts", payload)

    def update_post(self, post_id, payload):
        return self.put(f"/posts/{post_id}", payload)

    def delete_post(self, post_id):
        return self.delete(f"/posts/{post_id}")
