from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


class sauce_confirm_page:

    def __init__(self, driver):
        self.driver = driver

    checkouttotal = (By.CSS_SELECTOR,".summary_total_label")

    def getCheckouttotal(self):
        return self.driver.find_element(*sauce_confirm_page.checkouttotal)