
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from helpers.url import *


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = BASE_URL

    # Зайти на сайт
    def go_to_site(self):
        self.driver.get(self.url)


    def find_element_with(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))

    # Найти элемент
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # Клик по элемменту
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    # Достать url
    def current_url(self):
        return self.driver.current_url

    # Ввести текст
    def add_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    # Ожилание пока не появится элемент
    def without_element_located(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))


    def without_element_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    # Прочитать текст на элементе
    def text_button(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator)).text




