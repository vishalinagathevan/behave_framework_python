from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step definition for navigating to the login page
@given('I navigate to the Login page')
def step_impl(context):
    context.driver = webdriver.Chrome()  # Initialize the Chrome driver
    context.driver.maximize_window()  # Maximize the browser window
    context.driver.get("https://practicetestautomation.com/practice-test-login/")  # Navigate to login page
    time.sleep(2)  

# Step definition for entering valid username and password
@when('I enter valid username and valid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, "username").send_keys("student")  # Enter username
    context.driver.find_element(By.ID, "password").send_keys("Password123")  # Enter password

# Step definition for clicking the login button
@when('I click on the Login button')
def step_impl(context):
    context.driver.find_element(By.ID, "submit").click()  # Click the login button
    time.sleep(2)  
    
# Step definition to verify that login was successful
@then('I should get logged in')
def step_impl(context):
    success_message = context.driver.find_element(By.CSS_SELECTOR, ".post-title").text  # Verify login success
    assert "Logged In Successfully" in success_message, "Login failed!"
    context.driver.quit()  # Close the browser
    
    
@given('I navigated to Login page')
def step_impl(context):
    context.driver = webdriver.Chrome()  # Initialize the Chrome driver
    context.driver.maximize_window()  # Maximize the browser window
    context.driver.get("https://practicetestautomation.com/practice-test-login/")  # Navigate to login page
    time.sleep(2) 
    # raise NotImplementedError(u'STEP: Given I navigated to Login page')


@when('I enter invalid username and vaild password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, "username").send_keys("incorrectUser")  # Enter username
    context.driver.find_element(By.ID, "password").send_keys("Password123")  # Enter password
    # raise NotImplementedError(u'STEP: When I enter invalid username and vaild password into the fields')     


@when('I click on Login button')
def step_impl(context):
    context.driver.find_element(By.ID, "submit").click()  # Click the login button
    time.sleep(2)
    # raise NotImplementedError(u'STEP: When I click on Login button')


@then('I should get a proper warnig message')
def step_impl(context):
    # success_message = context.driver.find_element(By.CSS_SELECTOR, ".post-title").text  # Verify login success
    # assert "Logged In Successfully" in success_message
    context.driver.quit()  # Close the browser
    # raise NotImplementedError(u'STEP: Then I should get a proper warnig message')    
