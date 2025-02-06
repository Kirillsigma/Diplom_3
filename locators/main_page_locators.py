from selenium.webdriver.common.by import By

class MainPageLocators:

    # Найти кнопку личный кабинет
    SEARCH_PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//*[contains(@class, 'AppHeader_header__link__3D_hX') and contains(@href, '/account')]")

    # Найти кнопку Оформить заказ/войти в аккаунт
    BUTTON_PLACE_ORDER =  (By.XPATH, "//*[contains(@class, 'button_button__33qZ0')]")

    # Найти кнопку Оформить заказт
    BUTTON_DESIGNER = (By.XPATH, "//*[contains(@class,'button_button__33qZ0') and text() = 'Оформить заказ']")