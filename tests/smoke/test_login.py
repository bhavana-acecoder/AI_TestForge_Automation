from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object for Automation Exercise Login/Signup Page.
    """

    # ----------------------------
    # Login Locators
    # ----------------------------

    LOGIN_EMAIL = "input[data-qa='login-email']"
    LOGIN_PASSWORD = "input[data-qa='login-password']"
    LOGIN_BUTTON = "button[data-qa='login-button']"

    # ----------------------------
    # Signup Locators
    # ----------------------------

    SIGNUP_NAME = "input[data-qa='signup-name']"
    SIGNUP_EMAIL = "input[data-qa='signup-email']"
    SIGNUP_BUTTON = "button[data-qa='signup-button']"

    # ----------------------------
    # Error Messages
    # ----------------------------

    LOGIN_ERROR = "form[action='/login'] p"

    def __init__(self, page):
        super().__init__(page)

    # ----------------------------
    # Login Methods
    # ----------------------------

    def enter_login_email(self, email):
        self.fill(self.LOGIN_EMAIL, email)

    def enter_login_password(self, password):
        self.fill(self.LOGIN_PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_login_email(email)
        self.enter_login_password(password)
        self.click_login()

    # ----------------------------
    # Signup Methods
    # ----------------------------

    def enter_signup_name(self, name):
        self.fill(self.SIGNUP_NAME, name)

    def enter_signup_email(self, email):
        self.fill(self.SIGNUP_EMAIL, email)

    def click_signup(self):
        self.click(self.SIGNUP_BUTTON)

    def signup(self, name, email):
        self.enter_signup_name(name)
        self.enter_signup_email(email)
        self.click_signup()

    # ----------------------------
    # Validation
    # ----------------------------

    def get_login_error(self):
        return self.get_text(self.LOGIN_ERROR)