from pages.base_page import BasePage
from config.config import Config


class HomePage(BasePage):
    """
    Page Object for the Home Page of Automation Exercise.
    """

    # -----------------------
    # Locators
    # -----------------------

    SIGNUP_LOGIN_LINK = "a[href='/login']"
    PRODUCTS_LINK = "a[href='/products']"
    CART_LINK = "a[href='/view_cart']"
    CONTACT_US_LINK = "a[href='/contact_us']"
    TEST_CASES_LINK = "a[href='/test_cases']"

    # -----------------------
    # Constructor
    # -----------------------

    def __init__(self, page):
        super().__init__(page)

    # -----------------------
    # Actions
    # -----------------------

    def open(self):
        self.open_url(Config.BASE_URL)

    def click_signup_login(self):
        self.click(self.SIGNUP_LOGIN_LINK)

    def click_products(self):
        self.click(self.PRODUCTS_LINK)

    def click_cart(self):
        self.click(self.CART_LINK)

    def click_contact_us(self):
        self.click(self.CONTACT_US_LINK)

    def click_test_cases(self):
        self.click(self.TEST_CASES_LINK)