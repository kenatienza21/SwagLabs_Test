Feature: Swag Labs Sign in Test

  Background: User navigates to the sign in page
    Given the user launches the website "https://www.saucedemo.com/"

  Scenario: Successful Login with Valid Credentials
    # Verify successful login with valid credentials.
    When the user enters a valid username "standard_user"
    And the user enters a valid password "secret_sauce"
    And the user clicks the Sign in button
    Then the user should be logged in successfully

  Scenario Outline: Failed Login with various Invalid Credentials
    # Test various invalid login scenarios.
    When the user enters an invalid username "<username>"
    And the user enters an invalid password "<password>"
    And the user clicks the Sign in button
    Then the user should see an error message "<error_message>"

    # Examples of invalid credentials.
    Examples:
      | username        | password      | error_message                                                             |
      | 1rregul@r_user  | Wrongp@55w0rd | Epic sadface: Username and password do not match any user in this service |
      | locked_out_user | secret_sauce  | Epic sadface: Sorry, this user has been locked out.                       |
      | standard_user   | ""            | Epic sadface: Password is required                                        |
      | ""              | secret_sauce  | Epic sadface: Username is required                                        |
      | ""              | ""            | Epic sadface: Username is required                                        |