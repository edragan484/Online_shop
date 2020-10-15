import random

from .base_page import BasePage
from .locators import CheckoutPageLocators


class CheckoutPage(BasePage):
    unique_var = random.randint(1, 1000000)
    email = "{}@hotmail.com".format(unique_var)
    main_page = "http://selenium1py.pythonanywhere.com/en-gb/checkout/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, CheckoutPage.main_page)

    def verify_checkout_form(self):
        checkout_form = self.find(CheckoutPageLocators.checkout_form)
        assert checkout_form is not None, "Checkout form is present on the page"

    def fill_email_in_checkout_guest(self):
        new_email_checkout = self.find(CheckoutPageLocators.email_field)
        new_email_checkout.clear()
        new_email_checkout.send_keys(CheckoutPage.email)

    def fill_email_in_checkout_customer(self):
        new_email_checkout = self.find(CheckoutPageLocators.email_field)
        new_email_checkout.clear()
        new_email_checkout.send_keys("user2020@gmail.com")

    def new_customer_button_checked(self):
        new_customer = self.find(CheckoutPageLocators.checkbox1_guest)
        new_customer.click()

    def returning_customer_button_checked(self):
        returning_customer = self.find(CheckoutPageLocators.checkbox2_existing)
        returning_customer.click()

    def fill_password_guest(self):
        new_password = self.find(CheckoutPageLocators.password_field)
        new_password.send_keys(CheckoutPage.email, CheckoutPage.unique_var)

    def fill_password_customer(self):
        new_password = self.find(CheckoutPageLocators.password_field)
        new_password.send_keys("QRTYvvbbnmYU")

    def create_new_account_checked(self):
        create_account = self.find(CheckoutPageLocators.checkbox3_new)
        create_account.click()

    def password_reminder_link(self):
        password_reminder = self.find(CheckoutPageLocators.password_reminder_link)
        password_reminder.click()

    def button_continue(self):
        button_continue = self.find(CheckoutPageLocators.button_continue)
        button_continue.click()



