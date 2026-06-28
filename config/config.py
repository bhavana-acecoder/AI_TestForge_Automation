# config/config.py

from config.environments import Environments


class Config:
    """
    Framework configuration.
    """

    ENVIRONMENT = "qa"

    BASE_URL = Environments.URLS[ENVIRONMENT]

    BROWSER = "chromium"

    HEADLESS = False

    TIMEOUT = 30000