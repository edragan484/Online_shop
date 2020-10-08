import time

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.user_page import UserPage


def test_guest_verify_site_name(browser):
    page = MainPage(browser)
    page.open()
    page.verify_site_name()
    page.verify_site_subname()


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser)
    login_page.check_login_page()


def test_verify_guest_see_login_link(browser):
    page = MainPage(browser)
    page.open()
    page.verify_login_link()


def test_guest_check_change_languages(browser):
    page = MainPage(browser)
    page.open()
    page.change_language_to_it()
    page.verify_menu_and_basket_text_in_it()
    page.change_language_to_deutsch()
    page.verify_menu_and_basket_text_in_deutsch()


# Ispraviti
def test_verify_search_item(browser):
    page = MainPage(browser)
    page.open()
    page.searching_item()
    page.verify_search_items_is_correct()


def test_verify_welcome_block(browser):
    page = MainPage(browser)
    page.open()
    page.verify_welcome_block()


def test_verify_recommended_reading_block(browser):
    page = MainPage(browser)
    page.open()
    page.verify_recommended_reading_block()


def test_verify_other_books_block(browser):
    page = MainPage(browser)
    page.open()
    page.verify_other_good_books_block()


def test_add_item_to_basket(browser):
    page = MainPage(browser)
    page.open()
    page.add_to_basket_from_main_page()


def test_verify_alerts_of_add_item_to_basket(browser):
    page = MainPage(browser)
    page.open()
    page.add_to_basket_from_main_page()
    page.verify_alert_of_add_item_to_basket()
    page.verify_alert_of_offer()
    page.verify_alert_basket_total()


def test_verify_basket_and_checkout_buttons_in_alert(browser):
    page = MainPage(browser)
    page.open()
    page.add_to_basket_from_main_page()
    page.verify_alert_basket_total()
    page.verify_view_basket_button_in_alert()
    page.verify_checkout_in_alert()


def test_go_to_basket_from_add_item_alert(browser):
    page = MainPage(browser)
    page.open()
    page.add_to_basket_from_main_page()
    page.verify_alert_basket_total()
    page.go_to_basket_from_alert()


def test_go_to_checkout_from_add_item_alert(browser):
    page = MainPage(browser)
    page.open()
    page.add_to_basket_from_main_page()
    page.verify_alert_basket_total()
    page.go_to_checkout_from_alert()


