import pytest

import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.select import Select  # You need to import this for select class

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait


def document_initialised(driver):
    return driver.execute_script("return initialised")

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def pytest_addoption(parser): # This is how you declare a runtime variable
    parser.addoption("--browser_name", action="store", default="chrome") # We are telling our testcase it may need to expect this browser name from our terminal, if we dont, it wont recognise it.


@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("/Users/eubs/Downloads/chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()