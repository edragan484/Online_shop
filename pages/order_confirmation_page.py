from .base_page import BasePage

from .locators import OrderConfirmationPageLocators


class OrderConfirmationPage(BasePage):
    page_link = "http://selenium1py.pythonanywhere.com/en-gb/checkout/thank-you/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, OrderConfirmationPage.page_link)

    def verify_name_page(self):
        name_page = self.find(OrderConfirmationPageLocators.page_name).text
        assert "Order" in name_page, "Its Order confirmation page"
        assert "confirmation" in name_page, "Its Order confirmation page"

    def verify_address_review(self):
        address = self.find(OrderConfirmationPageLocators.address_review)
        assert address is not None, "Address is present in form"

    def verify_basket_items_review(self):
        basket_items = self.find(OrderConfirmationPageLocators.basket_items_review)
        assert basket_items is not None, "Basket items are presented in form"

    def verify_button_print_page(self):
        button_print_page = self.find(OrderConfirmationPageLocators.button_print_this_page).text
        assert button_print_page == "Print this page", "Button '%s' is on page"

    def push_button_print_page(self):
        button_print = self.find(OrderConfirmationPageLocators.button_print_this_page)
        button_print.click()

    def verify_print_page(self):
        addition_page = self.find(OrderConfirmationPageLocators.addition_page)
        assert addition_page is not None, "Addition page is open"
        print_button_add_page = self.find(OrderConfirmationPageLocators.print_button_addition_page)
        assert print_button_add_page is not None, "Addition print on page"

    def verify_continue_shopping(self):
        continue_shopping_button = self.find(OrderConfirmationPageLocators.button_continue_shopping).text
        assert continue_shopping_button == "Continue shopping"

    def push_continue_shopping(self):
        continue_shopping_button = self.find(OrderConfirmationPageLocators.button_continue_shopping)
        continue_shopping_button.ckick()




