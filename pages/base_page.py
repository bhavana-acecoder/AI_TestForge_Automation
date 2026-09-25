from playwright.sync_api import Locator, Page

from utilities.logger import Logger


class BasePage:
    """
    Base class for all Page Objects.

    Contains reusable Playwright methods that
    every page can inherit.
    """

    def __init__(self, page: Page):
        self.page = page
        self.logger = Logger.get_logger()

    def element(self, locator: str) -> Locator:
        """
        Return a Playwright Locator, so tests can use expect() assertions,
        for example: expect(home.element(home.LOGGED_IN_USER)).to_be_visible()
        """
        return self.page.locator(locator)

    def open_url(self, url: str):
        self.logger.info(f"Opening url: {url}")
        self.page.goto(url)

    def click(self, locator: str):
        self.logger.info(f"Click -> {locator}")
        self.page.locator(locator).click()

    def fill(self, locator: str, text: str):
        self.logger.info(f"Fill -> {locator}")
        self.page.locator(locator).fill(text)

    def get_text(self, locator: str):
        """
        Returns the text of an element after removing
        leading and trailing whitespace.
        """
        return self.page.locator(locator).text_content().strip()

    def get_title(self):
        return self.page.title()

    def is_visible(self, locator: str):
        return self.page.locator(locator).is_visible()

    def wait_for_visible(self, locator: str):
        self.page.locator(locator).wait_for()

    def take_screenshot(self, file_name: str):
        self.page.screenshot(path=f"screenshots/{file_name}")

    def select_dropdown(self, locator: str, value: str):
        self.logger.info(f"Select '{value}' from {locator}")
        self.page.locator(locator).select_option(value)
