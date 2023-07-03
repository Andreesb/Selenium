from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import unittest

class probando_unittest(unittest.TestCase):

    driver = None
    driver = webdriver.Chrome() #Find driver

    def test_facebook(self):
        self.driver.get("https://www.facebook.com/") #To open Facebook
        time.sleep(3)

    def test_login(self):
    
        user = self.driver.find_element(By.ID, "email") #To find the email input
        user.send_keys("test@gmail.com") #Enter an email
        password = self.driver.find_element(By.ID, "pass") #To find the password input
        password.send_keys("testtest") #Enter a password
        password.submit() #Press enter
        time.sleep(3)

    #Find the messenger button to verify the successfully login
        try:
            self.driver.find_element(By.XPATH, "//body/div[@id='mount_0_0_q/']/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/span[1]/span[1]/div[1]/div[1]/*[1]")
            print("Successfully login")

        except NoSuchElementException:
            print("Something went wrong")

if __name__ == "__main__":
    unittest.main()