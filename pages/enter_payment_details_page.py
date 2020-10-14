from .base_page import BasePage

from .locators import EnterPaymentDetailsPageLocators


class EnterPaymentDetailsPage(BasePage):
    page_link = "http://selenium1py.pythonanywhere.com/en-gb/checkout/payment-details/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, EnterPaymentDetailsPage.page_link)

    def verify_name_page(self):
        name_page = self.find(EnterPaymentDetailsPageLocators.page_name).text
        assert "Enter payment details" in name_page, "Name page '%s' name is correct" % name_page

    def press_button_continue(self):
        continue_button = self.find(EnterPaymentDetailsPageLocators.button_continue)
        continue_button.click()

