from .base_page import BasePage
from .locators import ClothingPageLocators


class ClothingPage(BasePage):
    page_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/category/clothing_1/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, ClothingPage.page_link)

    def verify_page_name(self):
        page_name = self.find(ClothingPageLocators.page_name)
        assert page_name == "Clothing"

    def verify_menu_block(self):
        menu = self.find(ClothingPageLocators.menu_block)
        assert menu is not None, "Block menu is present on the page"

    def verify_product_block(self):
        clothing = self.find(ClothingPageLocators.product_clothing_block)
        assert clothing is not None, "Block menu is present on the page"

    def verify_menu_clothing_link(self):
        clothing = self.find_by_link_text(ClothingPageLocators.clothing_link).text
        assert clothing == "Clothing"

    def verify_menu_books_link(self):
        books_link = self.find_by_link_text(ClothingPageLocators.books_link).text
        assert books_link == "Books"

    def verify_menu_fiction(self):
        fiction_link = self.find_by_link_text(ClothingPageLocators.fiction_link).text
        assert fiction_link == "Fiction"

    def verify_menu_computers(self):
        computers_link = self.find_by_link_text(ClothingPageLocators.computers).text
        assert computers_link == "Computers in Literature"

    def verify_menu_non_fiction(self):
        non_fiction_link = self.find_by_link_text(ClothingPageLocators.non_fiction_link)
        assert non_fiction_link == "Non-Fiction"

    def verify_menu_programming(self):
        programming_link = self.find_by_link_text(ClothingPageLocators.programming_link)
        assert programming_link == "Essential programming"

    def verify_menu_hacking(self):
        hacking_link = self.find_by_link_text(ClothingPageLocators.hacking_link)
        assert hacking_link == "Hacking"

    def verify_image_product_link(self):
        image_product = self.find(ClothingPageLocators.product_image_link)
        assert image_product is not None, "Product image is presented"

    def press_image_product_link(self):
        image_press = self.find(ClothingPageLocators.product_image_link)
        image_press.click()

    def press_clothing_link(self):
        clothing_link = self.find(ClothingPageLocators.product_text_link)
        clothing_link.click()



