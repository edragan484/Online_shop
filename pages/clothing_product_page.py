from .base_page import BasePage
from .locators import ClothingProductPageLocators


class ClothingProductPage(BasePage):
    page_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/django-t-shirt_8/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, ClothingProductPage.page_link)

    def verify_page_name(self):
        page_name = self.find(ClothingProductPageLocators.page_name)
        assert page_name == "Django T-shirt"

    def verify_image_product_link(self):
        image_product = self.find(ClothingProductPageLocators.product_image)
        assert image_product is not None, "Product image is presented"

    def press_product_variant1_link(self):
        clothing_link = self.find(ClothingProductPageLocators.variant1)
        clothing_link.click()

    def press_product_variant2_link(self):
        clothing_link = self.find(ClothingProductPageLocators.variant2)
        clothing_link.click()

    def write_review_button(self):
        write_review = self.find(ClothingProductPageLocators.review_button)
        write_review.click()

    def verify_viewed_products_block(self):
        viewed_products = self.find(ClothingProductPageLocators.viewed_products)
        assert viewed_products is not None, "Products block is presented"

