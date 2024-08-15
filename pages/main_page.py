import allure
from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from locators.main_page_locators import MainPageLocators
from constants import Constants

constants = Constants()


class MainPage(BasePage):
    @allure.step('Открыть страницу лента заказа')
    def open_page_order_feed(self):
        self.open_page(page=constants.BASE_URL + '/feed')

    @allure.step('Открыть главную странцу')
    def open_main_page(self):
        self.open_page(page=constants.BASE_URL)

    @allure.step('Кликнуть на вкладку "Конструктор"')
    def click_to_constructor_tab(self):
        self.click_to_element(locator=MainPageLocators.CONSTRUCTOR_TAB)

    @allure.step('Дождаться отображения вкладки конструктор')
    def wait_to_element_constructor_tab(self):
        self.get_element(locator=MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Проверить урл страницы "Конструктор"')
    def check_url_constructor_tab(self) -> str:
        return self.get_current_url()

    @allure.step('Кликнуть на вкладку "Лента заказов"')
    def click_to_order_feed_tab(self):
        self.click_to_element(locator=MainPageLocators.ORDER_FEED_TAB)

    @allure.step('Дождаться отображения вкладки "Лента заказов"')
    def wait_to_element_order_feed_tab(self):
        self.get_element(locator=MainPageLocators.TEXT_ORDER_FEED)

    @allure.step('Кликнуть на ингридиент')
    def click_to_ingredient_with_open_modal(self) -> bool:
        self.click_to_element(locator=MainPageLocators.BUN_IMG)
        return self.check_displayed_element(locator=MainPageLocators.MODAL_WINDOW)
    @allure.step('Закрыть окно детальной информации ингридиента')
    def close_ingredient_info(self):
        self.click_to_element(locator=MainPageLocators.BUTTON_CLOSE_MODAL)
        return self.check_not_displayed_element(locator=MainPageLocators.MODAL_WINDOW)

    @allure.step('Добавить ингридиент в заказ')
    def add_ingredient_in_order(self):
        first_element = self.get_element(locator=MainPageLocators.BUN_IMG)
        target_element = self.get_element(locator=MainPageLocators.DRAG__INGREDIENT)
        self.drag_and_drop_element(source_element=first_element, target_element=target_element)

    @allure.step('Проверить кол-во ингридиента')
    def check_counter_has_changed(self):
        return self.get_element(locator=MainPageLocators.ONE_COUNTER).text != 0
    @allure.step('Кликнуть на кнопку "Оформить заказ"')
    def place_order(self):
        self.click_to_element(locator=MainPageLocators.PLACE_ORDER_BUTTON)
        return self.check_displayed_element(locator=MainPageLocators.MODAL_WINDOW)

    @allure.step('Проверить отображения модального окна после оформления заказа')
    def check_place_order(self):
        return self.check_displayed_element(locator=MainPageLocators.MODAL_WINDOW)
