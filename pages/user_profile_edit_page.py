from .base_page import BasePage

from .locators import UserProfileEditPageLocators


class UserProfileEditPage(BasePage):
    user_page = "http://selenium1py.pythonanywhere.com/en-gb/accounts/profile/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, UserProfileEditPage.user_page)

    def change_name_field(self):
        name = self.find(UserProfileEditPageLocators.name_field_for_change)
        name.clear()
        name.send_keys("Elena")

    def press_button_save(self):
        save = self.find(UserProfileEditPageLocators.save_button)
        save.click()

    def press_button_cancel(self):
        cancel = self.find_by_link_text(UserProfileEditPageLocators.cancel)
        cancel.click()
