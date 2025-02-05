import pytest
from selenium import webdriver
from helpers.data import DRIVER_NAME

@pytest.fixture(params=['chrome','firefox'])
def driver(request):
    if request.param == "chrome":
        DRIVER_NAME = 'chrome'
        driver = webdriver.Chrome()
    else:
        DRIVER_NAME = 'firefox'
        driver = webdriver.Firefox()
    yield driver
    driver.quit()