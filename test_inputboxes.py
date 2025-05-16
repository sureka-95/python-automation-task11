# import the Pytest framework, which is used for writing and running automated tests in Python
# import Selenium WebDriver, the core tool used to automate web browsers
# Import time module in Python lets you pause your script
# import BY module
# import options

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# set a base url
BASE_URL = "https://www.guvi.in/sign-in/"

# @pytest.fixture is a special decorator in Pytest used to define a function
@pytest.fixture


# define driver function to set options
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

# declare test case for submit button
# validate the input boxes is enabled, visibled or not

def test_input_boxes(driver):
    driver.get(BASE_URL)
    time.sleep(3) # wait atime for 3 seconds
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")

    # use assert statement to check if a condition is true
    # if it is false it print the error message which we wrote after the conditon

    assert email_input.is_displayed() and email_input.is_enabled(), "Email input not visible or enabled"
    assert password_input.is_displayed() and password_input.is_enabled(), "Password input not visible or enabled"

# to know the test result in the console use print message
    print("Email and password field is visible and enabled")