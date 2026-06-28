from config.environments import BASE_URL


class Config:
    BASE_URL = BASE_URL

    BROWSER = "chromium"

    HEADLESS = False

    TIMEOUT = 30000