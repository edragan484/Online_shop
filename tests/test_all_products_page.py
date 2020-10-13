import time
import pytest

from pages.all_products_page2 import AllProductsPage2
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.all_products_page import AllProductsPage


@pytest.mark.regress
class TestAllProductsPageForGuest:
    product_item1 = "Coders at Work"
    menu_it = "Naviga nel negozio"
    basket_it = "Visualizza carrello"

    def test_verify_name_page(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.verify_page_name()

    def test_verify_page_structure(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.verify_menu_block()
        page.verify_product_block()

    def test_verify_menu(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.verify_menu_block()
        page.verify_menu_clothing_link()
        page.verify_menu_books_link()
        page.verify_menu_fiction()
        page.verify_menu_computers()
        page.verify_menu_non_fiction()
        page.verify_menu_programming()
        page.verify_menu_hacking()

    def test_verify_item_link(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.browser.execute_script("window.scrollBy(0, 200);")
        time.sleep(5)
        page.verify_item_link(TestAllProductsPageForGuest.product_item1)

    def test_press_item_link(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.browser.execute_script("window.scrollBy(0, 200);")
        page.press_item_link()

    def test_press_item_image(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.browser.execute_script("window.scrollBy(0, 200);")
        page.press_item_image()

    def test_guest_can_go_to_login(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.verify_login_link()
        page.press_login_link()
        login_page = LoginPage(browser)
        login_page.open()

    def test_change_language(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.change_language_to_it()
        page.verify_change_language_to_it(TestAllProductsPageForGuest.menu_it,
                                          TestAllProductsPageForGuest.basket_it)

    def test_verify_next_button(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.verify_next_button()

    def test_go_to_next_page_and_back(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.press_next_button()
        next_page = AllProductsPage2(browser)
        next_page.verify_page_name()
        next_page.verify_next_page()
        next_page.verify_previous_button()
        next_page.press_previous_button()
        page = AllProductsPage(browser)
        page.open()

    def test_press_add_to_basket_button(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.add_to_basket_button()

    def test_verify_alerts_of_add_to_basket(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.add_to_basket_button()
        page.verify_alert1_of_add_to_basket()
        page.verify_alert2_of_add_to_basket()
        page.verify_alert3_of_add_to_basket()

    def test_press_view_basket_from_alert(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.add_to_basket_button()
        page.press_view_basket_from_alert()

    def test_press_checkout_from_alert(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.add_to_basket_button()
        page.press_checkout_from_alert()


@pytest.mark.regress
class TestAllProductsPageForRegisteredUser:
    product_item1 = "Coders at Work"
    menu_it = "Naviga nel negozio"
    basket_it = "Visualizza carrello"

    def test_verify_name_page(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.user_in_system()
        page.verify_page_name()

    def test_verify_page_structure(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.user_in_system()
        page.verify_menu_block()
        page.verify_product_block()

    def test_verify_menu(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.user_in_system()
        page.verify_menu_block()
        page.verify_menu_clothing_link()
        page.verify_menu_books_link()
        page.verify_menu_fiction()
        page.verify_menu_computers()
        page.verify_menu_non_fiction()
        page.verify_menu_programming()
        page.verify_menu_hacking()

    def test_verify_item_link(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.user_in_system()
        page.browser.execute_script("window.scrollBy(0, 200);")
        page.verify_item_link(TestAllProductsPageForGuest.product_item1)

    def test_press_item_link(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.user_in_system()
        page.browser.execute_script("window.scrollBy(0, 200);")
        page.press_item_link()

    def test_press_item_image(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.user_in_system()
        page.browser.execute_script("window.scrollBy(0, 200);")
        page.press_item_image()

    def test_user_go_to_user_page_by_press_icon(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.user_in_system()
        page.verify_account_icon()
        page.press_account_icon()
        login_page = LoginPage(browser)
        login_page.open()

    def test_user_go_to_user_page_by_press_link(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.user_in_system()
        page.verify_account_link()
        page.press_account_link()

    def test_user_logout(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.user_in_system()
        page.verify_logout_link()
        page.press_logout_link()

    def test_change_language(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.user_in_system()
        page.change_language_to_it()
        page.verify_change_language_to_it(TestAllProductsPageForRegisteredUser.menu_it,
                                          TestAllProductsPageForRegisteredUser.basket_it)

    def test_verify_next_button(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.user_in_system()
        page.verify_next_button()

    def test_go_to_next_page_and_back(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.user_in_system()
        page.press_next_button()
        next_page = AllProductsPage2(browser)
        next_page.verify_page_name()
        next_page.verify_next_page()
        next_page.verify_previous_button()
        next_page.press_previous_button()
        page = AllProductsPage(browser)
        page.open()

    def test_press_add_to_basket_button(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.user_in_system()
        page.add_to_basket_button()

    def test_verify_alerts_of_add_to_basket(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.user_in_system()
        page.add_to_basket_button()
        page.browser.execute_script("window.scrollBy(0, 100);")
        page.verify_alert1_of_add_to_basket()
        page.verify_alert2_of_add_to_basket()
        page.verify_alert3_of_add_to_basket()

    def test_press_view_basket_from_alert(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.user_in_system()
        page.add_to_basket_button()
        page.press_view_basket_from_alert()

    def test_press_checkout_from_alert(self, browser):
        page = AllProductsPage(browser)
        page.open()
        page.user_in_system()
        page.add_to_basket_button()
        page.press_checkout_from_alert()
