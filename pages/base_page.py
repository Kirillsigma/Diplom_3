from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from setuptools.archive_util import extraction_drivers

from helpers.url import *

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = BASE_URL

    def go_to_site(self):
        self.driver.get(self.url)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def current_url(self):
        return self.driver.current_url

    def add_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def time_sleep(self):
        self.driver.implicitly_wait(10)

