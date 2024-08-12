import allure
from pages.personal_account_page import PersonalAccountPage


@allure.epic('Группа тестов на страницу персональных данных')
class TestPersonalAccount:
    @allure.title('Тест на открытие страницы персональных данных')
    def test_open_personal_account_page(self, create_user_and_authorization, driver):
        personal_acc_page = PersonalAccountPage(driver)
        personal_acc_page.click_to_button_personal_account()
        assert personal_acc_page.check_url_personal_account()

    @allure.title('Тест на открытие истории заказов')
    def test_open_history_orders_page(self, create_user_and_authorization, driver):
        personal_acc_page = PersonalAccountPage(driver)
        personal_acc_page.open_personal_account_page()
        personal_acc_page.click_button_history()
        assert personal_acc_page.check_url_history_orders()

    @allure.title('Тест на выход')
    def test_log_out(self, create_user_and_authorization, driver):
        personal_acc_page = PersonalAccountPage(driver)
        personal_acc_page.open_personal_account_page()
        personal_acc_page.log_out()
        assert personal_acc_page.check_url_log_out()
