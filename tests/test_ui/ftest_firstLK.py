import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

url = "https://magento.softwaretestingboard.com/customer/account/create/"


def test_user():
    pass


class TestDataBases:
    def test_db_connection(self):
        pass


def test_positive_registration():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    driver.implicitly_wait(10)

    driver.find_element_by_id("firstname").send_keys("Lady")
    driver.find_element_by_id("lastname").send_keys("GAGAha")
    driver.find_element_by_id("email").send_keys("lgagaha@gmail.com")
    driver.find_element_by_id("password1").send_keys("A123456")
    driver.find_element_by_id("password2").send_keys("A123456")
    driver.find_element_by_id("is_subscribed").click()
    driver.find_element_by_id("form-validate").click()
    driver.quit()


time.sleep(5)
