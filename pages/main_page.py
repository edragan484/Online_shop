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
        language1 = self.browser.find(*MainPageLocators.language_field)
        language1.click()
        language_it = self.browser.find(*MainPageLocators.language_italian)
        language_it.click()

        button_language = self.browser.find(*MainPageLocators.button_change_language_submit)
        button_language.click()
        all_products_it = self.browser.find(*MainPageLocators.all_products)
        assert "Naviga nel negozio" == all_products_it.text, "%s on italian" % all_products_it.text

        basket_it = self.browser.find(*MainPageLocators.basket)
        assert "Visualizza carrello" == basket_it.text, "%s italian" % basket_it.text

    def change_language_to_deutsch(self):
        language2 = self.browser.find(*MainPageLocators.language_field)
        language2.click()
        language_de = self.browser.find(*MainPageLocators.language_deutsch)
        language_de.click()

        button_language = self.browser.find(*MainPageLocators.button_change_language_submit)
        button_language.click()
        all_products_de = self.browser.find(*MainPageLocators.all_products)
        assert "Alle produkte" == all_products_de.text

        basket_en = self.browser.find(*MainPageLocators.basket)
        assert "Warenkorb anzeigen" == basket_en.text
