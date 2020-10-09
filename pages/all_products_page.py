from .base_page import BasePage
from .login_page import LoginPage

from .locators import AllProductsPageLocators


class AllProductsPage(BasePage):
    page_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, AllProductsPage.page_link)

    def verify_menu_clothing_link(self):
        clothing = self.find_by_link_text(AllProductsPageLocators.clothing_link).text
        assert clothing == "Clothing"

    def verify_menu_books_link(self):
        books_link = self.find_by_link_text(AllProductsPageLocators.books_link).text
        assert books_link == "Books"

    def verify_menu_fiction(self):
        fiction_link = self.find_by_link_text(AllProductsPageLocators.fiction_link).text
        assert fiction_link == "Fiction"

    def verify_menu_computers(self):
        computers_link = self.find_by_link_text(AllProductsPageLocators.computers).text
        assert computers_link == "Computers in Literature"

    def verify_menu_non_fiction(self):
        non_fiction_link = self.find_by_link_text(AllProductsPageLocators.non_fiction_link)
        assert non_fiction_link == "Non-Fiction"

    def verify_menu_programming(self):
        programming_link = self.find_by_link_text(AllProductsPageLocators.programming_link)
        assert programming_link == "Essential programming"

    def verify_menu_hacking(self):
        hacking_link = self.find_by_link_text(AllProductsPageLocators.hacking_link)
        assert hacking_link == "Hacking"




