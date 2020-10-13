from pages.login_page import LoginPage
from pages.password_reset_page import PasswordResetPage
from pages.main_page import MainPage


class TestLoginPage:
    def test_sign_up_new_user(self, browser):
        page = LoginPage(browser)
        page.open()
        page.fill_email_registration_field()
        page.fill_password_registration_field()
        page.fill_password_confirmation_field()
        page.submit_new_user()
        main_page = MainPage(browser)
        main_page.verify_welcome_success_alert()

    def test_sign_in_user(self, browser):
        page = LoginPage(browser)
        page.open()
        page.fill_user_email_field()
        page.fill_user_password_field()
        page.submit_enter_user()
        main_page = MainPage(browser)
        main_page.verify_welcome_success_alert()

    def test_recover_password(self, browser):
        page = LoginPage(browser)
        page.open()
        page.recover_password()
        password_reset_page = PasswordResetPage(browser)
        password_reset_page.email_field_for_recover()
        password_reset_page.button_for_recover()
        password_reset_page.alert_recover()
