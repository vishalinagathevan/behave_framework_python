from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# # Reusable function to set up WebDriver with Chrome options
def setup_webdriver(context, headless=True):
    # context.driver = webdriver.Chrome()  # Initialize the Chrome driver
    # context.driver.maximize_window()  # Maximize the browser window
    # context.driver.get("https://practicetestautomation.com/practice-test-login/")  # Navigate to login page
    # time.sleep(2)
    
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

# Scenario: Successful login
@given('I navigate to the Login page')
def step_impl(context):
    setup_webdriver(context)
    context.driver.get("https://practicetestautomation.com/practice-test-login/")

@when('I enter valid username and valid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, "username").send_keys("student")  # Enter valid username
    context.driver.find_element(By.ID, "password").send_keys("Password123")  # Enter valid password

@when('I click on the Login button')
def step_impl(context):
    context.driver.find_element(By.ID, "submit").click()  # Click the login button
    time.sleep(2)

@then('I should get logged in')
def step_impl(context):
    success_message = context.driver.find_element(By.CSS_SELECTOR, ".post-title").text
    assert "Logged In Successfully" in success_message, "Login failed!"
    context.driver.quit()

# Scenario: Login with invalid username and valid password
@given('I navigated to Login page')
def step_impl(context):
    setup_webdriver(context)
    context.driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)

@when('I enter invalid username and valid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, "username").send_keys("incorrectUser")  # Enter invalid username
    context.driver.find_element(By.ID, "password").send_keys("Password123")  # Enter valid password

@when('I click on Login button')
def step_impl(context):
    context.driver.find_element(By.ID, "submit").click()  # Click the login button
    time.sleep(2)

@then('I should get a proper warning message')
def step_impl(context):
    # Update this selector according to the actual HTML structure
    warning_message = context.driver.find_element(By.ID, "error").text  # Locate the error message
    assert "Your username is invalid!" in warning_message, "Warning message not shown!"
    context.driver.quit()
