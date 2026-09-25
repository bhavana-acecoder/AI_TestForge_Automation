from api.base_api import BaseAPI
from config.config import Config


class ProductsAPI(BaseAPI):
    """
    Products and brands endpoints of the AutomationExercise practice API.
    """

    def __init__(self):
        super().__init__(Config.API_BASE_URL)

    def get_products_list(self):
        return self.get("/productsList")

    def get_brands_list(self):
        return self.get("/brandsList")

    def search_product(self, search_term=None):
        # search_term=None sends the request without the required parameter
        data = {"search_product": search_term} if search_term is not None else None
        return self.post("/searchProduct", data=data)
