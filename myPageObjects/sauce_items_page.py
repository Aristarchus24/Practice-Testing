from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

class sauce_item_page:

    def __init__(self,driver):
        self.driver = driver

    backpack = (By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
    bikelight = (By.XPATH,"//button[@id='add-to-cart-sauce-labs-bike-light']")
    tshirt = (By.XPATH,"//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    fleecejacket = (By.CSS_SELECTOR,"#add-to-cart-sauce-labs-fleece-jacket")
    shoppingcartbadge = (By.CSS_SELECTOR,".shopping_cart_badge")
    checkoutbutton = (By.CSS_SELECTOR,"#checkout")

    def getBackpack(self):
        return self.driver.find_element(*sauce_item_page.backpack)

    def getBikelight(self):
        return self.driver.find_element(*sauce_item_page.bikelight)

    def getTshirt(self):
        return self.driver.find_element(*sauce_item_page.tshirt)

    def getFleecejacket(self):
        return self.driver.find_element(*sauce_item_page.fleecejacket)

    def getShoppingcartbadge(self):
        return self.driver.find_element(*sauce_item_page.shoppingcartbadge)

    def getCheckoutbutton(self):
        return self.driver.find_element(*sauce_item_page.checkoutbutton)
