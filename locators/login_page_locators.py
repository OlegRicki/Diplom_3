from selenium.webdriver.common.by import By


class LoginPageLocators:
    LINK_PASSWORD_RECOVERY = (By.XPATH, '//a[text()="Восстановить пароль"]')
    INPUT_EMAIL_FIELD = (By.XPATH, '(//input[contains(@class, "text input")])[1]')
    INPUT_PASSWORD_FIELD = (By.XPATH, '(//input[contains(@class, "text input")])[2]')
    BUTTON_LOGIN = (By.XPATH, '//button[text()="Войти"]')
    PLACE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')
