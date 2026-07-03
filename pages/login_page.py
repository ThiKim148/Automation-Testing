from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    URL = "http://127.0.0.1:8000/login/"
    
    txt_username = (By.ID, "id_username")
    txt_password = (By.ID, "id_password")
    btn_login = (By.ID, "login_button")
    
    def open(self):
        self.driver.get(self.URL)
        
    def login(self, username, password):
        self.input_text(self.txt_username, username)
        self.input_text(self.txt_password, password)
        self.click(self.btn_login)

