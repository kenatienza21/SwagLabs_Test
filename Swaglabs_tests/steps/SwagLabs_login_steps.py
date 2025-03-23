from behave import given, when, then
from selenium.webdriver.common.by import By


@given('the user launches the website "{url}"')
def step_impl(context, url):
    context.driver.get((url))


@when('the user enters a valid username "{valid_username}"')
def step_impl(context, valid_username):
    email_field = context.driver.find_element(By.ID, "user-name")
    email_field.send_keys(valid_username)


@when('the user enters a valid password "{valid_password}"')
def step_impl(context, valid_password):
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys(valid_password)


@when('the user clicks the Sign in button')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()


@then('the user should be logged in successfully')
def step_impl(context):
    context.driver.find_element(By.ID, "react-burger-menu-btn").click()
    if not context.driver.find_element(By.ID, "logout_sidebar_link"):
        assert False, "User did not go to the sign in page."
    assert True, "User was able to sign in properly!"


@when('the user enters an invalid username "{invalid_username}"')
def step_impl(context, invalid_username):
    username_field = context.driver.find_element(By.ID, "user-name")
    if invalid_username == '""':
        username_field.clear()
    else:
        username_field.send_keys(invalid_username)


@when('the user enters an invalid password "{invalid_password}"')
def step_impl(context, invalid_password):
    password_field = context.driver.find_element(By.ID, "password")
    if invalid_password == '""':
        password_field.clear()
    else:
        password_field.send_keys(invalid_password)


@then('the user should see an error message "{error_message}"')
def step_impl(context, error_message):
    actual_message = context.driver.find_element(By.CSS_SELECTOR, '[data-test="error"]').text
    assert actual_message == error_message
