
# Facebook Login Test

This project contains a set of automated tests for the Facebook login functionality using Selenium in Python.

## Pre-conditions

Before running the test case, ensure that you have the following dependencies installed:

Python 3.6 or above - https://www.python.org/downloads/release/python-3114/

Selenium 3.141.0 or above - https://www.selenium.dev/documentation/

Chrome driver - https://chromedriver.chromium.org/downloads


## Overwiew 

The purpose of these tests is to validate the Facebook login function with different credentials and the recovery password functionality. 

The tests are implemented using the Selenium WebDriver. 

Facebook_login.py executes the following test cases: 
Test 'Valid credentials', test 'Invalid username', test 'Invalid password', test 'Empty credentials', test 'Uppercase username', and test 'Uppercase password'.

Password_recovery executes the following test cases:
Test 'Valid email', test 'Invalid email', test 'No format', test 'Invalid format'.


You can add more test cases if you need.


The test results are logged in a file named facebook_login_tests.log, stored in the specified file path. The log file provides information about the test execution and the result of each test case.


## Getting Started

To get started with running the tests, follow these steps:

1. Open any of the tests in a text editor.

2. In the log_file_path update the desired directory for the tests output.

3. In the test cases list, update the email and password fields with your own test credentials.

4. Save the changes.

5. Open a terminal or command prompt and navigate to the directory where the file is located.

6. Run the tests: python facebook_login.py


## License

This project is licensed under the MIT License.

