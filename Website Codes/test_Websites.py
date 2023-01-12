import unittest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.select import Select

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

class JdShoePurchase(unittest.TestCase): # Test case class which is being inherited from the TestCase class, this is the way to tell unittest module that this is a test case
    def test_setUp(self):# Part of initialisation. This method will be called before every test function which I am going to write in this test case class. Here I am creating a chrome webdriver
        service_obj = Service("/Users/eubs/Downloads/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
        def test_JdShoepurchase(): # This is the test case method, it should always start with test_. First line inside this method create a local reference to the driver object created in setUp method.
            driver.get("https://www.google.co.uk/")
            driver.find_element(By.XPATH, "//input[@class='gLFyf gsfi']").send_keys("JD Sports UK")
            driver.find_element(By.XPATH, "//input[@class='gLFyf gsfi']").send_keys(Keys.ENTER)
            driver.find_element(By.XPATH,"(//h3[@class='LC20lb MBeuO DKV0Md'])[1]").click()  # Write the xpath, if there is multiple elements being located, put it in brackets and count from the top of the page which number your one is
            driver.find_element(By.XPATH,"(//button[@class='btn btn-level1 accept-all-cookies'][normalize-space()='Accept All Cookies'])[1]").send_keys(Keys.ENTER)
            action.move_to_element(driver.find_element(By.XPATH,"//a[normalize-space()='Men']")).perform()  # This is how you get the mouse to hover over an element
            WebDriverWait(driver, 20).until(expectedCondition.element_to_be_clickable((By.XPATH,"//a[@href='/men/mens-footwear/trainers/']"))).click()  # To click on the clickable elements you need to induce WebDriverWait for the element to be clickable.
            driver.find_element(By.XPATH,"//body/div[@id='main']/div[@id='productBrowse']/div[@id='productListings']/div[@class='maxWidth']/div[@id='productListRight']/div[@id='productListRightContainer']/ul[@id='productListMain']/li[2]/span[1]/a[1]/picture[1]/img[1]").click()
            driver.find_element(By.CSS_SELECTOR, "button[title='Select Size 9']").click()
            driver.find_element(By.ID, "addToBasket").click()
            basketTotal = driver.find_element(By.CSS_SELECTOR,"div[data-e2e='cart-basketTotals-total']").text
            print(basketTotal)
            assert "£165.00" in basketTotal

class Sauce_Demo_Test(unittest.TestCase):
    def test_SetUp(self):
        service_obj = Service("/Users/eubs/Downloads/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
    def test_SauceDemo(self):
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket").click()
        driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").click()
        driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Miserable")
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Teen")
        driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("se15 4qu")
        driver.find_element(By.XPATH, "//input[@id='continue']").click()
        checkoutTotal = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        assert "$114.44" in checkoutTotal
        print(checkoutTotal)
        driver.find_element(By.XPATH, "//button[@id='finish']").click()
        confirmMessage = driver.find_element(By.CSS_SELECTOR, ".complete-header").text
        assert "THANK YOU FOR YOUR ORDER" in confirmMessage
        print(confirmMessage)









