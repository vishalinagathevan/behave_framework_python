from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Reusable function to set up WebDriver with Chrome options
def setup_webdriver(context, headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), 
        options=chrome_options
    )

# Step for navigating to the login page
@given('I navigate to the Login page')
def step_impl(context):
    setup_webdriver(context)
    context.driver.get("https://practicetestautomation.com/practice-test-login/")

# Step for entering login credentials (can be reused)
def enter_login_credentials(context, username, password):
    context.driver.find_element(By.ID, "username").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)

# Scenario: Successful login
@when('I enter valid username and valid password into the fields')
def step_impl(context):
    enter_login_credentials(context, "student", "Password123")

@when('I click on the Login button')
def step_impl(context):
    context.driver.find_element(By.ID, "submit").click()
    time.sleep(2)

@then('I should get logged in')
def step_impl(context):
    success_message = context.driver.find_element(By.CSS_SELECTOR, ".post-title").text
    assert "Logged In Successfully" in success_message, "Login failed!"
    context.driver.quit()

# Scenario: Unsuccessful login
@given('I navigate to Login page with invalid credentials')
def step_impl(context):
    setup_webdriver(context)
    context.driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)

@when('I enter invalid username and valid password into the fields')
def step_impl(context):
    enter_login_credentials(context, "incorrectUser", "Password123")

@then('I should get a proper warning message')
def step_impl(context):
    warning_message = context.driver.find_element(By.CSS_SELECTOR, ".error").text
    assert "Your username is invalid!" in warning_message, "Warning message not shown!"
    context.driver.quit()
