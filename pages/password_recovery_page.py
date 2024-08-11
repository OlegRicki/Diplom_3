from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from locators.login_page_locators import LoginPageLocators
from locators.password_recovery_locators import PasswordRecoveryLocators, ResetPasswordLocators
from constants import Constants

constants = Constants()


class PasswordRecoveryPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver: WebDriver = driver

    def open_login_page(self):
        self.open_page(page=constants.LOGIN_URL)

    def open_forgot_password_page(self):
        self.open_page(page=constants.FORGOT_PASSWORD)

    def click_to_link_password_recovery(self):
        self.click_to_element(locator=LoginPageLocators.LINK_PASSWORD_RECOVERY)

    def check_open_page_forgot_password(self):
        self.wait_displayed_element(locator=PasswordRecoveryLocators.TEXT)
        current_url = self.get_current_url()
        return constants.FORGOT_PASSWORD == current_url

    def check_open_page_reset_password(self):
        self.wait_displayed_element(locator=ResetPasswordLocators.INPUT_FIELD_PASSWORD)
        current_url = self.get_current_url()
        return constants.RESET_PASSWORD == current_url

    def entry_field_email(self, email):
        self.send_keys(locator=PasswordRecoveryLocators.INPUT_FIELD_EMAIL, data=email)

    def entry_field_password(self, password):
        self.send_keys(locator=ResetPasswordLocators.INPUT_FIELD_PASSWORD, data=password)

    def click_to_button_active_inactive_field(self):
        self.click_to_element(locator=ResetPasswordLocators.BUTTON_DISPLAYED_PASSWORD)

    def check_active_field_password(self):
        return self.check_displayed_element(locator=ResetPasswordLocators.ENABLED_STATUS_PASSWORD)

    def click_to_button_restore(self):
        self.click_to_element(locator=PasswordRecoveryLocators.BUTTON_RESTORE)
