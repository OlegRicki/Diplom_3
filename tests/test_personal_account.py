from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:
    def test_open_personal_account_page(self, authorization, driver):
        personal_acc_page = PersonalAccountPage(driver)
        personal_acc_page.click_to_button_personal_account()
        assert personal_acc_page.check_url_personal_account()

    def test_open_history_orders_page(self, authorization, driver):
        personal_acc_page = PersonalAccountPage(driver)
        personal_acc_page.open_personal_account_page()
        personal_acc_page.click_button_history()
        assert personal_acc_page.check_url_history_orders()

    def test_log_out(self, authorization, driver):
        personal_acc_page = PersonalAccountPage(driver)
        personal_acc_page.open_personal_account_page()
        personal_acc_page.log_out()
        assert personal_acc_page.check_url_log_out()



