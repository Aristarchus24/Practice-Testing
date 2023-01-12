import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from myPageObjects.sauce_login_page import sauce_login_page
from myPageObjects.sauce_items_page import sauce_item_page
from myPageObjects.sauce_details_page import sauce_details_page
from myPageObjects.sauce_confirm_page import sauce_confirm_page
from myPageObjects.sauce_success_page import sauce_success_page
from ownUtilities.Sauce_Base_Class import sauce_base_class



class sauce_test_one(sauce_base_class):

    def test_saucee2e(self):
        sauceLogin = sauce_login_page(self.driver)
        # Type in your username in the username box
        sauceLogin.getUsername().send_keys("standard_user")
        # Type in your password in your password box
        sauceLogin.getPassword().send_keys("secret_sauce")
        # Click the login button
        sauceLogin.getLogin().click()
        sauceItems = sauce_item_page(self.driver)
        # Click the Backpack to add to the cart
        sauceItems.getBackpack().click()
        # Click the Bikelight to add to the cart
        sauceItems.getBikelight().click()
        # Click on the T shirt to add to the cart
        sauceItems.getTshirt().click()
        # Click on the Jacket and add to the cart
        sauceItems.getFleecejacket().click()
        # Click on the shopping cart badge at the top of the page
        sauceItems.getShoppingcartbadge().click()
        # Click the checkout button
        sauceItems.getCheckoutbutton().click()
        sauceDetails = sauce_details_page(self.driver)
        # Make sure the next page has loaded
        self.wait4connection()
        # Type in the first name in the first name box
        sauceDetails.getFirstname().send_keys("Miserable")
        # Type in the second name in the second name box
        sauceDetails.getSecondname().send_keys("Teen")
        # Type in your postcode in the postcode
        sauceDetails.getPostcode().send_keys("se15 4qu")
        # Click continue
        SauceDetailsPage.getContinuebutton().click()
        sauceConfirm = sauce_confirm_page(self.driver)
        # Make sure the price of the items are correct
        correctprice = sauceConfirm.getCheckouttotal().text
        assert "$144.44" in correctprice
        print(correctprice)
        sauceSuccess = sauce_success_page(self.driver)
        # Click the finish button
        sauceSuccess.getFinishbutton().click()
        # Check that the successful order message has appeared
        passedtest = sauceSuccess.getSuccessmessage().text
        assert "THANK YOU FOR YOUR ORDER" in passedtest
        print(passedtest)




