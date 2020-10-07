from .base_page import BasePage

from .locators import UserPageLocators


class UserPage(BasePage):
    user_page = "http://selenium1py.pythonanywhere.com/en-gb/accounts/profile/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, UserPage.user_page)

    def verify_success_alert(self):
        alert = self.find(UserPageLocators.registration_alert).text
        assert alert is not None, "'%s' is on page" % alert


