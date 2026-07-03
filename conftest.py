import json
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
from utils.driver_factory import get_driver


@pytest.fixture
def driver():

    driver = get_driver()

    yield driver

    driver.quit()
    
@pytest.fixture(scope="session")
def get_data():
    def _read_file(file_name):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_file_path = os.path.join(current_dir, "data", f"{file_name}.json")
        
        with open(data_file_path, "r", encoding="utf-8") as f:
            return json.load(f)
            
    return _read_file