import requests

from utilities.api_logger import APILogger


class BaseAPI:
    """
    Base class for all API requests (Python requests library) with logging.
    """

    TIMEOUT_SECONDS = 30

    def __init__(self, base_url):
        self.base_url = base_url
        self.logger = APILogger.get_logger()

    def send(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"{method} Request to URL: {url}")

        # Log only field names, so passwords never end up in the log file
        for key in ("json", "data", "params"):
            if kwargs.get(key):
                self.logger.info(f"Request {key} fields: {list(kwargs[key].keys())}")

        response = requests.request(method, url, timeout=self.TIMEOUT_SECONDS, **kwargs)

        self.logger.info(f"Response Status: {response.status_code}")
        return response

    def get(self, endpoint, params=None):
        return self.send("GET", endpoint, params=params)

    def post(self, endpoint, payload=None, data=None):
        return self.send("POST", endpoint, json=payload, data=data)

    def put(self, endpoint, payload=None, data=None):
        return self.send("PUT", endpoint, json=payload, data=data)

    def delete(self, endpoint, data=None):
        return self.send("DELETE", endpoint, data=data)
