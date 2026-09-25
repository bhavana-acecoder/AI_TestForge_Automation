import os
import re
from datetime import datetime

import pytest
from playwright.sync_api import sync_playwright

from config.config import Config

pytest_plugins = [
    "fixtures.user_fixtures"
]

# Third-party ad/tracking requests on the demo site. Blocking them keeps
# pop-up ads from covering page elements and making UI tests flaky.
AD_DOMAINS = re.compile(
    r"googlesyndication|doubleclick|googleadservices|adservice\.google|"
    r"fundingchoicesmessages|googletagmanager|google-analytics"
)


@pytest.fixture
def page():
    """
    Creates a new browser page for every test.
    """

    playwright = sync_playwright().start()

    # Launch Browser
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

    context.route(AD_DOMAINS, lambda route: route.abort())

    page = context.new_page()

    page.set_default_timeout(Config.TIMEOUT)

    yield page

    # Close browser after every test
    context.close()
    browser.close()
    playwright.stop()


def pytest_html_report_title(report):
    report.title = "AI TestForge Automation Report"


def pytest_configure(config):

    if hasattr(config, "_metadata"):
        config._metadata["Project"] = "AI TestForge Automation"
        config._metadata["Tester"] = "Bhavana Jain"
        config._metadata["Framework"] = "Playwright + Pytest"
        config._metadata["Language"] = "Python"
        config._metadata["Browser"] = Config.BROWSER


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Automatically captures screenshot when a test fails.
    """

    outcome = yield

    report = outcome.get_result()

    # Only take screenshot if test failed
    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            filename = (
                f"screenshots/{item.name}_{timestamp}.png"
            )

            page.screenshot(path=filename)

            print(f"\nScreenshot saved: {filename}")
