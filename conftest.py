import pytest
from playwright.sync_api import sync_playwright
from config.config import Config

@pytest.fixture
def page():
    """
    Creates a new Playwright page for every test.
    """

    # Start Playwright
    playwright = sync_playwright().start()

    # Launch browser
    if Config.BROWSER == "chromium":
        browser = playwright.chromium.launch(headless=Config.HEADLESS)

    elif Config.BROWSER == "firefox":
        browser = playwright.firefox.launch(headless=Config.HEADLESS)

    elif Config.BROWSER == "webkit":
        browser = playwright.webkit.launch(headless=Config.HEADLESS)

    else:
        raise ValueError(f"Unsupported browser: {Config.BROWSER}")
    
    # Create isolated browser context
    context = browser.new_context()

    # Open a new tab
    page = context.new_page()

    # Provide page to the test
    yield page

    # Cleanup after test
    context.close()
    browser.close()
    playwright.stop()