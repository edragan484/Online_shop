from .base_page import BasePage

from .locators import BasketPageLocators

link = "http://selenium1py.pythonanywhere.com/en-gb/basket/"


class BasketPage(BasePage):
    def check_page_name(self):
        page_name = self.browser.find_element(*BasketPageLocators.page_name).text
        assert page_name is not None, "%s is correct" % page_name

    def check_items_in_basket(self):
        items_in_basket = self.browser.find_element(*BasketPageLocators.basket_items).text
        assert items_in_basket is not None, "Items are in basket"

    def check_price_of_item(self):
        price_of_item = self.browser.find_element(*BasketPageLocators.sum_price)
        assert price_of_item is not None, "Price of item is printed"

    def check_price_the_city_and_the_stars(self):
        price_of_item_city = self.browser.find_element(*BasketPageLocators.sum_price).text
        assert price_of_item_city == "16.99"

    def check_shipping_free(self):
        free_shipping = self.browser.find_element(*BasketPageLocators.free_shipping).text
        assert free_shipping == "0.00"
