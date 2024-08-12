from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from constants import Constants

constants = Constants()


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_order_feed(self):
        self.open_page(page=constants.BASE_URL + '/feed')

    def click_to_order(self):
        self.click_to_element(locator=OrderFeedLocators.FIRST_ORDER)

    def check_displayed_order_details(self) -> bool:
        return self.check_displayed_element(locator=OrderFeedLocators.MODAL_WINDOW)

    def check_order_number(self, origin_number: str) -> bool:
        order_number = self.get_text_element(locator=OrderFeedLocators.FIRST_ORDER_NUMBER)
        return origin_number in order_number

    def get_counter_all_time(self) -> str:
        return self.get_text_element(locator=OrderFeedLocators.COUNTER_ALL_TIME)

    def get_counter_today(self) -> str:
        return self.get_text_element(locator=OrderFeedLocators.COUNTER_FOR_TODAY)

    def get_number_order_in_progress(self) -> str:
        self.wait_numbers_to_element(locator=OrderFeedLocators.IN_PROGRESS)
        return self.get_text_element(locator=OrderFeedLocators.IN_PROGRESS)
