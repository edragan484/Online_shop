from .base_page import BasePage

from .locators import BooksPageLocators


class BooksPage(BasePage):
    page_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/category/books_2/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, BooksPage.page_link)

    def verify_page_name(self):
        page_name = self.find(BooksPageLocators.page_name)
        assert page_name == "Books", "'%s' is correct page name" % page_name

    def verify_menu_block(self):
        menu = self.find(BooksPageLocators.menu_block)
        assert menu is not None, "Block menu is present on the page"

    def verify_product_block(self):
        clothing = self.find(BooksPageLocators.product_block)
        assert clothing is not None, "Block menu is present on the page"

    def press_image_book(self):
        image_book = self.find(BooksPageLocators.product_image_link)
        image_book.click()

    def press_book_link(self):
        book_link = self.find(BooksPageLocators.product_link)
        book_link.click()

    def press_add_to_basket_button(self):
        add_to_basket = self.find(BooksPageLocators.add_to_basket_button)
        add_to_basket.click()

    def press_next_button(self):
        next_button = self.find(BooksPageLocators.next_button)
        next_button.click()



