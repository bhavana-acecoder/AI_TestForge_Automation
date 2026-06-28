from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object for the Login Page.
    """

    # ---------- Locators ----------
    EMAIL_TEXTBOX = "#Email"
    PASSWORD_TEXTBOX = "#Password"
    LOGIN_BUTTON = "button.login-button"
    LOGIN_ERROR = ".message-error"
    FORGOT_PASSWORD_LINK = ".forgot-password"
    REGISTER_BUTTON = ".register-button"

    # ---------- Constructor ----------
    def __init__(self, page):
        super().__init__(page)

    # ---------- Actions ----------
    def enter_email(self, email):
        self.fill(self.EMAIL_TEXTBOX, email)

    def enter_password(self, password):
        self.fill(self.PASSWORD_TEXTBOX, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_login_error(self):
        return self.get_text(self.LOGIN_ERROR)