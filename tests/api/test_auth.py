import json
import allure
import pytest
import time  # Thêm thư viện để tạo chuỗi ngẫu nhiên bằng timestamp
from api.auth_client import AuthClient

# KHÔNG IMPORT GET_DATA TỪ CONFEST NỮA!

@allure.feature("Authentication API")
@allure.suite("API Regression Test")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.api
class TestAuthenticationAPI:

    @allure.story("Đăng ký tài khoản mới")
    @allure.title("Test case 01: Đăng ký tài khoản thành công")
    def test_create_user_successfully(self, get_data):

        with allure.step("Load test data"):
            user_payload = get_data("auth_data")["valid_user"]
            
            # GIẢI PHÁP SỐNG CÒN: Fake email bằng timestamp để không bao giờ bị trùng (400)
            random_email = f"test_kim_{int(time.time())}@fake.com"
            user_payload["email"] = random_email
            allure.note(f"Email ngẫu nhiên được tạo cho lượt test này: {random_email}")

        with allure.step("Call Create Account API"):
            response = AuthClient.register_user(user_payload)

            allure.attach(
                response.text,
                "Response",
                allure.attachment_type.TEXT
            )

        with allure.step("Verify response"):
            # Vỏ ngoài luôn là 200 OK theo thiết kế của trang Automation Exercise
            assert response.status_code == 200 

            response_data = response.json()
            assert response_data["responseCode"] == 201
            assert response_data["message"] == "User created!"

    @allure.story("Đăng nhập")
    @allure.title("Test case 02: Verify Login")
    def test_login_successfully(self, get_data):
        """
        LƯU Ý PHẢN BIỆN: Bài test này dùng email tĩnh từ file JSON.
        Nó chỉ PASSED nếu tài khoản đó ĐÃ TỒN TẠI trên hệ thống.
        """
        user_payload = get_data("auth_data")["valid_user"]

        # Vì bài test 1 phía trên đã đổi email ngẫu nhiên, bài test 2 này 
        # nên dùng một email cố định đã được đăng ký sẵn từ trước trên hệ thống (ví dụ: email mặc định trong JSON)
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