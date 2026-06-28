from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_registration_page import AccountRegistrationPage

from utilities.json_reader import JsonReader
from utilities.random_data import RandomData


def test_register_new_user(page):

    data = JsonReader.read_json("testdata/register.json")

    email = RandomData.generate_email()

    home = HomePage(page)
    login = LoginPage(page)
    registration = AccountRegistrationPage(page)

    home.open()

    home.click_signup_login()

    login.signup(
        data["user"]["name"],
        email
    )

    registration.fill_registration_form(
        password=data["user"]["password"],

        day=data["user"]["day"],
        month=data["user"]["month"],
        year=data["user"]["year"],

        first_name=data["user"]["first_name"],
        last_name=data["user"]["last_name"],

        company=data["user"]["company"],

        address1=data["user"]["address1"],
        address2=data["user"]["address2"],

        country=data["user"]["country"],

        state=data["user"]["state"],
        city=data["user"]["city"],

        zipcode=data["user"]["zipcode"],

        mobile=data["user"]["mobile"]
    )

    registration.click_create_account()

    assert registration.get_account_created_message() == "ACCOUNT CREATED!"