import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from tests.conftest import driver


class MainPage(BasePage):

    @allure.step("Клик по кнопке личный кабинет")
    def click_personal_account(self):
        self.click_to_element(MainPageLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON)
