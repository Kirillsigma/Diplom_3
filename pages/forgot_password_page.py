import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators
from helpers.data import DRIVER_NAME

class ForgotPasswordPage(BasePage):

    @allure.step("Пишем в поле для восстановления пароля email")
    def enter_reed_forgot_password_email(self, word):
        self.click_to_element(ForgotPasswordLocators.SEARCH_FIELD_FORGOT_PASSWORD_EMAIL)
        self.add_text(ForgotPasswordLocators.SEARCH_FIELD_FORGOT_PASSWORD_EMAIL, word)


    @allure.step("Кликаем на кнопку восстановить")
    def click_recover_password(self):
        if DRIVER_NAME == 'chrome':
            self.click_to_element(ForgotPasswordLocators.SEARCH_RECOVER_PASSWORD)
            self.enter_password()
        else:
            self.click_to_element(ForgotPasswordLocators.SEARCH_RECOVER_PASSWORD)


    @allure.step("Кликаем на поле куда вводить пароль")
    def enter_password(self):
        self.click_to_element(ForgotPasswordLocators.SEARCH_FIELD_PASSWORD)


    @allure.step("Смотрим ка изменлось поле")
    def password_active(self):
        # search_field = self.find_element(locator=ForgotPasswordLocators.SEARCH_FIELD_PASSWORD_ACTIVE)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ForgotPasswordLocators.SEARCH_FIELD_PASSWORD_ACTIVE)).get_attribute("class")
        return search_field




