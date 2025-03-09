import pytest
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium import webdriver


def test_outh_positive():
    url = "https://magento.softwaretestingboard.com/customer/account/create/"
    browser = webdriver.Chrome()
    browser.get(url)

    browser.find_element('xpath', "//input[@id='firstname']").send_keys("Lady")
    time.sleep(2)
    browser.find_element(By.XPATH, "//input[@id='lastname']").send_keys("GAGAha")
    browser.find_element(By.XPATH, "//*[@id='email_address']").send_keys("lgagaha@gmail.com")
    browser.find_element(By.XPATH, "//*[@id='password']").send_keys("A123456")
    time.sleep(2)
    browser.find_element(By.XPATH, "//*[@id='password-confirmation']").send_keys("A123456")
    browser.find_element(By.XPATH, "//button[@title='Create an Account']").click()
    time.sleep(2)
    assert browser.current_url == "https://magento.softwaretestingboard.com/customer/account/create/", "URL is not correct"

    browser.quit()

# def test_user():
#     pass

# class TestDataBases:
#     def test_db_connection(self):
#         pass

# def test_positive_registration():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get(url)
#     driver.implicitly_wait(10)
#
#     driver.find_element(By.ID, "firstname").send_keys("Lady")
#     driver.find_element(By.ID, "lastname").send_keys("GAGAha")
#     driver.find_element(By.ID, "email").send_keys("lgagaha@gmail.com")
#     driver.find_element(By.ID, "password1").send_keys("A123456")
#     driver.find_element(By.ID, "password2").send_keys("A123456")
#     driver.find_element(By.ID, "is_subscribed").click()
#     driver.find_element(By.ID, "form-validate").click()

#     driver.quit()
