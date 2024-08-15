from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    TEXT = (By.XPATH, '//h2[text()="Восстановление пароля"]')
    INPUT_FIELD_EMAIL = (By.XPATH, '//input[@name="name"]')

    BUTTON_RESTORE = (By.XPATH, '//button[text()="Восстановить"]')
    INPUT_FIELD_PASSWORD = (By.XPATH, '//input[@type="password"]')
    BUTTON_DISPLAYED_PASSWORD = (By.XPATH, '//div[contains(@class, "input__icon ")]')
    DISABLED_STATUS_PASSWORD = (By.XPATH, '//div[contains(@class, " input_status_error")]')
    ENABLED_STATUS_PASSWORD = (By.XPATH, '//div[contains(@class, " input_status_active")]')


class ResetPasswordLocators:
    INPUT_FIELD_PASSWORD = (By.XPATH, '//input[@type="password"]')
    BUTTON_DISPLAYED_PASSWORD = (By.XPATH, '//div[contains(@class, "input__icon ")]')
    DISABLED_STATUS_PASSWORD = (By.XPATH, '//div[contains(@class, " input_status_error")]')
    ENABLED_STATUS_PASSWORD = (By.XPATH, '//div[contains(@class, " input_status_active")]')
