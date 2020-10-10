from .base_page import BasePage

from .locators import PreviewOrderPageLocators


class PreviewOrderPage(BasePage):
    page_link = "http://selenium1py.pythonanywhere.com/en-gb/checkout/preview/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, PreviewOrderPage.page_link)

    def verify_name_page(self):
        page_name = self.find(PreviewOrderPageLocators.page_name).text
        assert page_name == "Preview order", "'%s' is correct name page"

    def verify_address_review(self):
        address = self.find(PreviewOrderPageLocators.address_review)
        assert address is not None, "Address is present in form"

    def verify_payment_review(self):
        payment = self.find(PreviewOrderPageLocators.payment_review)
        assert payment is not None, "Payment review is presented in form"

    def verify_basket_items_review(self):
        basket_items = self.find(PreviewOrderPageLocators.basket_items_review)
        assert basket_items is not None, "Basket items are presented in form"

    def push_place_order_button(self):
        order_button = self.find(PreviewOrderPageLocators.button_place_order)
        order_button.click()
