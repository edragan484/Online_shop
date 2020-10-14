from .base_page import BasePage

from .locators import AccountProfileEditPageLocators


class AccountProfileEditPage(BasePage):

    user_page = "http://selenium1py.pythonanywhere.com/en-gb/accounts/profile/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, AccountProfileEditPage.user_page)

    def change_name_field(self):
        name = self.find(AccountProfileEditPageLocators.name_field_for_change)
        name.clear()
        name.send_keys("Elena")

    def press_button_save(self):
        save = self.find(AccountProfileEditPageLocators.save_button)
        save.click()

    def press_button_cancel(self):
        cancel = self.find_by_link_text(AccountProfileEditPageLocators.cancel)
        cancel.click()
