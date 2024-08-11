import pytest
from pages.main_page import MainPage
from constants import Constants

constants = Constants()


class TestBasicFunctionality:

    def test_open_construction_tab(self, authorization, driver):
        main_page = MainPage(driver)
        main_page.open_page_order_feed()
        main_page.click_to_constructor_tab()
        main_page.wait_to_element_constructor_tab()
        assert main_page.get_current_url() == constants.BASE_URL + '/'

    def test_open_order_feed_tab(self, authorization, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_to_order_feed_tab()
        main_page.wait_to_element_order_feed_tab()
        assert main_page.get_current_url() == constants.BASE_URL + '/feed'

    def test_open_window_details_ingredient(self, authorization, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        assert main_page.click_to_ingredient_with_open_modal()

    def test_close_window_details_ingredient(self, authorization, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_to_ingredient_with_open_modal()
        assert main_page.close_ingredient_info()

    def test_add_ingredient_in_order(self, authorization, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.add_ingredient_in_order()
        assert main_page.check_counter_has_changed()

    def test_place_order(self, authorization, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.place_order()
        assert main_page.check_place_order()
