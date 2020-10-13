from .base_page import BasePage

from .locators import AllProductsPage2Locators


class AllProductsPage2(BasePage):

    page_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/?page=2"

    def __init__(self, browser):
        BasePage.__init__(self, browser, AllProductsPage2.page_link)

    def verify_page_name(self):
        page_name = self.find(AllProductsPage2Locators.name_page)
        assert page_name == "All Products", "'%s' is correct name name" % page_name

    def verify_next_page(self):
        next_button = self.find(AllProductsPage2Locators.button_next).text
        assert next_button == "next", "Button '%s' is correct" % next_button

    def verify_previous_button(self):
        previous_button = self.find(AllProductsPage2Locators.button_previous).text
        assert previous_button == "previous", "Button '%s' is correct" % previous_button

    def press_previous_button(self):
        previous_button = self.find(AllProductsPage2Locators.button_previous)
        previous_button.click()

