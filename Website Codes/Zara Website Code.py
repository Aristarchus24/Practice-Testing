from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.select import Select

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

import time

from selenium.webdriver.common.by import By

service_obj = Service("/Users/eubs/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(7)
driver.maximize_window()
action = ActionChains(driver)
expectedCondition = EC
chromeOptions = Options

driver.get("https://www.zara.com/")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"//button[@aria-label='Open menu']//*[name()='svg']").click()
driver.find_element(By.XPATH,"//span[@class='layout-categories-category__name'][normalize-space()='MAN']").click
time.sleep(6)
driver.find_element(By.XPATH,"//li[@class='layout-categories-category layout-categories-category--is-highlighted layout-categories-category--level-2']//span[@class='layout-categories-category__name'][normalize-space()='NEW']").click()





