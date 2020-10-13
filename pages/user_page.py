from .base_page import BasePage

from .locators import UserPageLocators


class UserPage(BasePage):
    user_page = "http://selenium1py.pythonanywhere.com/en-gb/accounts/profile/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, UserPage.user_page)

    def verify_page_name(self):
        site_name = self.find(UserPageLocators.name_page).text
        assert site_name == "Profile", "Shop name is '%s'" % site_name

    def verify_success_alert(self):
        alert = self.find(UserPageLocators.registration_alert).text
        assert alert is not None, "'%s' is on page" % alert

    def verify_profile_form(self):
        form = self.find(UserPageLocators.profile_block)
        assert form is not None, "Profile form is presented on site"

    def verify_change_pass_button(self):
        change_pass = self.find_by_link_text(UserPageLocators.change_password_button).text
        assert change_pass == "Change password", "'%s' button is correct" % change_pass

    def press_change_pass_button(self):
        change_password = self.find_by_link_text(UserPageLocators.change_password_button)
        change_password.click()

    def verify_edit_profile_button(self):
        edit_profile = self.find_by_link_text(UserPageLocators.edit_profile_button).text
        assert edit_profile == "Edit profile", "'%s' button is correct" % edit_profile

    def press_edit_profile_button(self):
        edit_profile = self.find_by_link_text(UserPageLocators.edit_profile_button)
        edit_profile.click()

    def verify_delete_profile_button(self):
        delete_profile = self.find(UserPageLocators.delete_profile_button).text
        assert delete_profile == "Delete profile", "'%s' button is correct"

    def press_delete_profile_button(self):
        delete_profile = self.find(UserPageLocators.delete_profile_button)
        delete_profile.click()

    def verify_menu_profile_link(self):
        profile_link = self.find(UserPageLocators.profile_link_in_menu).text
        assert profile_link == "Profile", "'%s' button is correct" % profile_link

    def verify_menu_order_history(self):
        order_history = self.find(UserPageLocators.order_history_link_in_menu).text
        assert order_history == "Order History", "'%s' button is correct" % order_history

    def verify_menu_address_book(self):
        address_book = self.find(UserPageLocators.address_book_link_in_menu).text
        assert address_book == "Address Book", "'%s' button is correct" % address_book

    def verify_menu_email_history(self):
        email_history = self.find(UserPageLocators.email_history_link_in_menu).text
        assert email_history == "Email History", "'%s' button is correct" % email_history

    def verify_menu_product_alerts(self):
        product_alerts = self.find(UserPageLocators.product_alerts_link_in_menu).text
        assert product_alerts == "Product Alerts", "'%s' button is correct"

    def verify_menu_notifications(self):
        notifications = self.find(UserPageLocators.notification_link_in_menu).text
        assert notifications == "Notifications", "'%s' button is correct"

    def verify_menu_wish_lists(self):
        wish_lists = self.find(UserPageLocators.wish_lists_link_in_menu).text
        assert wish_lists == "Wish Lists", "'%s' button is correct"

    def alert_of_change_password(self):
        alert = self.find(UserPageLocators.alert_of_change_pass).text
        assert alert == "Password updated", "'%s' is correct" % alert

