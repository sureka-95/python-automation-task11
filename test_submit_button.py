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

#SET A webdriver
driver = webdriver.Chrome

#set a base url
BASE_URL = "https://www.guvi.in/sign-in/"

# @pytest.fixture is a special decorator in Pytest used to define a function
@pytest.fixture

# define driver function
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

#call the driver function in test class
# positive testcase for submit button
def test_submit_button(driver):
    driver.get(BASE_URL)

    time.sleep(3)# driver wait for3 sec

# search the input by id
    email_input = driver.find_element(By.ID, "email")

    #send_keys used to type input
    email_input.send_keys("surekavj@gmail.com")
    time.sleep(2)# wait a driver for 2 sec

    # find password by id
    password_input = driver.find_element(By.ID, "password")
    # send_keys used to type input
    password_input.send_keys("sureka95")
    time.sleep(2)# wait a driver for 2 sec

#find submit button using by id
    submit_button = driver.find_element(By.ID,"login-btn")

    # assert statement used to check  button is displayed and enabled
    assert submit_button.is_displayed() and submit_button.is_enabled(), "Submit button not working"
    #click the button to validate is working or not
    submit_button.click()

# negative testcase for submit button without credentials
def test_submit_button_with_empty_credentials(driver):
    driver.get(BASE_URL)
    submit_button = driver.find_element(By.ID, "login-btn")
    # assert statement used to check  button is displayed and enabled
    assert submit_button.is_displayed() and submit_button.is_enabled(), "Submit button not working"
    # click the button to validate is working or not
    submit_button.click()

 # get  the output using  print
    print("submit button not working with empty credentials")
