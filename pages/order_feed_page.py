import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from constants import Constants

constants = Constants()


class OrderFeedPage(BasePage):
    @allure.step('Открыть страницу "Лента заказов"')
    def open_order_feed(self):
        self.open_page(page=constants.BASE_URL + '/feed')

    @allure.step('Кликнуть на первый заказ ')
    def click_to_order(self):
        self.click_to_element(locator=OrderFeedLocators.FIRST_ORDER)

    @allure.step('Проверить отоображение деталей заказа')
    def check_displayed_order_details(self) -> bool:
        return self.check_displayed_element(locator=OrderFeedLocators.MODAL_WINDOW)
    @allure.step('Проверить номер заказа')
    def check_order_number(self, origin_number: str) -> bool:
        order_number = self.get_element(locator=OrderFeedLocators.FIRST_ORDER_NUMBER).text

        return origin_number in order_number

    @allure.step('Получить номер за все время')
    def get_counter_all_time(self) -> str:
        return self.get_element(locator=OrderFeedLocators.COUNTER_ALL_TIME).text

    @allure.step('Получить номер за день ')
    def get_counter_today(self) -> str:
        return self.get_element(locator=OrderFeedLocators.COUNTER_FOR_TODAY).text

    @allure.step('Получить номер заказа в работе')
    def get_number_order_in_progress(self) -> str:
        self.wait_numbers_to_element(locator=OrderFeedLocators.IN_PROGRESS)
        return self.get_element(locator=OrderFeedLocators.IN_PROGRESS).text
