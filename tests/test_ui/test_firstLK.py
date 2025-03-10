import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver

MY_BASE_URL = "https://magento.softwaretestingboard.com/"


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    # test runs and closes the browser
    yield browser
    browser.quit()
    # and finally close the browser and DB close


@pytest.fixture
def custom_base_url():
    return MY_BASE_URL


@pytest.fixture
def registration_data():
    return {
        "first_name": "Lady",
        "last_name": "GAGAha",
        "email": "lgagaha@gmail.com",
        "password": "A123456"
    }


@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, 10)


def test_outh_positive(browser, custom_base_url, wait, registration_data):

    browser.get(f"{custom_base_url}/customer/account/create")

    browser.find_element('xpath', "//input[@id='firstname']").send_keys("registration_data", 'first_name')
    browser.find_element(By.XPATH, "//input[@id='lastname']").send_keys('registration_data', 'last_name')
    email_field = wait.until(EC.presence_of_element_located((By.ID, "email_address")))
    email_field.send_keys('registration_data', 'email')
    # browser.find_element(By.XPATH, "//*[@id='email_address']").send_keys("lgagaha@gmail.com")
    # browser.find_element(By.XPATH, "//*[@id='password']").send_keys("A123456")
    browser.find_element(By.XPATH, "//*[@id='password']").send_keys('registration_data','password')
    browser.find_element(By.XPATH, "//*[@id='password-confirmation']").send_keys("A123456")
    browser.find_element(By.XPATH, "//button[@title='Create an Account']").click()
    wait.until(EC.url_changes(f"{custom_base_url}/customer/account/login"))

    assert browser.current_url == f"{custom_base_url}/customer/account/create", "URL is not correct"

    browser.quit()


def test_user():
    pass


class TestDataBases:
    def test_db_connection(self):
        pass



