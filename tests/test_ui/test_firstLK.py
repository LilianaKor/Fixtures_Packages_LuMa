import time
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from faker import Faker


# fake = Faker()

@pytest.fixture
def faker_data():
    fake = Faker()
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.ascii_free_email(),
        "password": fake.password(length=8)
    }


# MY_BASE_URL = "https://magento.softwaretestingboard.com/"
#   https://magento.softwaretestingboard.com/customer/account/create/

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


# @pytest.fixture(params=[
#     {"first_name": "Lady",
#      "last_name": "GAGAha",
#      "email": "lgaga1@gmail.com",
#      "password": "A123456"},
#     {"first_name": "La",
#      "last_name": "GAG",
#      "email": "lgaga2@gmail.com",
#      "password": "A123457"},
#     {"first_name": "Ly",
#      "last_name": "GAk",
#      "email": "lgagaha@gmail.com",
#      "password": "A123458"}
# ])
def registration_data(request):
    return request.param


@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, 10)


# @pytest.mark.ui
# @pytest.mark.registration
# @pytest.mark.positive
# @pytest.mark.smoke
# @pytest.mark.regression
# @pytest.mark.parametrize("first_name, last_name, email, password",[
#     ("Lady", "GAGAha", "lgaga1@gmail.com", "A123456"),
#     ("La", "GAG", "lgaga2@gmail.com", "A123457"),
#     ("Lu", "GAk", "lgagaha@gmail.com", "A123458")
# ])
# def test_outh_positive(browser, custom_base_url, wait, registration_data):
#     browser.get(f"{custom_base_url}/customer/account/create")
#
#     browser.find_element('xpath', "//input[@id='firstname']").send_keys(registration_data['first_name'])
#     browser.find_element(By.XPATH, "//input[@id='lastname']").send_keys(registration_data['last_name'])
#     email_field = wait.until(EC.presence_of_element_located((By.ID, "email_address")))
#     email_field.send_keys(registration_data['email'])
#     # browser.find_element(By.XPATH, "//*[@id='email_address']").send_keys("lgagaha@gmail.com")
#     # browser.find_element(By.XPATH, "//*[@id='password']").send_keys("A123456")
#     browser.find_element(By.XPATH, "//*[@id='password']").send_keys(registration_data['password'])
#     browser.find_element(By.XPATH, "//*[@id='password-confirmation']").send_keys(registration_data['password'])
#     browser.find_element(By.XPATH, "//button[@title='Create an Account']").click()
#     wait.until(EC.url_changes(f"{custom_base_url}/customer/account/login"))
#     assert browser.current_url == f"{custom_base_url}/customer/account/create", "URL is not correct"

# @pytest.mark.ui
# @pytest.mark.registration
# @pytest.mark.positive
# @pytest.mark.smoke
# @pytest.mark.regression
# @pytest.mark.parametrize("first_name, last_name, email, password",[
#     ("Lady", "GAGAha", "lgaga1@gmail.com", "A123456"),
#     ("La", "GAG", "lgaga2@gmail.com", "A123457"),
#     ("Lu", "GAk", "lgagaha@gmail.com", "A123458")
# ])
# def test_outh_positive(browser, custom_base_url, wait, first_name, last_name, email, password):
#     browser.get(f"{custom_base_url}/customer/account/create")
#
#     browser.find_element('xpath', "//input[@id='firstname']").send_keys(first_name)
#     browser.find_element(By.XPATH, "//input[@id='lastname']").send_keys(last_name)
#     email_field = wait.until(EC.presence_of_element_located((By.ID, "email_address")))
#     email_field.send_keys(email)
#     browser.find_element(By.XPATH, "//*[@id='password']").send_keys(password)
#     browser.find_element(By.XPATH, "//*[@id='password-confirmation']").send_keys(password)
#     browser.find_element(By.XPATH, "//button[@title='Create an Account']").click()
#     wait.until(EC.url_changes(f"{custom_base_url}/customer/account/login"))
#     assert browser.current_url == f"{custom_base_url}/customer/account/create", "URL is not correct"
#     time.sleep(4)
#     browser.quit()


# def test_outh_positive(browser, custom_base_url, wait, faker_data):
#     browser.get(f"{custom_base_url}/customer/account/create")
#
#     browser.find_element('xpath', "//input[@id='firstname']").send_keys(faker_data['first_name'])
#     browser.find_element(By.XPATH, "//input[@id='lastname']").send_keys(faker_data['last_name'])
#     email_field = wait.until(EC.presence_of_element_located((By.ID, "email_address")))
#     email_field.send_keys(faker_data['email'])
#     browser.find_element(By.XPATH, "//*[@id='password']").send_keys(faker_data['password'])
#     browser.find_element(By.XPATH, "//*[@id='password-confirmation']").send_keys(faker_data['password'])
#     browser.find_element(By.XPATH, "//button[@title='Create an Account']").click()
#     wait.until(EC.url_changes(f"{custom_base_url}/customer/account/login"))
#     assert browser.current_url == f"{custom_base_url}/customer/account/create", "URL is not correct"
#     time.sleep(4)
#     browser.quit()


MY_BASE_URL = "https://magento.softwaretestingboard.com"


def test_outh_positive(browser, custom_base_url, wait, faker_data):
    browser.get(f"{custom_base_url}/customer/account/create")

    browser.find_element(By.XPATH, "//input[@id='firstname']").send_keys(faker_data['first_name'])
    browser.find_element(By.XPATH, "//input[@id='lastname']").send_keys(faker_data['last_name'])
    email_field = wait.until(EC.presence_of_element_located((By.ID, "email_address")))
    email_field.send_keys(faker_data['email'])
    browser.find_element(By.XPATH, "//*[@id='password']").send_keys(faker_data['password'])
    browser.find_element(By.XPATH, "//*[@id='password-confirmation']").send_keys(faker_data['password'])
    browser.find_element(By.XPATH, "//button[@title='Create an Account']").click()

    wait.until(EC.url_contains("/customer/account/"))  # More flexible wait condition
    #assert browser.current_url.rstrip('/') == f"{custom_base_url}/customer/account", "URL is not correct"
#assert browser.current_url.rstrip('/') == f"{custom_base_url.rstrip('/')}/customer/account", "URL is not correct"

    # assert browser.current_url == f"{custom_base_url}/customer/account", "URL is not correct"
    assert "/customer/account/create" in browser.current_url, "URL is not correct"

# def test_user():
#     pass

# class TestDataBases:
#     def test_db_connection(self):
#         pass
