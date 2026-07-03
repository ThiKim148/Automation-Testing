from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):
    
    URL = "http://127.0.0.1:8000/register/"
    
    txt_username = (By.ID, "id_username")
    txt_email = (By.ID, "id_email")
    txt_phone = (By.ID, "id_phone")
    txt_password = (By.ID, "id_password1")
    txt_confirm_password = (By.ID, "id_password2")
    btn_register = (By.ID, "register_button")
    
    def open(self):
        self.driver.get(self.URL)
        
    def register(self, username, email, phone, password, confirm_password):
        self.input_text(self.txt_username, username)
        self.input_text(self.txt_email, email)
        self.input_text(self.txt_phone, phone)
        self.input_text(self.txt_password, password)
        self.input_text(self.txt_confirm_password, confirm_password)
        self.click(self.btn_register)
        
