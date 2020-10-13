from .base_page import BasePage
from .locators import ChangePasswordPageLocators


class ChangePasswordPage(BasePage):
    page_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/change-password/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, ChangePasswordPage.page_link)

    def verify_page_name(self):
        page_name = self.find(ChangePasswordPageLocators.page_name).text
        assert page_name == "Change Password", "'%s' page name is correct"

    def change_password_for_new(self):
        old_password = self.find(ChangePasswordPageLocators.old_password_field)
        old_password.send_keys("QRTYvvbbnmYU")
        new_password = self.find(ChangePasswordPageLocators.new_password_field)
        new_password.send_keys("QRTYvvbbnmYUTYRE")
        new_pass_confirm = self.find(ChangePasswordPageLocators.new_password_confirm)
        new_pass_confirm.send_keys("QRTYvvbbnmYUTYRE")
        save = self.find(ChangePasswordPageLocators.save_button)
        save.click()

    def change_password_for_old(self):
        old_password = self.find(ChangePasswordPageLocators.old_password_field)
        old_password.send_keys("QRTYvvbbnmYUTYRE")
        new_password = self.find(ChangePasswordPageLocators.new_password_field)
        new_password.send_keys("QRTYvvbbnmYU")
        new_pass_confirm = self.find(ChangePasswordPageLocators.new_password_confirm)
        new_pass_confirm.send_keys("QRTYvvbbnmYU")
        save = self.find(ChangePasswordPageLocators.save_button)
        save.click()
