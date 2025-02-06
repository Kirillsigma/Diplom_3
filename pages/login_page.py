import allure

from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from helpers.data import email, password


@allure.title("Страница входа в аккаунт")
class LoginPage(BasePage):

    @allure.step("Клик по кнопке восстановить аккаунт")
    def click_recowery_password(self):
        self.click_to_element(LoginLocators.SEARCH_RECOVER_PASSWORD)

    @allure.step("Ввод email")
    def entering_a_email(self):
        self.click_to_element(LoginLocators.FIELD_EMAIL)
        self.add_text(LoginLocators.FIELD_EMAIL, email)

    @allure.step("Ввод пароля")
    def entering_a_password(self):
        self.click_to_element(LoginLocators.FIELD_PASSWORD)
        self.add_text(LoginLocators.FIELD_PASSWORD, password)

    @allure.step("Клик по кнопке ВОЙТИ")
    def click_button_entrance(self):
        self.click_to_element(LoginLocators.BUTTON_ENTER)

    @allure.step("Клик по кнопке КОНСТРУКТОР")
    def click_button_designer(self):
        self.click_to_element(LoginLocators.BUTTON_DESIGNER)

    @allure.step("Ожидание когда появится кнопка войти в аккаунт/оформить заказ")
    def without_element_order(self):
        self.without_element_located(LoginLocators.BUTTON_DESIGNER)

    @allure.step("Клик по кнопке исторяи заказов")
    def click_history_order(self):
        self.click_to_element(LoginLocators.HISTORY_ORDER)

    @allure.step("Клик по кнопке Выход")
    def click_exir_account(self):
        self.click_to_element(LoginLocators.EXIT_ACCOUNT)

    @allure.step("Ожидание когда появится кнопка войти")
    def without_element_entrance(self):
        self.without_element_located(LoginLocators.BUTTON_ENTER)






