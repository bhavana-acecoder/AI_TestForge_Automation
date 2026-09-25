from pages.base_page import BasePage


class DeleteAccountPage(BasePage):
    """
    Page Object for Delete Account page.
    """

    # -----------------------------
    # Locators
    # -----------------------------

    DELETE_ACCOUNT_LINK = "a[href='/delete_account']"

    ACCOUNT_DELETED_MESSAGE = "h2[data-qa='account-deleted']"

    CONTINUE_BUTTON = "a[data-qa='continue-button']"

    # -----------------------------
    # Constructor
    # -----------------------------

    def __init__(self, page):
        super().__init__(page)

    # -----------------------------
    # Actions
    # -----------------------------

    def click_delete_account(self):
        self.click(self.DELETE_ACCOUNT_LINK)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    # -----------------------------
    # Validation
    # -----------------------------

    def get_account_deleted_message(self):
        return self.get_text(self.ACCOUNT_DELETED_MESSAGE)

    def is_account_deleted(self):
        return "Account Deleted" in self.get_account_deleted_message()
