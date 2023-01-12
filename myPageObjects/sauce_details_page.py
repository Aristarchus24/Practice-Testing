from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


class sauce_details_page:

    def __init__(self, driver):
        self.driver = driver

    firstname = (By.CSS_SELECTOR,"#first-name")
    secondname = (By.XPATH,"//input[@id='last-name']")
    postcode = (By.XPATH,"//input[@id='postal-code']")
    continuebutton = (By.XPATH,"//input[@id='continue']")

    def getFirstname(self):
        return self.driver.find_element(*sauce_details_page.firstname)

    def getSecondname(self):
        return self.driver.find_element(*sauce_details_page.secondname)

    def getPostcode(self):
        return self.driver.find_element(*sauce_details_page.postcode)

    def getContinuebutton(self):
        return self.driver.find_element(*sauce_details_page.continuebutton)