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

driver.get("https://www.google.co.uk/")
driver.find_element(By.XPATH,"//input[@title='Search']").send_keys("JD Sports UK")
driver.find_element(By.XPATH,"//input[@title='Search']").send_keys(Keys.ENTER)
driver.find_element(By.XPATH,"(//h3[@class='LC20lb MBeuO DKV0Md'])[1]").click() # Write the xpath, if there is multiple elements being located, put it in brackets and count from the top of the page which number your one is
driver.find_element(By.XPATH,"(//button[@class='btn btn-level1 accept-all-cookies'][normalize-space()='Accept All Cookies'])[1]").send_keys(Keys.ENTER)
action.move_to_element(driver.find_element(By.XPATH,"//a[normalize-space()='Men']")).perform() # This is how you get the mouse to hover over an element
WebDriverWait(driver,20).until(expectedCondition.element_to_be_clickable((By.XPATH,"//a[@href='/men/mens-footwear/trainers/']"))).click() # To click on the clickable elements you need to induce WebDriverWait for the element to be clickable.
#driver.execute_script("window.scrollTo(0, 100") # This is how you scroll on a webpage
#time.sleep(60)
driver.find_element(By.XPATH,"//body/div[@id='main']/div[@id='productBrowse']/div[@id='productListings']/div[@class='maxWidth']/div[@id='productListRight']/div[@id='productListRightContainer']/ul[@id='productListMain']/li[2]/span[1]/a[1]/picture[1]/img[1]").click()
driver.find_element(By.CSS_SELECTOR,"button[title='Select Size 9']").click()
driver.find_element(By.ID,"addToBasket").click()
basketTotal = driver.find_element(By.CSS_SELECTOR,"div[data-e2e='cart-basketTotals-total']").text
print(basketTotal)
assert "£165.00" in basketTotal

# This website is weird, sometimes when we run the test, it takes us to the pick location website, sometimes when we run the test it goes straight through




