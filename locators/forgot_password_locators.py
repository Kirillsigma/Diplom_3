from selenium.webdriver.common.by import By

class ForgotPasswordLocators:

    # Найти поле куда вводить email
    SEARCH_FIELD_FORGOT_PASSWORD_EMAIL = (By.XPATH, ".//input[contains(@name,'name')]")

    # Найти кнопку восстановить
    SEARCH_RECOVER_PASSWORD = (By.XPATH, ".//*[text()='Восстановить']")

    # Найти поле куда вводить пароль для восстановления
    SEARCH_FIELD_PASSWORD = (By.XPATH, ".//div[contains(@class,'input__icon input__icon-action')]")

    # Найти поле куда вводить пароль для восстановления (активное)
    SEARCH_FIELD_PASSWORD_ACTIVE = (
    By.XPATH, "//div[contains(@class, 'input pr-6 pl-6 input_type_password input_size_default input_status_active')]")