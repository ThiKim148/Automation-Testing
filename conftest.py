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
