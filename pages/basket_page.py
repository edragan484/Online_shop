from .base_page import BasePage

from .locators import BasketPageLocators


class BasketPage(BasePage):
    link_page = "http://selenium1py.pythonanywhere.com/en-gb/basket/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, BasketPage.link_page)

    def verify_page_name(self):
        page_name = self.find(BasketPageLocators.page_name).text
        assert page_name is not None, "%s is correct" % page_name

    def verify_items_in_basket(self):
        items_in_basket = self.find(BasketPageLocators.basket_items).text
        assert items_in_basket is not None, "Items are in basket"

    def verify_price_of_item(self):
        price_of_item = self.find(BasketPageLocators.sum_price)
        assert price_of_item is not None, "Price of item is presented"

    def verify_price_the_city_and_the_stars(self):
        price_of_item_city = self.find(BasketPageLocators.sum_price).text
        assert price_of_item_city == "£16.99"

    def verify_shipping_free(self):
        free_shipping = self.find_by_xpath(BasketPageLocators.free_shipping).text
        assert free_shipping == "£0.00"

    def press_proceed_to_checkout_button(self):
        checkout_button = self.find(BasketPageLocators.button_proceed_to_checkout)
        checkout_button.click()


