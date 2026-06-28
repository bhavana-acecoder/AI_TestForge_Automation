from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_open_login_page(page):
    """
    Verify that the user can navigate
    from the Home Page to the Login Page.
    """

    home = HomePage(page)
    login = LoginPage(page)

    home.open()

    home.click_login()

    assert "Login" in login.get_title()