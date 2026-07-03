import requests

class AuthClient:
    """Class đảm nhận việc gửi request HTTP tới các API Authentication"""
    BASE_URL = "https://thinking-tester-contact-list.herokuapp.com/users"
    HEADERS = {"Content-Type": "application/json"}

    @staticmethod
    def register_user(payload):
        """Gửi request POST để tạo tài khoản mới"""
        return requests.post(AuthClient.BASE_URL, json=payload, headers=AuthClient.HEADERS)

    @staticmethod
    def login_user(email, password):
        """Gửi request POST để đăng nhập"""
        login_url = f"{AuthClient.BASE_URL}/login"
        payload = {"email": email, "password": password}
        return requests.post(login_url, json=payload, headers=AuthClient.HEADERS)