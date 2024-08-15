import allure

from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from locators.personal_account_locators import PersonalAccountLocators
from constants import Constants

constants = Constants()


class PersonalAccountPage(BasePage):
    @allure.step('Открыть страницу Личный кабинет"')
    def open_personal_account_page(self):
        self.open_page(page=constants.ACCOUNT_PROFILE)

    @allure.step('Кликнуть на кнопку "Личный кабинет"')
    def click_to_button_personal_account(self):
        self.click_to_element(locator=PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)
        self.get_element(locator=PersonalAccountLocators.TEXT)

    @allure.step('Проверить урл страницы "Личный кабинет"')
    def check_url_personal_account(self):
        current_url = self.get_current_url()
        return current_url == constants.ACCOUNT_PROFILE

    @allure.step('Кликнуть на кнопку "История"')
    def click_button_history(self):
        self.click_to_element(locator=PersonalAccountLocators.HISTORY_ORDERS_BUTTON)

    @allure.step('Проверить урл Страницы "История"')
    def check_url_history_orders(self):
        current_url = self.get_current_url()
        return current_url == constants.ORDER_HISTORY

    @allure.step('Выйти из аккаунта')
    def log_out(self):
        self.click_to_element(locator=PersonalAccountLocators.BUTTON_LOG_OUT)
        self.get_element(locator=PersonalAccountLocators.INPUT_EMAIL_FIELD)

    @allure.step('Проверить что выход из аккаунта')
    def check_url_log_out(self):
        current_url = self.get_current_url()
        return current_url == constants.LOGIN_URL
