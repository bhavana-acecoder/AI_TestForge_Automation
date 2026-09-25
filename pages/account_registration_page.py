from pages.base_page import BasePage


class AccountRegistrationPage(BasePage):
    """
    Page Object for Automation Exercise
    Account Registration Page.
    """

    # ==========================================
    # Title
    # ==========================================

    TITLE_MR = "#id_gender1"
    TITLE_MRS = "#id_gender2"

    # ==========================================
    # Account Information
    # ==========================================

    PASSWORD = "#password"

    DAY = "#days"
    MONTH = "#months"
    YEAR = "#years"

    # ==========================================
    # Address Information
    # ==========================================

    FIRST_NAME = "#first_name"
    LAST_NAME = "#last_name"

    COMPANY = "#company"

    ADDRESS1 = "#address1"
    ADDRESS2 = "#address2"

    COUNTRY = "#country"

    STATE = "#state"
    CITY = "#city"

    ZIPCODE = "#zipcode"

    MOBILE_NUMBER = "#mobile_number"

    # ==========================================
    # Buttons
    # ==========================================

    CREATE_ACCOUNT_BUTTON = "button[data-qa='create-account']"

    CONTINUE_BUTTON = "a[data-qa='continue-button']"

    # ==========================================
    # Validation
    # ==========================================

    ACCOUNT_CREATED_MESSAGE = "h2[data-qa='account-created']"

    # ==========================================
    # Constructor
    # ==========================================

    def __init__(self, page):
        super().__init__(page)

    # ==========================================
    # Title
    # ==========================================

    def select_mr_title(self):
        self.click(self.TITLE_MR)

    def select_mrs_title(self):
        self.click(self.TITLE_MRS)

    # ==========================================
    # Account Information
    # ==========================================

    def enter_password(self, password):
        self.fill(self.PASSWORD, password)

    def select_day(self, day):
        self.select_dropdown(self.DAY, day)

    def select_month(self, month):
        self.select_dropdown(self.MONTH, month)

    def select_year(self, year):
        self.select_dropdown(self.YEAR, year)

    # ==========================================
    # Address Information
    # ==========================================

    def enter_first_name(self, first_name):
        self.fill(self.FIRST_NAME, first_name)

    def enter_last_name(self, last_name):
        self.fill(self.LAST_NAME, last_name)

    def enter_company(self, company):
        self.fill(self.COMPANY, company)

    def enter_address1(self, address1):
        self.fill(self.ADDRESS1, address1)

    def enter_address2(self, address2):
        self.fill(self.ADDRESS2, address2)

    def select_country(self, country):
        self.select_dropdown(self.COUNTRY, country)

    def enter_state(self, state):
        self.fill(self.STATE, state)

    def enter_city(self, city):
        self.fill(self.CITY, city)

    def enter_zipcode(self, zipcode):
        self.fill(self.ZIPCODE, zipcode)

    def enter_mobile_number(self, mobile):
        self.fill(self.MOBILE_NUMBER, mobile)

    # ==========================================
    # Buttons
    # ==========================================

    def click_create_account(self):
        self.click(self.CREATE_ACCOUNT_BUTTON)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    # ==========================================
    # Complete Registration
    # ==========================================

    def fill_registration_form(self, user):
        """
        Fill the complete registration form
        using data from register.json.
        """

        self.select_mr_title()

        self.enter_password(user["password"])

        self.select_day(user["day"])
        self.select_month(user["month"])
        self.select_year(user["year"])

        self.enter_first_name(user["first_name"])
        self.enter_last_name(user["last_name"])

        self.enter_company(user["company"])

        self.enter_address1(user["address1"])
        self.enter_address2(user["address2"])

        self.select_country(user["country"])

        self.enter_state(user["state"])
        self.enter_city(user["city"])

        self.enter_zipcode(user["zipcode"])

        self.enter_mobile_number(user["mobile"])

    # ==========================================
    # Validation
    # ==========================================

    def get_account_created_message(self):
        return self.get_text(self.ACCOUNT_CREATED_MESSAGE)
    
    def is_account_created(self):
        return "Account Created" in self.get_account_created_message()