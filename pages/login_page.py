import random

from .base_page import BasePage

from .locators import LoginPageLocators


class LoginPage(BasePage):
    unique_var = random.randint(1, 1000000)

    def should_be_login_page(self):
        login_page = self.browser.find_element(*LoginPageLocators.should_be_login_page)
        assert login_page is not None, "Login page is"

    def should_be_login_url(self):
        login_url = self.browser.get(*LoginPageLocators.should_be_login_url)
        login_url_text = login_url.text
        assert login_url == login_url_text, "Login url is and correct"

    def should_be_login_form(self):
        login_form = self.browser.find_element(*LoginPageLocators.should_be_login_form)
        assert login_form is not None, "Login form is on page"

    def should_be_register_form(self):
        register_form = self.browser.find_element(*LoginPageLocators.should_be_register_form)
        assert register_form is not None, "Register form is on page"

    def fill_email_registration_field(self):
        unique_var = random.randint(1, 1000000)
        email_address_field = self.browser.find_element(*LoginPageLocators.email_registration_field)
        email_address_field.clear()
        email_address_field.send_keys("{}@gmail.com".format(unique_var))

    def fill_password_registration_field(self):
        unique_var = random.randint(1, 1000000)
        password1 = self.browser.find_element(*LoginPageLocators.password_registration_field)
        password1.clear()
        password1.send_keys(unique_var, unique_var)

    def fill_password_confirmation_field(self):
        unique_var = random.randint(1, 1000000)
        password2 = self.browser.find_element(*LoginPageLocators.password_confirmation_field)
        password2.clear()
        password2.send_keys(unique_var, unique_var)

    def submit_new_user(self):
        button_submit_registration = self.browser.find_element(*LoginPageLocators.button_submit_registration)
        button_submit_registration.click()

