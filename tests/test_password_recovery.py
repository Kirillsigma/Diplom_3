import allure

from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage

from helpers.url import *

@allure.story('Восстановление пароля')
class TestPasswordRecovery:

    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_recovery_password(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_personal_account()
        LoginPage(driver).click_recowery_password()
        assert main_page.current_url() == f'{BASE_URL}{RECOVERY_PASSWORD}'

    @allure.title('ввод почты и клик по кнопке «Восстановить»')
    def test_input_email(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_personal_account()
        LoginPage(driver).click_recowery_password()
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.enter_reed_forgot_password_email('zcx')
        forgot_password.click_recover_password()
        url = forgot_password.current_url()
        assert url == f'{BASE_URL}{RESET_PASSWORD}'


    @allure.title('Cмотрим чтобы подсвечивалось поле куда вводить пароль')
    def test_input_password(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_personal_account()
        LoginPage(driver).click_recowery_password()
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.enter_reed_forgot_password_email('sgdsr465432365gdsgfb@mail.com')
        forgot_password.click_recover_password()
        forgot_password.enter_password()
        assert 'status_active' in forgot_password.password_active()