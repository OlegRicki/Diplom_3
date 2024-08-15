from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    TEXT = (By.XPATH, '//a[text()="Профиль"]')
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')
    HISTORY_ORDERS_BUTTON = (By.XPATH, '//a[text()="История заказов"]')
    EXIT_BUTTON = (By.XPATH, '//button[text()="Выход"]')
    BUTTON_LOG_OUT = (By.XPATH, '//button[text()="Выход"]')
    INPUT_EMAIL_FIELD = (By.XPATH, '(//input[contains(@class, "text input")])[1]')
    NAME_FIRST_ORDER = (By.XPATH, '(//a[contains('
                                  '@class, "OrderHistory_link__1iNby")])[1]//h2[contains(@class, "text ")]')

