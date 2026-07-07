import allure
import pytest

from pages.register_course_page import RegisterCoursePage


@allure.feature("Course Registration")
@allure.story("Register course successfully")
@allure.title("Verify register course with valid information")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui

def test_register_course(driver):

    page = RegisterCoursePage(driver)

    name = "Nguyễn Văn A"
    phone = "0912345678"
    email = "vana@example.com"

    allure.dynamic.parameter("Name", name)
    allure.dynamic.parameter("Phone", phone)
    allure.dynamic.parameter("Email", email)

    with allure.step("Open course page"):
        page.open()

    with allure.step("Register course"):
        page.register_course(name, phone, email)

    with allure.step("Verify confirmation information"):
        assert page.get_confirm_name() == name
        assert page.get_confirm_phone() == phone
        assert page.get_confirm_email() == email

    with allure.step("Click Agree"):
        page.click_agree_button()

    with allure.step("Verify success alert"):
        alert_text = page.get_alert_text()

        assert "Đăng ký thành công" in alert_text

        page.accept_alert()