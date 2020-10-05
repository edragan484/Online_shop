from .base_page import BasePage

from .locators import PasswordResetPageLocators

link = "http://selenium1py.pythonanywhere.com/en-gb/password-reset/"


class PasswordResetPage(BasePage):

    def email_field_for_recover(self):
        email_field = self.browser.find_element(*PasswordResetPageLocators.email_field)
        email_field.send_keys("user2020")

    def button_for_recover(self):
        send_reset_email_button = self.browser.find_element(*PasswordResetPageLocators.send_reset_email_button)
        send_reset_email_button.click()

    def alert_recover(self):
        alert_confirmation = self.browser.find_element(*PasswordResetPageLocators.alert_reset)
        assert alert_confirmation is not None, "Alert of info recovery is on page"
