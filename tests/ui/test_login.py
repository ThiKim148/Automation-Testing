import pytest
import allure
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait

@allure.feature("Authentication")
@allure.story("Đăng nhập thành công với tài khoản hợp lệ")
@allure.severity(allure.severity_level.BLOCKER) # Chức năng cốt lõi, lỗi này sẽ block toàn bộ hệ thống
@pytest.mark.ui
def test_login(driver):
    # Khởi tạo Page Object
    login_page = LoginPage(driver)
    
    # Định nghĩa dữ liệu test
    username = "testuser"
    password = "Abc12345."

    # Bước 1: Mở trang
    with allure.step("Bước 1: Truy cập vào trang đăng nhập Học Tiếng Thái"):
        login_page.open()
        # Chụp ảnh màn hình đính kèm vào báo cáo để xác nhận trang đã mở thành công
        allure.attach(
            driver.get_screenshot_as_png(), 
            name="Màn hình đăng nhập", 
            attachment_type=allure.attachment_type.PNG
        )

    # Bước 2: Thực hiện hành động Đăng nhập
    with allure.step(f"Bước 2: Nhập tài khoản và mật khẩu"):
        login_page.login(username, password)

    # Bước 3: Kiểm tra kết quả (Assert)
    with allure.step("Bước 3: Xác thực chuyển trang và tiêu đề (Title) chính xác"):
        try:
            # Chờ đợi tối đa 10 giây để tiêu đề trang đổi thành đúng kỳ vọng
            WebDriverWait(driver, 10).until(
                lambda d: d.title == "Học Tiếng Thái Trực Tuyến"
            )
            # Khẳng định (Assert) kết quả
            assert driver.title == "Học Tiếng Thái Trực Tuyến"
            
        except Exception as error:
            # BẪY LỖI: Nếu bước kiểm tra này bị fail (do sai title hoặc timeout)
            # Allure sẽ lập tức chụp ảnh màn hình ngay tại khoảnh khắc bị lỗi đó để bạn dễ debug
            allure.attach(
                driver.get_screenshot_as_png(), 
                name="ẢNH CHỤP LÚC BỊ LỖI", 
                attachment_type=allure.attachment_type.PNG
            )
            raise error # Ném lại lỗi để Pytest đánh dấu case này là FAIL