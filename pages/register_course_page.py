from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class RegisterCoursePage(BasePage):

    URL = "http://127.0.0.1:8000/courses/1/"

    # Locator
    REGISTER_BUTTON = (By.ID, "register-btn")

    TXT_NAME = (By.ID, "name")
    TXT_PHONE = (By.ID, "phone")
    TXT_EMAIL = (By.ID, "email")

    SAVE_BUTTON = (By.ID, "save-btn")

    CONFIRM_NAME = (By.ID, "confirm-name")
    CONFIRM_PHONE = (By.ID, "confirm-phone")
    CONFIRM_EMAIL = (By.ID, "confirm-email")

    AGREE_BUTTON = (By.ID, "agree-btn")

    # Navigation
    def open(self):
        self.driver.get(self.URL)

    # Action
    def click_register_button(self):
        self.click(self.REGISTER_BUTTON)

    def enter_name(self, name):
        self.input_text(self.TXT_NAME, name)

    def enter_phone(self, phone):
        self.input_text(self.TXT_PHONE, phone)

    def enter_email(self, email):
        self.input_text(self.TXT_EMAIL, email)

    def click_save_button(self):
        self.click(self.SAVE_BUTTON)

    def click_agree_button(self):
        self.click(self.AGREE_BUTTON)

    # Business method
    def register_course(self, name, phone, email):
        self.click_register_button()
        self.enter_name(name)
        self.enter_phone(phone)
        self.enter_email(email)
        self.click_save_button()

    # Verify
    def get_confirm_name(self):
        return self.get_text(self.CONFIRM_NAME)

    def get_confirm_phone(self):
        return self.get_text(self.CONFIRM_PHONE)

    def get_confirm_email(self):
        return self.get_text(self.CONFIRM_EMAIL)

    # Alert
    def get_alert_text(self):
        alert = self.wait.until(EC.alert_is_present())
        return alert.text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()