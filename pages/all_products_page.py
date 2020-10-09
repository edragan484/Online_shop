from .base_page import BasePage

from .locators import AllProductsPageLocators


class AllProductsPage(BasePage):
    page_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, AllProductsPage.page_link)

    def verify_page_name(self):
        page_name = self.find(AllProductsPageLocators.page_name)
        assert page_name == "All Products", "'%s' is correct name name" % page_name

    def verify_menu_block(self):
        menu = self.find(AllProductsPageLocators.menu_block)
        assert menu is not None, "Block menu is present on the page"

    def verify_product_block(self):
        items_block = self.find(AllProductsPageLocators.items_block)
        assert items_block is not None, "Block menu is present on the page"

    def verify_menu_clothing_link(self):
        clothing = self.find_by_link_text(AllProductsPageLocators.clothing_link).text
        assert clothing == "Clothing", "'%s' is correct link name" % clothing

    def verify_menu_books_link(self):
        books_link = self.find_by_link_text(AllProductsPageLocators.books_link).text
        assert books_link == "Books", "'%s' is correct link name" % books_link

    def verify_menu_fiction(self):
        fiction_link = self.find_by_link_text(AllProductsPageLocators.fiction_link).text
        assert fiction_link == "Fiction", "'%s' is correct link name" % fiction_link

    def verify_menu_computers(self):
        computers_link = self.find_by_link_text(AllProductsPageLocators.computers).text
        assert computers_link == "Computers in Literature", "'%s' is correct link name" % computers_link

    def verify_menu_non_fiction(self):
        non_fiction_link = self.find_by_link_text(AllProductsPageLocators.non_fiction_link)
        assert non_fiction_link == "Non-Fiction", "'%s' is correct link name" % non_fiction_link

    def verify_menu_programming(self):
        programming_link = self.find_by_link_text(AllProductsPageLocators.programming_link)
        assert programming_link == "Essential programming", "'%s' is correct link name" % programming_link

    def verify_menu_hacking(self):
        hacking_link = self.find_by_link_text(AllProductsPageLocators.hacking_link)
        assert hacking_link == "Hacking", "'%s' is correct link name" % hacking_link
