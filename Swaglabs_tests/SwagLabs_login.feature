Feature: Swag Labs Sign in Test

  Background: User navigates to the sign in page
    Given the user launches the website "https://www.saucedemo.com/"

  Scenario: Successful Login with Valid Credentials
    When the user enters a valid username "standard_user"
    And the user enters a valid password "secret_sauce"
    And the user clicks the "Sign in" button
    Then the user should be logged in successfully

  Scenario: Failed Login with Invalid Credentials
    When the user enters an invalid username "invalidcredentials21"
    And the user enters an invalid password "Wrongp@55w0rd"
    And the user clicks the "Sign in" button
    Then the user should see an error message "Epic sadface: Username and password do not match any user in this service"

  Scenario: Failed Login with Locked out user Credentials
    When the user enters a locked out username "locked_out_user"
    And the user enters a locked out password "secret_sauce"
    And the user clicks the "Sign in" button
    Then the user should see an error message "Epic sadface: Sorry, this user has been locked out."