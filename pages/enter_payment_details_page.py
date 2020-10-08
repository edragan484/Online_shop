from .base_page import BasePage

from .locators import EnterPaymentDetailsPageLocators


class EnterPaymentDetailsPage(BasePage):
    page_link = "http://selenium1py.pythonanywhere.com/en-gb/checkout/payment-details/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, EnterPaymentDetailsPage.page_link)

    def verify_name_page(self):
        name_page = self.find(EnterPaymentDetailsPageLocators.page_name)
        assert name_page == "Enter payment details", "Page name is correct"

    def push_button_continue(self):
        continue_button = self.find(EnterPaymentDetailsPageLocators.button_continue)
        continue_button.click()

