# Swag Labs Sign-in Test Automation

This project automates the testing of the sign-in functionality of the Swag Labs website (https://www.saucedemo.com/). It utilizes Behave for Behavior-Driven Development (BDD) and Selenium for web browser automation, developed within the PyCharm IDE.

## Table of Contents

* [Description](#description)
* [Setup](#setup)
* [Usage](#usage)
* [Features](#features)
* [Test Scenarios](#test-scenarios)
* [Dependencies](#dependencies)
* [Environment](#environment)
* [References](#references)
* [Author](#author)

## Description <a id="description"></a>

This project aims to verify the sign-in functionality of the Swag Labs website. It includes tests for successful logins with valid credentials and failed logins with various invalid credentials, including locked-out user scenarios.

## Setup <a id="setup"></a>

1.  **Install Python 3.12:** Ensure you have Python 3.x installed on your system.
2.  **Setup Project in PyCharm:**
    * Open PyCharm and create a new project or open an existing one.
    * Create a virtual environment for your project within PyCharm.
    * In PyCharm's terminal or using the "Python Packages" tool window, install the required dependencies:
        ```bash
        pip install selenium behave
        ```
3.  **Download ChromeDriver:** Download the appropriate ChromeDriver for your Chrome browser version from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads) and place it in a directory that is in your system's PATH.

## Usage <a id="usage"></a>

To run the tests, navigate to the project directory within PyCharm's terminal and execute the following command:

```bash
behave features/sign_in.feature
```

Alternatively, you can configure a Behave run configuration within PyCharm for easier execution.

## Features <a id="features"></a>

* **Successful login with valid credentials.**
* **Failed login with invalid credentials** (invalid password, invalid username, and empty fields).
* **Handling of locked-out user scenarios.**
* **Display of appropriate error messages for failed login attempts.**

## Test Scenarios <a id="test-scenarios"></a>

* **Successful Login:**
    * Tests successful login with "standard\_user" and "secret\_sauce".
* **Failed Login:**
    * Tests login with various invalid usernames and passwords, including empty fields.
    * Tests login with a locked-out user.
* **Error Message Verification:**
    * Verifies that the correct error messages are displayed for each failed login scenario.

## Dependencies <a id="dependencies"></a>

* **Selenium:** For web browser automation.
* **Behave:** For Behavior-Driven Development (BDD).
* **ChromeDriver:** For controlling the Chrome browser.

## Environment <a id="environment"></a>

* **Operating System:** Tested on Windows 10.
* **Browser:** Google Chrome.
* **Python:** 3.12
* **IDE:** PyCharm

## References <a id="references"></a>

### Official Documentation

* **Selenium Documentation:**
    * Title: Selenium Documentation
    * URL: https://www.selenium.dev/documentation/
* **Behave Documentation:**
    * Title: Behave Documentation
    * URL: https://behave.readthedocs.io/en/stable/
* **Python Documentation:**
    * Title: Python Documentation
    * URL: https://www.python.org/doc/

### Tutorials/Articles

* **Behavior-Driven Development (BDD) with Gherkin:**
    * Title: Gherkin Reference
    * URL: https://cucumber.io/docs/gherkin/reference/
* **Selenium Locators:**
    * Title: Locating Elements
    * URL: https://www.selenium.dev/documentation/webdriver/elements/locating_elements/
* **Behave and Allure Report Tutorial Playlist:**
    * Title: Selenium with Python Behave(BDD)   
    * URL: https://youtube.com/playlist?list=PLUDwpEzHYYLsARXz1o3Ldt1FnvRbvlxsS&si=HrXnqubP8dx6CLcn
    * Description: This playlist taught me all about gherkin and behave, as well as allure reports.

### Stack Overflow/Forums

* **How to generate a single file Allure Report:**
    * Title: Allure report: nothing shown in Chrome
    * URL: https://stackoverflow.com/questions/23997449/allure-report-nothing-shown-in-chrome/78205486#78205486

### Webpage used for Testing

* **SauceDemo webpage:**
    * Title: SauceDemo webpage
    * URL: https://www.saucedemo.com/
 
### Author <a id="author"></a>
Kenneth Roel C. Atienza [kenatienza21]
