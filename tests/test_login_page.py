from pages.login_page import LoginPage
from pages.password_reset_page import PasswordResetPage
from pages.user_page import UserPage

link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


def test_sign_up_new_user(browser):
    page = LoginPage(browser, link)
    page.open()
    page.fill_email_registration_field()
    page.fill_password_registration_field()
    page.fill_password_confirmation_field()
    page.submit_new_user()
    user_page = UserPage(browser, browser.current_url)
    user_page.should_be_success_alert()


def test_sign_in_user(browser):
    page = LoginPage(browser, link)
    page.open()
    page.fill_user_email_field()
    page.fill_user_password_field()
    page.submit_enter_user()
    user_page = UserPage(browser, browser.current_url)
    user_page.should_be_success_alert()


def test_recover_password(browser):
    page = LoginPage(browser, link)
    page.open()
    page.recover_password()
    password_reset_page = PasswordResetPage(browser, link)
    password_reset_page.email_field_for_recover()
    password_reset_page.button_for_recover()
    password_reset_page.alert_recover()






