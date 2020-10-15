from .base_page import BasePage
from .locators import ClothingVariantPageLocators


class ClothingVariantPage(BasePage):
    page_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/django-t-shirt_10/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, ClothingVariantPage.page_link)

    def verify_page_name(self):
        page_name = self.find(ClothingVariantPageLocators.page_name)
        assert page_name == "Django T-shirt"

    def verify_image_product(self):
        image_product = self.find(ClothingVariantPageLocators.variant_image)
        assert image_product is not None, "Product image is presented"

    def press_write_review_button(self):
        write_review = self.find(ClothingVariantPageLocators.review_button)
        write_review.click()

    def press_add_to_basket_button(self):
        write_review = self.find(ClothingVariantPageLocators.button_add_to_basket)
        write_review.click()

    def verify_viewed_products_block(self):
        viewed_products = self.find(ClothingVariantPageLocators.viewed_products)
        assert viewed_products is not None, "Products block is presented"


