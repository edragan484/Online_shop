from .base_page import BasePage

from .locators import ShippingAddressPageLocators


class ShippingAddressPage(BasePage):
    page_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, ShippingAddressPage.page_link)

