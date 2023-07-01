
# Facebook Login Test

This project contains an automated test case that verifies the login process on Facebook using the Selenium and the UnitTest in Python.

## Pre-conditions

Before running the test case, ensure that you have the following dependencies installed:

Python 3.6 or above

Selenium 3.141.0 or above

Chrome driver




## Getting Started

To get started with running the test case, follow these steps:

1. Clone this repository to your local machine or download the source code.

2. Install the required dependencies by running the following command: pip install selenium

3. Make sure you have the Chrome driver installed and available in the system path. You can download the Chrome driver from the official website: https://chromedriver.chromium.org/home

4. Open the facebook_login.py file in a text editor.

5. In the test_login method, update the email and password fields with your own test credentials.

6. Save the changes.

7. Open a terminal or command prompt and navigate to the directory where the facebook_login.py file is located.

8. Run the following command to execute the test case: python facebook_login.py

## Test Case Description

The test case facebook_login.py performs the following steps:

1. Opens the Chrome browser and navigates to the Facebook login page.

2. Enters the specified email and password into the login form.

3. Submits the form and waits for the page to load after login.

4. Verifies if the Messenger button is present on the page.

5. Prints "Successfully login" if the Messenger button is found, or "Something went wrong" if the Messenger button is not found.

## License


This project is licensed under the MIT License.

