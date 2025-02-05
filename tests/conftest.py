import pytest
from selenium import webdriver
from helpers.data import DRIVER_NAME

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()