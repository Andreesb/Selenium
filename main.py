from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
import datetime



current_datetime = datetime.datetime.now()

log_file_path = r"C:\Users\Andresb\Desktop\FacebookTests\facebook_login_tests.log"

def verify_login(username, password, test_name, log_file):
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.facebook.com/")
        time.sleep(2)
        user = driver.find_element(By.ID, "email")
        user.send_keys(username)
        password_input = driver.find_element(By.ID, "pass")
        password_input.send_keys(password)
        password_input.submit()
        time.sleep(3)

        try:
            success = driver.find_elements(By.CSS_SELECTOR, ".x9f619.x1n2onr6.x1ja2u2z")
            if success:
                result = f"Test '{test_name}': Login successful"
            else:
                result = f"Test '{test_name}': Failed to log in"
        except NoSuchElementException:
            result = f"Test '{test_name}': Error during login"
        log_file.write(result + "\n" )


    finally:
        driver.quit()


test_cases = [
    {"username": "juantestt2023@gmail.com", "password": "JuantesT2023", "test_name": "Valid credentials"},
    {"username": "invalid_username", "password": "JuantesT2023", "test_name": "Invalid username"},
    {"username": "juantestt2023@gmail.com", "password": "invalid_password", "test_name": "Invalid password"},
    {"username": "", "password": "", "test_name": "Empty credentials"},
    {"username": "JUANTESTT2023@GMAIL.COM", "password": "JuantesT2023", "test_name": "Uppercase username"},
    {"username": "juantestt2023@gmail.com", "password": "JUANTEST2023", "test_name": "Uppercase password"}


]
with open(log_file_path, "a") as log_file:
    log_file.write(f"\n\n--- Tested at {current_datetime.strftime('%Y-%m-%d %H:%M:%S')} ---\n\n")
    for index, test_case in enumerate(test_cases, start=1):
        print(f"Test Case #{index}: {test_case['test_name']}")
        verify_login(test_case["username"], test_case["password"], test_case["test_name"], log_file)
        print()

log_file.close()



