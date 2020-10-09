from .base_page import BasePage

from .locators import BooksPage2Locators


class BooksPage2(BasePage):
    page_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/category/books_2/?page=2"

    def __init__(self, browser):
        BasePage.__init__(self, browser, BooksPage2.page_link)

    def verify_page_name(self):
        page_name = self.find(BooksPage2Locators.page_name)
        assert page_name == "Books", "'%s' is correct page name" % page_name

    def verify_next_button(self):
        next_button = self.find(BooksPage2Locators.next_button).text
        assert next_button == "next", "Button '%s' is presented on page" % next_button

    def press_previous_button(self):
        previous_button = self.find(BooksPage2Locators.button_previous)
        previous_button.click()
