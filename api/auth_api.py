from api.base_api import BaseAPI
from config.config import Config


class AuthAPI(BaseAPI):
    """
    Account and login endpoints of the AutomationExercise practice API.
    This API expects form data (not JSON) in the request body.
    """

    def __init__(self):
        super().__init__(Config.API_BASE_URL)

    def verify_login(self, email=None, password=None):
        # Only send the fields that are given, so missing-field cases can be tested
        data = {}
        if email is not None:
            data["email"] = email
        if password is not None:
            data["password"] = password
        return self.post("/verifyLogin", data=data)

    def create_account(self, user):
        """
        Create an account from a user dictionary built from testdata/register.json.
        """
        data = {
            "name": user["name"],
            "email": user["email"],
            "password": user["password"],
            "title": "Mr",
            "birth_date": user["day"],
            "birth_month": user["month"],
            "birth_year": user["year"],
            "firstname": user["first_name"],
            "lastname": user["last_name"],
            "company": user["company"],
            "address1": user["address1"],
            "address2": user["address2"],
            "country": user["country"],
            "zipcode": user["zipcode"],
            "state": user["state"],
            "city": user["city"],
            "mobile_number": user["mobile"],
        }
        return self.post("/createAccount", data=data)

    def get_user_detail_by_email(self, email):
        return self.get("/getUserDetailByEmail", params={"email": email})

    def delete_account(self, email, password):
        return self.delete("/deleteAccount", data={"email": email, "password": password})
