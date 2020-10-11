import random

from .base_page import BasePage

from .locators import LoginPageLocators


class LoginPage(BasePage):
    unique_var = random.randint(1, 1000000)
    email = "{}@mail.com".format(unique_var)

    login_page = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, LoginPage.login_page)

    def check_login_page(self):
        login_page_button = self.find(LoginPageLocators.login_page_button)
        assert login_page_button is not None, "Login page is"
        # assert login_page_button == LoginPage.login_page, "Login page is correct"

    def verify_login_url(self):
        login_url = self.browser.get(LoginPageLocators.login_url)
        login_url_text = login_url.text
        assert login_url == login_url_text, "Login url is and correct"

    def verify_login_form(self):
        login_form = self.find(LoginPageLocators.login_form)
        assert login_form is not None, "Login form is on page"

    def verify_register_form(self):
        register_form = self.find(LoginPageLocators.register_form)
        assert register_form is not None, "Register form is on page"

    def fill_email_registration_field(self):
        email_address_field = self.find(LoginPageLocators.email_registration_field)
        email_address_field.clear()
        email_address_field.send_keys(LoginPage.email)

    def fill_password_registration_field(self):
        password1 = self.find(LoginPageLocators.password_registration_field)
        password1.clear()
        password1.send_keys(LoginPage.email)

    def fill_password_confirmation_field(self):
        password2 = self.find(LoginPageLocators.password_confirmation_field)
        password2.clear()
        password2.send_keys(LoginPage.email)

    def submit_new_user(self):
        button_submit_registration = self.find(LoginPageLocators.button_submit_registration)
        button_submit_registration.click()

    def fill_user_email_field(self):
        email_address_field = self.find(LoginPageLocators.email_login)
        email_address_field.clear()
        email_address_field.send_keys("user2020@gmail.com")

    def fill_user_password_field(self):
        password1 = self.find(LoginPageLocators.password_login)
        password1.clear()
        password1.send_keys("QRTYvvbbnmYU")

    def submit_enter_user(self):
        button_submit_registration = self.find(LoginPageLocators.button_login)
        button_submit_registration.click()

    def recover_password(self):
        recover_pass_link = self.find(LoginPageLocators.recover_password_link)
        recover_pass_link.click()

    def registered_user_on_main_page(self):
        email_address_field = self.find(LoginPageLocators.email_login)
        email_address_field.clear()
        email_address_field.send_keys("user2020@gmail.com")
        password1 = self.find(LoginPageLocators.password_login)
        password1.clear()
        password1.send_keys("QRTYvvbbnmYU")
        button_submit_registration = self.find(LoginPageLocators.button_login)
        button_submit_registration.click()

