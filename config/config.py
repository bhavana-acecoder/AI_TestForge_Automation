# config/config.py

import os

from config.environments import Environments


class Config:
    """
    Framework configuration.

    BROWSER and HEADLESS can be overridden with environment variables,
    for example HEADLESS=true in CI.
    """

    ENVIRONMENT = os.getenv("TEST_ENV", "qa")

    BASE_URL = Environments.URLS[ENVIRONMENT]

    # Public practice APIs
    API_BASE_URL = "https://automationexercise.com/api"
    JSONPLACEHOLDER_URL = "https://jsonplaceholder.typicode.com"

    BROWSER = os.getenv("BROWSER", "chromium")

    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

    TIMEOUT = 30000
