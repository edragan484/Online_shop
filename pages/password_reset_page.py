from .base_page import BasePage

from .locators import PasswordResetPageLocators


class PasswordResetPage(BasePage):
    page_link = "http://selenium1py.pythonanywhere.com/en-gb/password-reset/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, PasswordResetPage.page_link)

    def email_field_for_recover(self):
        email_field = self.find(PasswordResetPageLocators.email_field)
        email_field.send_keys("user2020")

    def button_for_recover(self):
        send_reset_email_button = self.find(PasswordResetPageLocators.send_reset_email_button)
        send_reset_email_button.click()

    def alert_recover(self):
        alert_confirmation = self.find(PasswordResetPageLocators.alert_reset)
        assert alert_confirmation is not None, "Alert of info recovery is on page"
