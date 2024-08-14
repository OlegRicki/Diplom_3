import allure
from pages.main_page import MainPage
from constants import Constants

constants = Constants()


@allure.epic('Группа тестов на омновной функционал')
class TestBasicFunctionality:
    @allure.title('Тест на открытие страницы конструктора')
    def test_open_construction_tab(self, create_user_and_authorization, driver):
        main_page = MainPage(driver)
        main_page.open_page_order_feed()
        main_page.click_to_constructor_tab()
        main_page.wait_to_element_constructor_tab()
        assert main_page.get_current_url() == constants.BASE_URL + '/'

    @allure.title('Тест на открытие страницы лента заказов')
    def test_open_order_feed_tab(self, create_user_and_authorization, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_to_order_feed_tab()
        main_page.wait_to_element_order_feed_tab()
        assert main_page.get_current_url() == constants.BASE_URL + '/feed'

    @allure.title('Тест на открытие детальной информации об ингредиенте')
    def test_open_window_details_ingredient(self, create_user_and_authorization, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        assert main_page.click_to_ingredient_with_open_modal()

    @allure.title('Тест на закрытие окна детальной информации об ингредиенте')
    def test_close_window_details_ingredient(self, create_user_and_authorization, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_to_ingredient_with_open_modal()
        assert main_page.close_ingredient_info()

    @allure.title('Тест на добавление ингредиента в заказ')
    def test_add_ingredient_in_order(self, create_user_and_authorization, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.add_ingredient_in_order()
        assert main_page.check_counter_has_changed()

    @allure.title('Тест создание заказа')
    def test_place_order(self, create_user_and_authorization, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.place_order()
        assert main_page.check_place_order()

