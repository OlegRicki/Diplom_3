import time

import pytest
from pages.password_recovery_page import PasswordRecoveryPage
from constants import Constants

constants = Constants()


class TestPasswordRecovery:

    def test_open_page_password_recovery(self, driver):
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.open_login_page()
        recovery_page.click_to_link_password_recovery()
        assert recovery_page.check_open_page_forgot_password()

    def test_entry_email_and_click_button_recovery(self, driver):
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.open_forgot_password_page()
        recovery_page.entry_field_email(email=constants.EMAIL)
        recovery_page.click_to_button_restore()
        assert recovery_page.check_open_page_reset_password()

    def test_make_field_password_active(self, driver):
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.open_forgot_password_page()
        recovery_page.entry_field_email(email=constants.EMAIL)
        recovery_page.click_to_button_restore()
        recovery_page.entry_field_password(password=constants.TEST_PASSWORD)
        recovery_page.click_to_button_active_inactive_field()
        assert recovery_page.check_active_field_password()

