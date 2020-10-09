import random

from .base_page import BasePage

from .locators import RegisterFromCheckoutPageLocators


class RegisterFromCheckoutPage(BasePage):
    unique_var = random.randint(1, 1000000)
    email = "{}@hotmail.com".format(unique_var)
    page_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/register/?next=/en-gb/checkout/shipping-address/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, RegisterFromCheckoutPage.page_link)

    def verify_name_page(self):
        page_name = self.find(RegisterFromCheckoutPageLocators.page_name)
        assert page_name == "Register", "'%s' is correct name page"

    def fill_new_email(self):
        new_email = self.find(RegisterFromCheckoutPageLocators.email_field)
        new_email.clear()
        new_email.send_keys(RegisterFromCheckoutPage.email)

    def fill_password_guest(self):
        new_password = self.find(RegisterFromCheckoutPageLocators.email_field)
        new_password.send_keys(RegisterFromCheckoutPage.email)
        password2 = self.find(RegisterFromCheckoutPageLocators.confirm_password)
        password2.send_keys(RegisterFromCheckoutPage.email)

    def press_register_button(self):
        register_button = self.find(RegisterFromCheckoutPageLocators.button_register)
        register_button.click()
        


