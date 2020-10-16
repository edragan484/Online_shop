from .base_page import BasePage
from .locators import Product2PageLocators


class Product2Page(BasePage):
    product_name = "Google Hacking"
    page_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/google-hacking_197/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, Product2Page.page_link)

    def verify_name_page(self):
        name_page = self.find(Product2PageLocators.name_page).text
        assert Product2Page.product_name == name_page, \
            "Product name '%s' is '%s'" % (Product2Page.product_name, name_page)

    def verify_product_image(self):
        image = self.find(Product2PageLocators.product_image)
        image_name = image.get_attribute("alt")
        assert image_name == Product2Page.product_name, "'%s' is correct"

    def verify_review_button(self):
        review = self.find(Product2PageLocators.review_button)
        assert review is not None, "Review button is presented"

    def press_review_button(self):
        review = self.find(Product2PageLocators.review_button)
        review.click()

    def add_to_basket(self):
        button_add_to_basket = self.find(Product2PageLocators.button_add)
        button_add_to_basket.click()

    def verify_alert_of_add_product(self):
        alert_of_add_product = self.find(Product2PageLocators.alert_of_add_product).text
        assert "has been added to your basket." in alert_of_add_product, \
            "'%s'has been added to your basket." % Product2Page.product_name

    def press_basket_button(self):
        basket = self.find(Product2PageLocators.basket)
        basket.click()

