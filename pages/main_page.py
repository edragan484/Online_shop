from .base_page import BasePage
from .login_page import LoginPage

from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def change_language_to_italian(self):
        language1 = self.browser.find_element(*MainPageLocators.language_field)
        language1.click()
        language_it = self.browser.find_element(*MainPageLocators.language_italian)
        language_it.click()

        button_language = self.browser.find_element(*MainPageLocators.button_change_language_submit)
        button_language.click()

        all_products_it = self.browser.find_element(*MainPageLocators.all_products)
        assert "Naviga nel negozio" == all_products_it.text, "Its on italian"
        basket_it = self.browser.find_element(*MainPageLocators.basket)
        assert "Visualizza carrello" == basket_it.text, "Its italian"

    def change_language_to_deutsch(self):
        language2 = self.browser.find_element(*MainPageLocators.language_field)
        language2.click()
        language_de = self.browser.find_element(*MainPageLocators.language_deutsch)
        language_de.click()
        button_language = self.browser.find_element(*MainPageLocators.button_change_language_submit)
        button_language.click()

        all_products_de = self.browser.find_element(*MainPageLocators.all_products).text
        assert "Im Webshop stöbern" == all_products_de, "On German"
        basket_en = self.browser.find_element(*MainPageLocators.basket).text
        assert "Warenkorf anzeigen" == basket_en, "On German"
