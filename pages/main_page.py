import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


@allure.title("Главная страница")
class MainPage(BasePage):

    @allure.step("Клик по кнопке личный кабинет")
    def click_personal_account(self):
        self.click_to_element(MainPageLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Прочитать что написано на кнопке на главном экране")
    def button_place(self):
        return self.text_button(MainPageLocators.BUTTON_PLACE_ORDER)

    @allure.step("оЖИДАНИЕ ПОКА КНОПКА ЛИЧНЫЙ АККАУНТ НЕ СТАНЕТ КЛИКАБЕЛЬНОЙ")
    def without_button_clickable(self):
        return self.without_element_clickable(MainPageLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON)