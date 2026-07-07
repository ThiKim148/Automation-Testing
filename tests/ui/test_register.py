import uuid

import allure
import pytest
from pages.register_page import RegisterPage
from selenium.webdriver.support.ui import WebDriverWait

@allure.feature("Authentication")
@allure.story("Đăng ký thành công với tài khoản hợp lệ")
@allure.severity(allure.severity_level.BLOCKER) # Chức năng cốt lõi, lỗi này sẽ block toàn bộ hệ thống
@pytest.mark.ui

def test_register(driver):
    
    register_page = RegisterPage(driver)
    
    username = f"testuser_{uuid.uuid4().hex[:8]}"
    email = f"testuser_{uuid.uuid4().hex[:8]}@example.com"
    phone = "0323456789"
    password = "Abc12345."

    with allure.step("Bước 1: Truy cập vào trang đăng ký Học Tiếng Thái"):
        register_page.open()
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    with allure.step(f"Bước 2: Nhập thông tin đăng ký: Tài khoản: {username}, Email: {email}, Số điện thoại: {phone}, Mật khẩu: {password}"):
        register_page.register(
            username,
            email,
            phone,
            password,
            password
        )
        
    with allure.step("Bước 3: Xác thực chuyển trang và tiêu đề (Title) chính xác"):
        try:
            WebDriverWait(driver, 10).until(
                lambda d: d.title == "Học Tiếng Thái Trực Tuyến"
            )
            assert driver.title == "Học Tiếng Thái Trực Tuyến"
        except Exception as e:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            raise e