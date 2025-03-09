import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium import webdriver

# url = "https://magento.softwaretestingboard.com/customer/account/create/"
# login_url = "https://magento.softwaretestingboard.com/customer/account/login/"

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
    # url = "https://magento.softwaretestingboard.com/customer/account/create/"
    # browser = webdriver.Chrome()
    # browser.get(url)
    browser.get(f"{custom_base_url}/customer/account/create")

    browser.find_element('xpath', "//input[@id='firstname']").send_keys("Lady")
    browser.find_element(By.XPATH, "//input[@id='lastname']").send_keys("GAGAha")
    email_field = wait.until(EC.presence_of_element_located((By.ID, "email_address")))
    # EC.url_to_be()
    # EC.presence_of_element_located((By.ID, "email_address"))
    # EC.visibility_of_element_located((By.ID, "email_address"))
    email_field.send_keys("lgagaha@gmail.com")
    # browser.find_element(By.XPATH, "//*[@id='email_address']").send_keys("lgagaha@gmail.com")
    browser.find_element(By.XPATH, "//*[@id='password']").send_keys("A123456")
    browser.find_element(By.XPATH, "//*[@id='password-confirmation']").send_keys("A123456")
    browser.find_element(By.XPATH, "//button[@title='Create an Account']").click()
    # time.sleep(2)
    wait.until(EC.url_changes(f"{custom_base_url}/customer/account/login"))

    assert browser.current_url == f"{custom_base_url}/customer/account/create", "URL is not correct"

    browser.quit()


def test_user():
    pass


class TestDataBases:
    def test_db_connection(self):
        pass


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
#
#     driver.quit()
