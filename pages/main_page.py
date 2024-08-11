from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from locators.main_page_locators import MainPageLocators
from constants import Constants

constants = Constants()


class MainPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver: WebDriver = driver

    def open_page_order_feed(self):
        self.open_page(page=constants.BASE_URL + '/feed')

    def open_main_page(self):
        self.open_page(page=constants.BASE_URL)

    def click_to_constructor_tab(self):
        self.click_to_element(locator=MainPageLocators.CONSTRUCTOR_TAB)

    def wait_to_element_constructor_tab(self):
        self.wait_displayed_element(locator=MainPageLocators.PLACE_ORDER_BUTTON)

    def check_url_constructor_tab(self) -> str:
        return self.get_current_url()

    def click_to_order_feed_tab(self):
        self.click_to_element(locator=MainPageLocators.ORDER_FEED_TAB)

    def wait_to_element_order_feed_tab(self):
        self.wait_displayed_element(locator=MainPageLocators.TEXT_ORDER_FEED)

    def click_to_ingredient_with_open_modal(self) -> bool:
        self.click_to_element(locator=MainPageLocators.BUN_IMG)
        return self.check_displayed_element(locator=MainPageLocators.MODAL_WINDOW)

    def close_ingredient_info(self):
        self.click_to_element(locator=MainPageLocators.BUTTON_CLOSE_MODAL)
        return self.check_not_displayed_element(locator=MainPageLocators.MODAL_WINDOW)

    def add_ingredient_in_order(self):
        first_element = self.get_element(locator=MainPageLocators.BUN_IMG)
        target_element = self.get_element(locator=MainPageLocators.DRAG__INGREDIENT)
        self.drag_and_drop_element(source_element=first_element, target_element=target_element)

    def check_counter_has_changed(self):
        return self.get_text_element(locator=MainPageLocators.ONE_COUNTER) != 0

    def place_order(self):
        self.click_to_element(locator=MainPageLocators.PLACE_ORDER_BUTTON)
        return self.check_displayed_element(locator=MainPageLocators.MODAL_WINDOW)

    def check_place_order(self):
        return self.check_displayed_element(locator=MainPageLocators.MODAL_WINDOW)
