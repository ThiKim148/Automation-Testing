import json
import allure
import pytest
from api.auth_client import AuthClient
from conftest import get_data  # Đảm bảo đúng folder api_clients của bạn


@allure.feature("Authentication API")
@allure.suite("API Regression Test")  # Gom nhóm tập hợp các bài test API
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.api
class TestAuthenticationAPI:

    @allure.story("Đăng ký tài khoản mới")
    @allure.title("Test case 01: Đăng ký tài khoản thành công")
    def test_create_user_successfully(self, get_data):

        with allure.step("Load test data"):
            user_payload = get_data("auth_data")["valid_user"]

        with allure.step("Call Create Account API"):
            response = AuthClient.register_user(user_payload)

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
    def test_login_successfully(self, get_data):

        user_payload = get_data("auth_data")["valid_user"]

        response = AuthClient.login_user(
            user_payload["email"],
            user_payload["password"]
        )

        allure.attach(
            response.text,
            "Response",
            allure.attachment_type.TEXT
        )

        assert response.status_code == 200

        response_data = response.json()

        assert response_data["responseCode"] == 200
        assert response_data["message"] == "User exists!"