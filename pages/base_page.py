from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)

    def get_title(self):
        return self.page.title()

    def get_text(self, locator: str):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator: str):
        return self.page.locator(locator).is_visible()

    def take_screenshot(self, file_name: str):
        self.page.screenshot(path=f"screenshots/{file_name}")