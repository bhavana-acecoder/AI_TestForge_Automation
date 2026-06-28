from pages.base_page import BasePage


class HomePage(BasePage):
    """
    Page Object for the nopCommerce Home Page.
    This class contains locators and actions
    that can be performed on the home page.
    """

    # ---------- Locators ----------
    LOGIN_LINK = ".ico-login"
    REGISTER_LINK = ".ico-register"
    SEARCH_BOX = "#small-searchterms"
    SEARCH_BUTTON = "button[type='submit']"
    CART_LINK = ".cart-label"
    WISHLIST_LINK = ".wishlist-label"

    # ---------- Constructor ----------
    def __init__(self, page):
        super().__init__(page)

    # ---------- Actions ----------
    def open(self):
        self.open_url("https://demo.nopcommerce.com/")

    def click_login(self):
        self.click(self.LOGIN_LINK)

    def click_register(self):
        self.click(self.REGISTER_LINK)

    def search_product(self, product_name):
        self.fill(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BUTTON)

    def open_cart(self):
        self.click(self.CART_LINK)

    def open_wishlist(self):
        self.click(self.WISHLIST_LINK)