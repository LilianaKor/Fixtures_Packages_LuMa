import time
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from faker import Faker


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def custom_base_url():
    return MY_BASE_URL


MY_BASE_URL = "https://magento.softwaretestingboard.com/"


def registration_data(request):
    return request.param


@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, 10)


@pytest.mark.ui
@pytest.mark.registration
@pytest.mark.positive
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("first_name, last_name, email, password", [
    ("", "GAGA", "lgaga1@gmail", "A123456"),
    ("", "GA", "lgaga2@com", "A123457"),
    ("L", "GAk", "$@gmail.com", "A123458")
])
def test_outh_negative(browser, custom_base_url, wait, first_name, last_name, email, password):
    browser.get(f"{MY_BASE_URL}/customer/account/create")

    browser.find_element('xpath', "//input[@id='firstname']").send_keys(first_name)
    browser.find_element(By.XPATH, "//input[@id='lastname']").send_keys(last_name)
    email_field = wait.until(EC.presence_of_element_located((By.ID, "email_address")))
    email_field.send_keys(email)
    browser.save_screenshot(f"screenshot_{email}_2.png")
    browser.find_element(By.XPATH, "//*[@id='password']").send_keys(password)
    browser.find_element(By.XPATH, "//*[@id='password-confirmation']").send_keys(password)
    browser.find_element(By.XPATH, "//button[@title='Create an Account']").click()
    browser.save_screenshot("screenshot.png")
    wait.until(EC.url_changes(f"{MY_BASE_URL}/customer/account/login"))
    # error_message = browser.find_element(By.CSS_SELECTOR, "#firstname-error")
    # assert error_message.is_displayed(), f"Expected first_name validation error message for {first_name}"
    error_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#firstname-error")))
    assert error_message.is_displayed(), f"Expected first_name validation error message for {first_name}"
