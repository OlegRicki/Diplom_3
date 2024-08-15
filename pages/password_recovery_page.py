import allure

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.password_recovery_locators import PasswordRecoveryLocators
from constants import Constants

constants = Constants()


class PasswordRecoveryPage(BasePage):
    @allure.step('Открыть страницу логина')
    def open_login_page(self):
        self.open_page(page=constants.LOGIN_URL)

    @allure.step('Открыть страницу ввода пароля')
    def open_forgot_password_page(self):
        self.open_page(page=constants.FORGOT_PASSWORD)

    @allure.step('Кликнуть на ссылку восстановления пароля')
    def click_to_link_password_recovery(self):
        self.click_to_element(locator=LoginPageLocators.LINK_PASSWORD_RECOVERY)

    @allure.step('Проверить открытие страницы ввода пароля')
    def check_open_page_forgot_password(self):
        self.get_element(locator=PasswordRecoveryLocators.TEXT)
        current_url = self.get_current_url()
        return constants.FORGOT_PASSWORD == current_url

    @allure.step('Проверить открытие страницы восстановления пароля')
    def check_open_page_reset_password(self):
        self.get_element(locator=PasswordRecoveryLocators.INPUT_FIELD_PASSWORD)
        current_url = self.get_current_url()
        return constants.RESET_PASSWORD == current_url

    @allure.step('Заполнить поле email')
    def entry_field_email(self, email):
        self.send_keys(locator=PasswordRecoveryLocators.INPUT_FIELD_EMAIL, data=email)

    @allure.step('Заполнить поле пароль ')
    def entry_field_password(self, password):
        self.send_keys(locator=PasswordRecoveryLocators.INPUT_FIELD_PASSWORD, data=password)

    @allure.step('Кликнуть на кнопку (отображения/не отображения) пароля ')
    def click_to_button_active_inactive_field(self):
        self.click_to_element(locator=PasswordRecoveryLocators.BUTTON_DISPLAYED_PASSWORD)

    @allure.step('Проверить что пароль отображается')
    def check_active_field_password(self):
        return self.check_displayed_element(locator=PasswordRecoveryLocators.ENABLED_STATUS_PASSWORD)

    @allure.step('Кликнуть на кнопку Восстановить')
    def click_to_button_restore(self):
        self.click_to_element(locator=PasswordRecoveryLocators.BUTTON_RESTORE)
