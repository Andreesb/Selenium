
# Facebook Login Test

This project contains an automated test case that verifies the login process on Facebook using Selenium and the UnitTest in Python.

## Pre-conditions

Before running the test case, ensure that you have the following dependencies installed:

Python 3.6 or above - https://www.python.org/downloads/release/python-3114/

Selenium 3.141.0 or above - https://www.selenium.dev/documentation/

Chrome driver - https://chromedriver.chromium.org/downloads




## Getting Started

To get started with running the test case, follow these steps:

1. Open the facebook_login.py file in a text editor.

2. In the test_login method, update the email and password fields with your own test credentials.

3. Save the changes.

4. Open a terminal or command prompt and navigate to the directory where the facebook_login.py file is located.

5. Run the following command to execute the test case: python facebook_login.py

## Test Case Description

The test case facebook_login.py performs the following steps:

1. Opens the Chrome browser and navigate to the Facebook login page.

2. Enters the specified email and password into the login form.

3. Submits the form and waits for the page to load after login.

4. Verifies if the Messenger button is present on the page.

5. Prints "Successfully login" if the Messenger button is found, or "Something went wrong" if the Messenger button is not.

## License


This project is licensed under the MIT License.

