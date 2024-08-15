import allure
from pages.order_feed_page import OrderFeedPage
from api.api_base import ApiBase


@allure.epic('Группа тестов на раздел "Лента заказов" ')
class TestOrderFeed:
    @allure.title('Тест на открытие детальной информации заказа')
    def test_open_details_order(self, create_user_and_authorization, create_order, driver):
        order_page = OrderFeedPage(driver)
        order_page.open_order_feed()
        order_page.click_to_order()
        assert order_page.check_displayed_order_details()

    @allure.title('Тест на отображение заказа пользователя на странице "Дента заказов"')
    def test_displayed_user_order_inorder_feed(self, create_user_and_authorization, create_order, driver):
        order_page = OrderFeedPage(driver)
        number = create_order
        order_number = '#0' + str(number)
        order_page.open_order_feed()
        assert order_page.check_order_number(origin_number=order_number)

    @allure.title('Тест на увеличение коунтера за все время после создания заказа')
    def test_increase_counter_all_time(self, create_user_and_authorization, driver):
        email, password, access_token = create_user_and_authorization
        order_page = OrderFeedPage(driver)
        api_base = ApiBase()
        order_page.open_order_feed()
        counter_old = order_page.get_counter_all_time()
        api_base.create_order_authorization_user(access_token=access_token)
        order_page.browser_refresh()
        counter_new = order_page.get_counter_all_time()
        assert counter_old < counter_new

    @allure.title('Тест на увеличение коунтера за день, после создания заказа')
    def test_decrease_counter_today(self, create_user_and_authorization, driver):
        email, password, access_token = create_user_and_authorization
        order_page = OrderFeedPage(driver)
        api_base = ApiBase()
        order_page.open_order_feed()
        counter_old = order_page.get_counter_today()
        api_base.create_order_authorization_user(access_token=access_token)
        order_page.browser_refresh()
        counter_new = order_page.get_counter_today()
        assert counter_old < counter_new

    @allure.title('Тест на отображение номера заказа в работе')
    def test_display_order_in_progress(self, create_user_and_authorization, driver):
        api_base = ApiBase()
        order_page = OrderFeedPage(driver)
        order_page.open_order_feed()
        email, password, access_token = create_user_and_authorization
        number_order = api_base.create_order_authorization_user(access_token=access_token)
        number_order = '#0' + str(number_order)
        number_in_progress = order_page.get_number_order_in_progress()
        assert number_order == number_in_progress
