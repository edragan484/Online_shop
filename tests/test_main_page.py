import time

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.user_page import UserPage
from pages.basket_page import BasketPage
from pages.checkout_page import CheckoutPage
from pages.shipping_address_page import ShippingAddressPage
from pages.enter_payment_details_page import EnterPaymentDetailsPage
from pages.preview_order_page import PreviewOrderPage
from pages.order_confirmation_page import OrderConfirmationPage


class TestMainPageForGuestsRegress:
    product_name1 = "Coders at Work"
    menu_deutsch = "Im Webshop stöbern"
    basket_deutsch = "Warenkorb anzeigen"

    def test_verify_site_name(self, browser):
        page = MainPage(browser)
        page.open()
        page.verify_site_name()
        page.verify_site_subname()

    def test_verify_guest_see_login_link(self, browser):
        page = MainPage(browser)
        page.open()
        page.verify_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser)
        login_page.check_login_page()

    def test_guest_check_change_languages(self, browser):
        page = MainPage(browser)
        page.open()
        page.change_language_to_it()
        page.verify_menu_and_basket_text_in_it()
        page.change_language_to_deutsch()
        page.verify_menu_and_basket_text_in_deutsch()
        page.verify_another_method_deutsch(TestMainPageForGuestsRegress.menu_deutsch, TestMainPageForGuestsRegress.basket_deutsch)

    def test_verify_search_item(self, browser):
        page = MainPage(browser)
        page.open()
        page.searching_item(TestMainPageForGuestsRegress.product_name1)
        page.verify_search_items_is_correct(TestMainPageForGuestsRegress.product_name1)
        page.verify_image_found_item_is_correct(TestMainPageForGuestsRegress.product_name1)

    def test_verify_welcome_block(self, browser):
        page = MainPage(browser)
        page.open()
        page.verify_welcome_block()

    def test_verify_recommended_reading_block(self, browser):
        page = MainPage(browser)
        page.open()
        page.verify_recommended_reading_block()

    def test_verify_other_books_block(self, browser):
        page = MainPage(browser)
        page.open()
        page.verify_other_good_books_block()

    def test_add_item_to_basket(self, browser):
        page = MainPage(browser)
        page.open()
        page.add_to_basket_from_main_page()

    def test_verify_alerts_of_add_item_to_basket(self, browser):
        page = MainPage(browser)
        page.open()
        page.add_to_basket_from_main_page()
        page.verify_alert_of_add_item_to_basket()
        page.verify_alert_of_offer()
        page.verify_alert_basket_total()

    def test_verify_basket_and_checkout_buttons_in_alert(self, browser):
        page = MainPage(browser)
        page.open()
        page.add_to_basket_from_main_page()
        page.verify_alert_basket_total()
        page.verify_view_basket_button_in_alert()
        page.verify_checkout_in_alert()

    def test_go_to_basket_from_add_item_alert(self, browser):
        page = MainPage(browser)
        page.open()
        page.add_to_basket_from_main_page()
        page.verify_alert_basket_total()
        page.go_to_basket_from_alert()

    def test_go_to_checkout_from_add_item_alert(self, browser):
        page = MainPage(browser)
        page.open()
        page.add_to_basket_from_main_page()
        page.verify_alert_basket_total()
        page.go_to_checkout_from_alert()

    def test_verify_page_constructor(self, browser):
        page = MainPage(browser)
        page.open()
        page.verify_menu_block()
        page.verify_welcome_block()
        page.verify_other_good_books_block()
        page.verify_recommended_reading_block()

    def test_verify_menu_links(self, browser):
        page = MainPage(browser)
        page.open()
        page.verify_all_products_button_menu()
        page.verify_clothing_button_menu()
        page.verify_books_button_menu()
        page.verify_offers_button_menu()

    def test_verify_add_item_to_basket(self, browser):
        page = MainPage(browser)
        page.open()
        page.add_to_basket_from_main_page()
        page.verify_alert_of_add_item_to_basket()
        page.verify_alert_of_offer()
        page.verify_alert_basket_total()
        page.verify_view_basket_button_in_alert()
        page.verify_checkout_in_alert()


class TestMainPageForGuestEndToEnd:
    def test_buy_product_from_main_page(self, browser):
        page = MainPage(browser)
        page.open()
        page.add_to_basket_from_main_page()
        page.press_basket_button()
        basket_page = BasketPage(browser)
        basket_page.open()
        basket_page.verify_page_name()
        basket_page.verify_items_in_basket()
        basket_page.verify_price_of_item()
        basket_page.verify_shipping_free()
        basket_page.verify_price_the_city_and_the_stars()
        basket_page.press_proceed_to_checkout_button()
        checkout_page = CheckoutPage(browser)
        checkout_page.open()
        checkout_page.fill_email_in_checkout_guest()
        checkout_page.new_customer_button_checked()
        checkout_page.fill_password_guest()
        checkout_page.button_continue()
        shipping_address_page = ShippingAddressPage(browser)
        shipping_address_page.open()
        shipping_address_page.fill_shipping_title()
        shipping_address_page.fill_first_name()
        shipping_address_page.fill_last_name()
        shipping_address_page.fill_address1()
        shipping_address_page.fill_city()
        shipping_address_page.fill_zip()
        shipping_address_page.fill_country()
        shipping_address_page.push_button_continue()
        enter_payment_details_page = EnterPaymentDetailsPage(browser)
        enter_payment_details_page.open()
        enter_payment_details_page.verify_name_page()
        enter_payment_details_page.push_button_continue()
        preview_order_page = PreviewOrderPage(browser)
        preview_order_page.open()
        preview_order_page.verify_name_page()
        preview_order_page.verify_address_review()
        preview_order_page.verify_payment_review()
        preview_order_page.verify_basket_items_review()
        preview_order_page.push_place_order_button()
        order_confirmation_page = OrderConfirmationPage(browser)
        order_confirmation_page.open()
        order_confirmation_page.verify_name_page()
        order_confirmation_page.verify_address_review()
        order_confirmation_page.verify_basket_items_review()
        order_confirmation_page.verify_button_print_page()
        order_confirmation_page.verify_continue_shopping()
