from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

class sauce_login_page:

    def __init__(self,driver):
        self.driver = driver

    username = (By.XPATH,"//input[@id='user-name']")
    password = (By.CSS_SELECTOR,"#password")
    login1 = (By.ID,"login-button")

    def getUsername(self):
        return self.driver.find_element(*sauce_login_page.username)

    def getPassword(self):
        return self.driver.find_element(*sauce_login_page.password)

    def getLogin(self):
        return self.driver.find_element(*sauce_login_page.login1)


