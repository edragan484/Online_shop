from .base_page import BasePage

from .locators import UserPageLocators


class UserPage(BasePage):
    def should_be_success_confirmation(self):
        alert = self.browser.find_element(*UserPageLocators.registration_alert).text
        assert alert is not None, "'%s' is on page" % alert
