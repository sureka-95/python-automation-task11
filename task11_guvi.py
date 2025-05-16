# import webdriver
# import service module
# use By module is a helper class that lets you specify how to locate elements
# import module expected_condition EC contains predefined conditions
# import WebDriverWait, which is used to perform explicit waits


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode
chrome_options.add_argument("--disable-infobars")  # Disabling infobars
chrome_options.add_argument("--disable-extensions")  # Disabling extensions


# Replace these with your actual GUVI credentials
Email_Address = "suan@gmail.com"
Password = "password"

# Setup Chrome options
options = Options()
options.add_argument("--start-maximized")

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Step 1: Go to GUVI Sign-in page
    driver.get("https://www.guvi.in/")
    time.sleep(2)

    # Step 2: Click Login
    login_button = driver.find_element(By.LINK_TEXT, "Login")
    login_button.click()
    time.sleep(2)

    #step 3: verify redirection
    assert driver.current_url == "https://www.guvi.in/sign-in/", "Login button did not navigate to the correct page"

    # Step 4: Enter email
    email_input = driver.find_element(By.ID,"email")
    email_input.send_keys("suam@gmail.com")
    time.sleep(2)

    # Step 5: Enter password
    password_input = driver.find_element(By.ID,"password")
    password_input.send_keys("psword")
    time.sleep(2)


    # Step 6: Wait for redirect and print final URL
    print("Logged in successfully. Current URL:", driver.current_url)

finally:
    driver.quit()
