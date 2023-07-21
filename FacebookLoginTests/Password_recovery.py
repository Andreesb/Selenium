from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import pyperclip

current_datetime = datetime.datetime.now()

log_file_path = r"C:\YOUR\DESIRED\DIRECTORY\facebook_restart_password_tests.log"

def forget_psw_test(username, passwrd, test_name, log_file):
    driver = webdriver.Chrome()
    user = "PROFILE NAME"
    custome_pasword_1 =  "NEW PASSWORD"
    try:
        driver.get("https://www.facebook.com/")
        time.sleep(2)
        driver.find_element(By.PARTIAL_LINK_TEXT, "¿Olvidaste tu contraseña?").click()
        email_user = driver.find_element(By.CSS_SELECTOR,".inputtext._9o1w")
        email_user.send_keys(username)
        email_user.submit()
        time.sleep(2)

        if driver.find_element(By.CSS_SELECTOR, ".fsl.fwb.fcb").text == user:
            
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/form/div/div[3]/div/div[1]/a").click()
                time.sleep(1)
                select_option = driver.find_element(By.ID, "send_email").is_selected()

                success = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[2]/form/div/div[3]/div/div[1]/button")

                try:
                    success.click()
                    result = f"Test '{test_name}': An email was sent. \n\ "
                    time.sleep(2)
                    
                    try:
                        driver.execute_script("window.open("");")
                        time.sleep(2)
                        driver.switch_to.window(driver.window_handles[1])
                        driver.get("http://www.gmail.com")
                        time.sleep(2)

                        assert "Gmail" in driver.title, "Arrived at the login page."
                        
                        time.sleep(2)
                        enter_mail = driver.find_element(By.NAME, "identifier")
                        assert enter_mail, "Found the email input."
                        enter_mail.send_keys(username)
                        time.sleep(2)
                        next_passw = driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.qIypjc.TrZEUc.lw1w4b")
                        assert next_passw, "Found the 'Next' button."
                        next_passw.click()
                        time.sleep(2)
                        enter_passw = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
                        assert enter_passw, "Found the password input."
                        time.sleep(2)
                        
                        enter_passw.send_keys(passwrd)
                        time.sleep(1)
                        enter_passw.send_keys(Keys.ENTER)
                        time.sleep(2)

                        open_mail = driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[8]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[4]/div[2]")
                        open_mail.click()
                        time.sleep(2)

                        try:
                            code = driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[1]/table/tbody/tr/td/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/span/span/table[1]/tbody/tr/td/span/span").text
                            assert code, "Got the verification code."
                            time.sleep(2)
                            pyperclip.copy(code)
                            assert pyperclip.paste() == code, "Copied the code."
                            time.sleep(1)
                            driver.switch_to.window(driver.window_handles[0])
                            time.sleep(1)

                            enter_code = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[2]/form/div/div[2]/div[3]/div[1]/input")
                            assert enter_code, "Found the verification code input."
                            enter_code.send_keys(Keys.CONTROL, 'v')
                            time.sleep(2)
                            enter_code.send_keys(Keys.ENTER)
                            time.sleep(2)
                            new_passw = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[2]/form/div/div[2]/div[2]/div[1]/div/input")
                            assert new_passw, "Found the new password input."
                            new_passw.send_keys(custome_pasword_1)
                            new_passw.send_keys(Keys.ENTER)
                            time.sleep(2)
                            assert "password changed" in driver.page_source, "Password changed successfully."
                            result = f" Test #{index}' {test_name}': The password was changed successfully."
                            time.sleep(2)

                        except NoSuchElementException:
                            result = f"\n Test #{index} '{test_name}': Problems with the verification code."
                            
                    except NoSuchElementException:
                        result = f"\n Test #{index} '{test_name}': Problems with Gmail."

                except NoSuchElementException:
                    result = f" Test #{index} '{test_name}': Email wasn't sent."
                    time.sleep(2)

            except NoSuchElementException:
                result = f"Test #{index} '{test_name}': Error during login."

        elif driver.find_element(By.CSS_SELECTOR, ".fsl.fwb.fcb").text != user:
            print("Invalid email")
            result = f" Test #{index}' {test_name}': Invalid username."
        
    except AssertionError as e:
        log_file.write(f"Test #{index} '{test_name}' : {str(e)}\n")
        result = f"Test #{index}' {test_name}': Password change failed."

    finally:
        log_file.write(result + "\n")
        driver.quit()

test_cases = [
    {"username": "ValidEmail@gmail.com", "passwrd": "ValidPassword", "test_name": "Recovery password"},
    {"username": "InvalidEmail@gmail.com", "passwrd": "ValidPassword", "test_name": "Invalid email"},
    {"username": "NoFormat", "passwrd":"ValidPassword", "test_name": "No format"},
    {"username": "ValidEmail@invalid.com", "passwrd": "ValidPassword", "test_name": "Invalid format"}
]

with open(log_file_path, "a") as log_file:
    log_file.write(f"\n\n--- Tested at {current_datetime.strftime('%Y-%m-%d %H:%M:%S')} ---\n\n")
    for index, test_case in enumerate(test_cases, start=1):
        print(f"Test Case #{index}: {test_case['test_name']}")
        forget_psw_test(test_case["username"], test_case["passwrd"], test_case["test_name"], log_file)
        print()
