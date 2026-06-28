from pages.base_page import BasePage


class AccountRegistrationPage(BasePage):

    # ---------- Title ----------
    TITLE_MR = "#id_gender1"
    TITLE_MRS = "#id_gender2"

    # ---------- Account Information ----------
    PASSWORD = "#password"

    DAY = "#days"
    MONTH = "#months"
    YEAR = "#years"

    def __init__(self, page):
        super().__init__(page)

    def select_title(self):
        self.click(self.TITLE_MR)

    def enter_password(self, password):
        self.fill(self.PASSWORD, password)

    def select_day(self, day):
        self.select_dropdown(self.DAY, day)

    def select_month(self, month):
        self.select_dropdown(self.MONTH, month)

    def select_year(self, year):
        self.select_dropdown(self.YEAR, year)