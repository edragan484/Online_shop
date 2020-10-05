from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.user_page import UserPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_check_change_languages(browser):
    page = MainPage(browser, link)
    page.open()
    page.change_language_to_italian()
    page.change_language_to_deutsch()
