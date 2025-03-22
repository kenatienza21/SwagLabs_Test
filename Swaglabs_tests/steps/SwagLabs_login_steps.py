from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('the user launches the website "{url}"')
def step_impl(context, url):
    context.driver.get(str(url))


@when('the user enters a valid username "{valid_username}"')
def step_impl(context, valid_username):
    email_field = context.driver.find_element(By.ID, "user-name")
    email_field.send_keys(valid_username)


@when('the user enters a valid password "{valid_password}"')
def step_impl(context, valid_password):
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys(valid_password)


@when('the user clicks the "Sign in" button')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()


@then('the user should be logged in successfully')
def step_impl(context):
    context.driver.find_element(By.ID, "react-burger-menu-btn").click()
    if not context.driver.find_element(By.ID, "logout_sidebar_link"):
        assert False, "User did not go to the sign in page."
    assert True, "User was able to sign in properly!"

    # WebDriverWait(context.driver, 5).until(
    #     EC.presence_of_element_located((By.ID, "react-burger-menu-btn"))).click()
    # try:
    #     WebDriverWait(context.driver, 5).until(
    #         EC.presence_of_element_located((By.ID, "logout_sidebar_link")))
    # except:
    #     assert False, "User did not go to sign in page"
    # assert True, "User was able to go to sign in page!"


@when('the user enters an invalid username "{invalid_username}"')
def step_impl(context, invalid_username):
    email_field = context.driver.find_element(By.ID, "user-name")
    email_field.send_keys(invalid_username)


@when('the user enters an invalid password "{invalid_password}"')
def step_impl(context, invalid_password):
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys(invalid_password)


@then('the user should see an error message "{error_message}"')
def step_impl(context, error_message):
    actual_message = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3").text
    assert actual_message == error_message

@when('the user enters a locked out username "{locked_username}"')
def step_impl(context, locked_username):
    email_field = context.driver.find_element(By.ID, "user-name")
    email_field.send_keys(locked_username)


@when('the user enters a locked out password "{locked_password}"')
def step_impl(context, locked_password):
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys(locked_password)


@when('the user clicks the "Log In" button without entering credentials')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user clicks the "Log In" button without entering credentials')


@then('the user should see an error message indicating required fields.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user should see an error message indicating required fields.')


@when('the user clicks the "Forgot Password" link')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user clicks the "Forgot Password" link')


@then('the user should be redirected to the password reset page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user should be redirected to the password reset page')


@when('the user clicks the "Reset Password" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user clicks the "Reset Password" button')


@then('the user should see a message indicating a password reset email has been sent.')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the user should see a message indicating a password reset email has been sent.')


@when('the user enters a password "HiddenPassword123!"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user enters a password "HiddenPassword123!"')


@when('the user clicks the "Show Passsword" checkbox')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user clicks the "Show Passsword" checkbox')


@then('the password should be visible in the password field')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the password should be visible in the password field')


@then('the user should see the valid password "Test123!" on the password field')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user should see the valid password "Test123!" on the password field')
