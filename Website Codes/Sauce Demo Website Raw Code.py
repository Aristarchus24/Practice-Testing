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

driver.get("https://www.saucedemo.com/")

#Login Page
driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

#Items Page
driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']").click()
driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-bike-light']").click()
driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-fleece-jacket").click()
driver.find_element(By.CSS_SELECTOR,".shopping_cart_badge").click()
driver.find_element(By.CSS_SELECTOR,"#checkout").click()

#Details Page
driver.find_element(By.CSS_SELECTOR,"#first-name").send_keys("Miserable")
driver.find_element(By.XPATH,"//input[@id='last-name']").send_keys("Teen")
driver.find_element(By.XPATH,"//input[@id='postal-code']").send_keys("se15 4qu")
driver.find_element(By.XPATH,"//input[@id='continue']").click()

#Confirmation Page
checkoutTotal = driver.find_element(By.CSS_SELECTOR,".summary_total_label").text
assert "$114.44" in checkoutTotal
print(checkoutTotal)

#Success Page
driver.find_element(By.XPATH,"//button[@id='finish']").click()
confirmMessage = driver.find_element(By.CSS_SELECTOR,".complete-header").text
assert "THANK YOU FOR YOUR ORDER" in confirmMessage
print(confirmMessage)



