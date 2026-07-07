import json
import allure
import pytest
import time
from api.auth_client import AuthClient

@allure.feature("Authentication API")
@allure.suite("API Regression Test")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.api
class TestAuthenticationAPI:

    @allure.story("Đăng ký tài khoản mới")
    @allure.title("Test case 01: Đăng ký tài khoản thành công")
    def test_create_user_successfully(self, get_data):

        with allure.step("Load test data"):
            # Dùng .copy() để không làm thay đổi dữ liệu gốc trong file JSON lưu ở bộ nhớ
            user_payload = get_data("auth_data")["valid_user"].copy()
            
            random_email = f"test_kim_{int(time.time())}@fake.com"
            user_payload["email"] = random_email
            
            # SỬA LỖI TẠI ĐÂY: Thay thế hoàn toàn allure.note bằng dynamic.description
            allure.dynamic.description(f"Email ngẫu nhiên được tạo cho lượt test này: {random_email}")

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
        # Lúc này user_payload sẽ lấy đúng email gốc (ví dụ: test_kim_2026@fake.com) 
        # mà không bị ảnh hưởng bởi email ngẫu nhiên của bài test 1 nữa
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