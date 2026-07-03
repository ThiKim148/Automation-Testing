import json
import allure
import pytest
from api.auth_client import AuthClient  # Đảm bảo đúng folder api_clients của bạn


@allure.feature("Authentication API")
@allure.suite("API Regression Test")  # Gom nhóm tập hợp các bài test API
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.api
class TestAuthenticationAPI:

    @allure.story("Đăng ký tài khoản mới")
    @allure.title("Test case 01: Đăng ký tài khoản thành công với dữ liệu hợp lệ") # Định nghĩa tiêu đề trực quan trên Allure
    def test_create_user_successfully(self, get_data):
        """Kịch bản 1: Chỉ xử lý logic kiểm tra Đăng ký tài khoản mới"""
        
        with allure.step("Bước 1: Nạp dữ liệu test đăng ký từ file JSON"):
            user_payload = get_data("auth_data")["valid_user"]
            allure.attach(json.dumps(user_payload, indent=4), name="Request Payload (Dự kiến)", attachment_type=allure.attachment_type.JSON)
        
        with allure.step("Bước 2: Gọi API Client thực hiện đăng ký"):
            response = AuthClient.register_user(user_payload)
            # Đính kèm Response thực tế nhận được từ Server Heroku vào báo cáo Allure
            allure.attach(json.dumps(response.json(), indent=4), name="Response Body (Thực tế)", attachment_type=allure.attachment_type.JSON)
            allure.attach(str(response.status_code), name="Response Status Code", attachment_type=allure.attachment_type.TEXT)
        
        with allure.step("Bước 3: Kiểm tra logic và mã trạng thái"):
            if response.status_code == 400:
                pytest.skip("Tài khoản email này đã được tạo từ trước.")
                
            assert response.status_code == 201
            response_data = response.json()
            assert "user" in response_data
            assert response_data["user"]["email"] == user_payload["email"]
            assert "token" in response_data



    @allure.story("Đăng nhập hệ thống")
    @allure.title("Test case 02: Đăng nhập thành công và nhận Access Token")
    def test_login_successfully(self, get_data):
        """Kịch bản 2: Chỉ xử lý logic kiểm tra Đăng nhập thành công"""
        
        with allure.step("Bước 1: Lấy thông tin đăng nhập hợp lệ"):
            user_payload = get_data("auth_data")["valid_user"]
            
        with allure.step("Bước 2: Gửi request đăng nhập hệ thống"):
            response = AuthClient.login_user(user_payload["email"], user_payload["password"])
            allure.attach(json.dumps(response.json(), indent=4), name="Response Login Body", attachment_type=allure.attachment_type.JSON)
        
        with allure.step("Bước 3: Xác thực thông tin đăng nhập thành công"):
            assert response.status_code == 200
            response_data = response.json()
            assert "token" in response_data
            assert response_data["user"]["firstName"] == user_payload["firstName"]