import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.regress
class TestProductPageForGuest:
    product_name1 = "Excession"

    def test_verify_product_name(self, browser):
        page = ProductPage(browser)
        page.open()
        page.verify_name_page()
        page.verify_product_image()
        page.verify_product_price()
        page.verify_review_button()

    def test_verify_guest_see_login_link(self, browser):
        page = ProductPage(browser)
        page.open()
        page.verify_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        page = ProductPage(browser)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser)
        login_page.check_login_page()

    def test_add_item_to_basket(self, browser):
        page = ProductPage(browser)
        page.open()
        page.add_to_basket()

    def test_press_review_button(self, browser):
        page = ProductPage(browser)
        page.open()
        page.press_review_button()

    def test_verify_alerts_of_add_item(self, browser):
        page = ProductPage(browser)
        page.open()
        page.add_to_basket()
        page.verify_alert_of_add_product()

    def test_go_to_basket(self, browser):
        page = ProductPage(browser)
        page.open()
        page.press_basket_button()

    def test_go_to_basket_from_alert(self, browser):
        page = ProductPage(browser)
        page.open()
        page.add_to_basket()
        page.press_view_basket_in_alert()

    def test_go_to_checkout_from_alert(self, browser):
        page = ProductPage(browser)
        page.open()
        page.add_to_basket()
        page.press_checkout_in_alert()


@pytest.mark.regress
class TestProductPageForRegisteredUser:
    product_name1 = "Excession"

    def test_verify_product_name(self, browser):
        page = ProductPage(browser)
        page.open()
        page.user_in_system()
        page.verify_name_page()
        page.verify_product_image()
        page.verify_product_price()
        page.verify_review_button()

    def test_verify_guest_see_login_link(self, browser):
        page = ProductPage(browser)
        page.open()
        page.user_in_system()
        page.verify_logout_link()

    def test_guest_can_go_to_login_page(self, browser):
        page = ProductPage(browser)
        page.open()
        page.user_in_system()
        page.logout()

    def test_add_item_to_basket(self, browser):
        page = ProductPage(browser)
        page.open()
        page.user_in_system()
        page.add_to_basket()

    def test_press_review_button(self, browser):
        page = ProductPage(browser)
        page.open()
        page.user_in_system()
        page.press_review_button()

    def test_verify_alerts_of_add_item(self, browser):
        page = ProductPage(browser)
        page.open()
        page.user_in_system()
        page.add_to_basket()
        page.verify_alert_of_add_product()

    def test_go_to_basket(self, browser):
        page = ProductPage(browser)
        page.open()
        page.user_in_system()
        page.press_basket_button()

    def test_go_to_basket_from_alert(self, browser):
        page = ProductPage(browser)
        page.open()
        page.user_in_system()
        page.add_to_basket()
        page.press_view_basket_in_alert()

    def test_go_to_checkout_from_alert(self, browser):
        page = ProductPage(browser)
        page.open()
        page.user_in_system()
        page.add_to_basket()
        page.press_checkout_in_alert()

