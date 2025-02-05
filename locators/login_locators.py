from selenium.webdriver.common.by import By

class LoginLocators:

    # Найти кнопку восстановить пароль
    SEARCH_RECOVER_PASSWORD = (By.XPATH, ".//a[contains(text(), 'Восстановить пароль')]")