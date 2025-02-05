import allure

from pages.base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):

    @allure.step("Клик по кнопке восстановить аккаунт")
    def click_recowery_password(self):
        self.click_to_element(LoginLocators.SEARCH_RECOVER_PASSWORD)

