from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


class sauce_success_page:

    def __init__(self, driver):
        self.driver = driver

    finish = (By.XPATH, "//button[@id='finish']")
    success = (By.CSS_SELECTOR,".complete-header")

    def getFinishbutton(self):
        return self.driver.find_element(*sauce_success_page.finish)

    def getSuccessmessage(self):
        return self.driver.find_element(*sauce_success_page.success)