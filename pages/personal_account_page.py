from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from locators.personal_account_locators import PersonalAccountLocators
from constants import Constants

constants = Constants()


class PersonalAccountPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver: WebDriver = driver

    def open_personal_account_page(self):
        self.open_page(page=constants.ACCOUNT_PROFILE)

    def click_to_button_personal_account(self):
        self.click_to_element(locator=PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_displayed_element(locator=PersonalAccountLocators.TEXT)

    def check_url_personal_account(self):
        current_url = self.get_current_url()
        return current_url == constants.ACCOUNT_PROFILE

    def click_button_history(self):
        self.click_to_element(locator=PersonalAccountLocators.HISTORY_ORDERS_BUTTON)

    def check_url_history_orders(self):
        current_url = self.get_current_url()
        return current_url == constants.ORDER_HISTORY

    def log_out(self):
        self.click_to_element(locator=PersonalAccountLocators.BUTTON_LOG_OUT)
        self.wait_displayed_element(locator=PersonalAccountLocators.INPUT_EMAIL_FIELD)

    def check_url_log_out(self):
        current_url = self.get_current_url()
        return current_url == constants.LOGIN_URL
