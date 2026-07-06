import requests

class AuthClient:

    BASE_URL = "https://automationexercise.com/api"

    @staticmethod
    def register_user(payload):
        return requests.post(
            f"{AuthClient.BASE_URL}/createAccount",
            data=payload
        )

    @staticmethod
    def login_user(email, password):

        payload = {
            "email": email,
            "password": password
        }

        return requests.post(
            f"{AuthClient.BASE_URL}/verifyLogin",
            data=payload
        )