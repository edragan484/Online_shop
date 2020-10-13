from .base_page import BasePage

from .locators import DeleteProfilePageLocators


class DeleteProfilePage(BasePage):
    user_page = "http://selenium1py.pythonanywhere.com/en-gb/accounts/profile/delete/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, DeleteProfilePage.user_page)

    def cancel_delete_profile_link(self):
        cancel = self.find_by_link_text(DeleteProfilePageLocators.cancel)
        cancel.click()

