from pages.home_page import HomePage
from pages.login_page import LoginPage
from utilities.json_reader import JsonReader


def test_valid_login(page):

    data = JsonReader.read_json("testdata/login.json")

    home = HomePage(page)
    login = LoginPage(page)

    home.open()

    home.click_login()

    login.login(
        data["valid_user"]["email"],
        data["valid_user"]["password"]
    )

    assert "Logged in as" in page.locator("a:has-text('Logged in as')").text_content()