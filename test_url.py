# import the Pytest framework, which is used for writing and running automated tests in Python
# import Selenium WebDriver, the core tool used to automate web browsers
# Import time module in Python lets you pause your script
# import BY module


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Base URL of the GUVI website
BASE_URL = "https://www.guvi.in/"
EXPECTED_LOGIN_URL = "https://www.guvi.in/sign-in/"

# @pytest.fixture is a special decorator in Pytest used to define a function
@pytest.fixture

# define  browser function
def browser():
    # Initialize Chrome browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# define login button functions
def test_login_button_url(browser):
    browser.get(BASE_URL)

    # Wait for page to load (adjust time or use WebDriverWait for dynamic content)
    time.sleep(3)

    # Find and click the login button
    login_button = browser.find_element(By.LINK_TEXT, "Login")
    href_value = login_button.get_attribute("href")

    # Check href value without clicking
    assert href_value == EXPECTED_LOGIN_URL, f"Login button href is incorrect: {href_value}"

    # Optional: Click the login button to check redirection
    login_button.click()
    time.sleep(2)

    current_url = browser.current_url
    assert current_url == EXPECTED_LOGIN_URL, f"Redirection failed. Landed on: {current_url}"
