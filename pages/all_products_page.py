from .base_page import BasePage

from .locators import AllProductsPageLocators
from .locators import LoginPageLocators
from .locators import MainPageLocators


class AllProductsPage(BasePage):
    product_item1 = "Coders at Work"
    page_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, AllProductsPage.page_link)

    def verify_page_name(self):
        page_name = self.find(AllProductsPageLocators.page_name).text
        assert page_name == "All products", "'%s' is correct name" % page_name

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
        non_fiction_link = self.find_by_link_text(AllProductsPageLocators.non_fiction_link).text
        assert non_fiction_link == "Non-Fiction", "'%s' is correct link name" % non_fiction_link

    def verify_menu_programming(self):
        programming_link = self.find_by_link_text(AllProductsPageLocators.programming_link).text
        assert programming_link == "Essential programming", "'%s' is correct link name" % programming_link

    def verify_menu_hacking(self):
        hacking_link = self.find_by_link_text(AllProductsPageLocators.hacking_link).text
        assert hacking_link == "Hacking", "'%s' is correct link name" % hacking_link

    def press_basket_link(self):
        basket = self.find(AllProductsPageLocators.basket)
        basket.click()

    def verify_login_link(self):
        login = self.find(AllProductsPageLocators.login_button).text
        assert login == "Login or register", "'%s' button is correct" % login

    def press_login_link(self):
        login = self.find(AllProductsPageLocators.login_button)
        login.click()

    def verify_account_icon(self):
        account_icon = self.find(AllProductsPageLocators.account_icon)
        assert account_icon is not None, "Account link is presented"

    def verify_account_link(self):
        account = self.find_by_link_text(AllProductsPageLocators.account).text
        assert account == "Account", "'%s' is correct button" % account

    def press_account_icon(self):
        account_icon = self.find(AllProductsPageLocators.account_icon)
        account_icon.click()

    def press_account_link(self):
        account = self.find_by_link_text(AllProductsPageLocators.account)
        account.click()

    def verify_logout_link(self):
        logout = self.find(AllProductsPageLocators.logout_button).text
        assert logout == "Logout", "'%s' is correct button" % logout

    def press_logout_link(self):
        logout = self.find(AllProductsPageLocators.logout_button)
        logout.click()

    def change_language_to_it(self):
        language1 = self.find(AllProductsPageLocators.language_field)
        language1.click()
        language1 = self.find(AllProductsPageLocators.language_italian)
        language1.click()
        button_language = self.find(AllProductsPageLocators.button_change_language_submit)
        button_language.click()

    def verify_change_language_to_it(self, menu_it, basket_it):
        all_products_button = self.find(AllProductsPageLocators.browse_store_button)
        assert menu_it == all_products_button.text, "Translate is correct"
        basket_button = self.find(AllProductsPageLocators.basket)
        assert basket_it == basket_button.text, "Translate is correct"

    def verify_item_link(self, product_item1):
        item = self.find_by_link_text(AllProductsPage.product_item1).text
        assert item == product_item1, "'%s' is correct name" % item

    def press_item_link(self):
        item = self.find_by_link_text(AllProductsPage.product_item1)
        item.click()

    def press_item_image(self):
        item_image = self.find(AllProductsPageLocators.product_image_link)
        item_image.click()

    def add_to_basket_button(self):
        add_to_basket = self.find_by_xpath(AllProductsPageLocators.add_to_button_item)
        add_to_basket.click()

    def verify_alert1_of_add_to_basket(self):
        alert1 = self.find_by_xpath(AllProductsPageLocators.alert1).text
        assert "has been added to your basket" in alert1, "Item in basket"

    def verify_alert2_of_add_to_basket(self):
        alert2 = self.find_by_xpath(AllProductsPageLocators.alert2).text
        assert "offer" in alert2, "Alert about offer"

    def verify_alert3_of_add_to_basket(self):
        alert3 = self.find_by_xpath(AllProductsPageLocators.alert3).text
        assert "Your basket total is now" in alert3, "Alert about total prise in basket"

    def press_view_basket_from_alert(self):
        basket_alert = self.find_by_link_text(AllProductsPageLocators.view_basket_from_alert)
        basket_alert.click()

    def press_checkout_from_alert(self):
        checkout_alert = self.find_by_link_text(AllProductsPageLocators.checkout_in_alert)
        checkout_alert.click()

    def verify_next_button(self):
        next_button = self.find(AllProductsPageLocators.button_next).text
        assert next_button == "next", "Button '%s' is correct" % next_button

    def press_next_button(self):
        next_button = self.find(AllProductsPageLocators.button_next)
        next_button.click()

    def user_in_system(self):
        login = self.find(AllProductsPageLocators.login_button)
        login.click()
        login_page_email = self.find(LoginPageLocators.email_login)
        login_page_email.send_keys("user2020@gmail.com")
        login_page_pass = self.find(LoginPageLocators.password_login)
        login_page_pass.send_keys("QRTYvvbbnmYU")
        enter_button = self.find(LoginPageLocators.button_login)
        enter_button.click()
        all_products = self.find(MainPageLocators.all_products_menu_link)
        all_products.click()



