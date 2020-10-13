from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.user_page import UserPage

link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/profile/"


def test_open_user_page(browser):
    page = UserPage(browser)
    page.open()
    page.verify_site_name()