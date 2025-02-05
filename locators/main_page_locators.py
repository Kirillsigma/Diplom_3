from selenium.webdriver.common.by import By

class MainPageLocators:

    # Найти кнопку личный кабинет
    SEARCH_PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//*[contains(@class, 'AppHeader_header__linkText') and text() = 'Личный Кабинет']")