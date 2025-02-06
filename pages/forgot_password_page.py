import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators


@allure.title("Страница восстановленя пароля")
class ForgotPasswordPage(BasePage):

    @allure.step("Пишем в поле для восстановления пароля email")
    def enter_reed_forgot_password_email(self, word):
        self.click_to_element(ForgotPasswordLocators.SEARCH_FIELD_FORGOT_PASSWORD_EMAIL)
        self.add_text(ForgotPasswordLocators.SEARCH_FIELD_FORGOT_PASSWORD_EMAIL, word)

    @allure.step("Кликаем на кнопку восстановить")
    def click_recover_password(self):
       self.click_to_element(ForgotPasswordLocators.SEARCH_RECOVER_PASSWORD)

    @allure.step("Ожидание когда появится поле куда вводить пароль")
    def without_element(self):
        self.without_element_located(ForgotPasswordLocators.SEARCH_FIELD_PASSWORD)

    @allure.step("Кликаем на поле куда вводить пароль")
    def enter_password(self):
        self.click_to_element(ForgotPasswordLocators.SEARCH_FIELD_PASSWORD)

    @allure.step("Ожидание что поле стало активным")
    def without_element_password(self):
        self.driver.find_element(By.XPATH, "//div[contains(@class, 'input pr-6 pl-6 input_type_password input_size_default')]")

    @allure.step("Получаем родительский класс поля с паролем")
    def get_parent_class_password_field(self):
        return self.find_element_with(ForgotPasswordLocators.PASSWORD_FIELD_PARENT)

    @allure.step("Присваиваем переменной родительский класс поля Пароль")
    def assign_parent_class_password_by_variable(self):
        return self.find_element_with(ForgotPasswordLocators.HIGHLIGHTED_PASSWORD_FIELD)






