from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_open_login_page(page):
    """
    Verify that the user can navigate
    from the Home Page to the Login Page.
    """

    # Create Home Page object
    home = HomePage(page)

    # Create Login Page object
    login = LoginPage(page)

    # Open the application
    home.open()

    # Click the Signup / Login menu
    home.click_login()

    # Verify Login page title
    assert "Signup / Login" in login.get_title()