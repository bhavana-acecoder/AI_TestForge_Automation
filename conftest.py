import pytest
from playwright.sync_api import sync_playwright
from config.config import Config


@pytest.fixture
def page():
    """
    Creates a new Playwright page for every test.
    """

    playwright = sync_playwright().start()

    if Config.BROWSER == "chromium":
        browser = playwright.chromium.launch(
            headless=Config.HEADLESS
        )

    elif Config.BROWSER == "firefox":
        browser = playwright.firefox.launch(
            headless=Config.HEADLESS
        )

    elif Config.BROWSER == "webkit":
        browser = playwright.webkit.launch(
            headless=Config.HEADLESS
        )

    else:
        raise ValueError(
            f"Unsupported browser: {Config.BROWSER}"
        )

    context = browser.new_context()

    page = context.new_page()

    page.set_default_timeout(Config.TIMEOUT)

    yield page

    context.close()
    browser.close()
    playwright.stop()