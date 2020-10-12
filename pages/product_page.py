
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    product_name = "The City and the Stars"
    page_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, ProductPage.page_link)

    def verify_name_page(self):
        name_page = self.find(ProductPageLocators.name_page).text
        assert ProductPage.product_name == name_page, \
            "Product name '%s' is '%s'" % (ProductPage.product_name, name_page)

    def verify_product_image(self):
        image = self.find(ProductPageLocators.product_image)
        image_name = image.get_attribute("alt")
        assert image_name == ProductPage.product_name, "'%s' is correct"

    def verify_review_button(self):
        review = self.find(ProductPageLocators.review_button)
        assert review is not None, "Review button is presented"

    def press_review_button(self):
        review = self.find(ProductPageLocators.review_button)
        review.click()

    def verify_product_price(self):
        price = self.find(ProductPageLocators.product_price).text
        assert price == "£16.99", "Review button is presented"

    def add_to_basket(self):
        button_add_to_basket = self.find(ProductPageLocators.button_add)
        button_add_to_basket.click()

    def verify_alert_of_add_product(self):
        button_add_to_basket = self.find(ProductPageLocators.button_add)
        button_add_to_basket.click()
        alert_of_add_product = self.find(ProductPageLocators.alert_of_add_product).text
        assert alert_of_add_product == ProductPage.product_name + "has been added to your basket.", \
            "'%s'has been added to your basket." % ProductPage.product_name

    def check_alert_of_add_on_product_page(self):
        button_add_to_basket = self.find(ProductPageLocators.button_add)
        button_add_to_basket.click()
        alert_of_add_product = self.browser.find_element(ProductPageLocators.alert_of_add_product)
        assert ProductPage.product_name in alert_of_add_product, \
            "'%s' has been added to your basket." % ProductPage.product_name
        