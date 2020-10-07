from .base_page import BasePage
from .login_page import LoginPage

from .locators import MainPageLocators


class MainPage(BasePage):
    main_page = "http://selenium1py.pythonanywhere.com/en-gb/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, MainPage.main_page)

    def go_to_login_page(self):
        login_link = self.find(MainPageLocators.login_page_link)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def verify_login_link(self):
        assert self.is_element_present(MainPageLocators.login_page_link), "Login link is not presented"

    def is_element_present(self, login_page_link):
        pass

    def change_language(self):
        language1 = self.find(MainPageLocators.language_field)
        language1.click()
        button_language = self.find(MainPageLocators.button_change_language_submit)
        button_language.click()

    def verify_menu_and_basket_text(self, menu_text, basket_text):
        all_products_button = self.find(MainPageLocators.all_products)
        assert menu_text == all_products_button.text, "Translate is correct"
        basket_button = self.find(MainPageLocators.basket)
        assert basket_text == basket_button.text, "Translate is correct"

    def verify_success_alert(self):
        alert_welcome = self.find(MainPageLocators.alert_welcome_user).text
        assert alert_welcome == "Welcome back", "Alert is correct"




