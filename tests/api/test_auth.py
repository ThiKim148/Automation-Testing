import json
import allure
import pytest

from api.auth_client import AuthClient

@allure.feature("Authentication API")
@allure.suite("API Regression Test")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.api
class TestAuthenticationAPI:

    @allure.story("Đăng ký tài khoản mới")
    @allure.title("Test case 01: Đăng ký tài khoản thành công")
    def test_create_user_successfully(self, test_user):

        with allure.step("Load test data"):
            allure.attach(
                json.dumps(test_user, indent=4),
                "Request Payload",
                allure.attachment_type.JSON
            )

        with allure.step("Call Create Account API"):
            response = AuthClient.register_user(test_user)

            allure.attach(
                response.text,
                "Response",
                allure.attachment_type.TEXT
            )

        with allure.step("Verify response"):
            assert response.status_code == 200

            response_data = response.json()

            assert response_data["responseCode"] == 201
            assert response_data["message"] == "User created!"

    @allure.story("Đăng nhập")
    @allure.title("Test case 02: Verify Login")
    def test_login_successfully(self, test_user):

        with allure.step("Call Verify Login API"):
            response = AuthClient.login_user(
                test_user["email"],
                test_user["password"]
            )

            allure.attach(
                response.text,
                "Response",
                allure.attachment_type.TEXT
            )

        with allure.step("Verify response"):
            assert response.status_code == 200

            response_data = response.json()

            assert response_data["responseCode"] == 200
            assert response_data["message"] == "User exists!"

    @allure.story("Xóa tài khoản")
    @allure.title("Test case 03: Delete Account")
    def test_delete_user(self, test_user):

        with allure.step("Call Delete Account API"):
            response = AuthClient.delete_user(
                test_user["email"],
                test_user["password"]
            )

            allure.attach(
                response.text,
                "Response",
                allure.attachment_type.TEXT
            )

        with allure.step("Verify response"):
            assert response.status_code == 200

            response_data = response.json()

            assert response_data["responseCode"] == 200
            assert response_data["message"] == "Account deleted!"