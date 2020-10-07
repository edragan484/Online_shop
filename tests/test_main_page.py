from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.user_page import UserPage


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser.current_url)
    login_page.check_login_page()


def test_verify_guest_see_login_link(browser):
    page = MainPage(browser)
    page.open()
    page.verify_login_link()


def test_check_change_languages(browser):
    page = MainPage(browser)
    page.open()
    page.change_language()
    page.verify_menu_and_basket_text()



