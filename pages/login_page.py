from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from locators.login_page_locators import LoginPageLocators
from constants import Constants

constants = Constants()


class LoginPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver: WebDriver = driver

    def authorization(self, email: str, password: str):
        self.open_page(constants.LOGIN_URL)
        self.send_keys(locator=LoginPageLocators.INPUT_EMAIL_FIELD, data=email)
        self.send_keys(locator=LoginPageLocators.INPUT_PASSWORD_FIELD, data=password)
        self.click_to_element(locator=LoginPageLocators.BUTTON_LOGIN)
        self.wait_displayed_element(locator=LoginPageLocators.PLACE_ORDER)
