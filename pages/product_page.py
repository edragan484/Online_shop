
from .base_page import BasePage
from .locators import ProductPageLocators, LoginPageLocators, MainPageLocators


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

    def verify_login_link(self):
        login_link = self.find(ProductPageLocators.login_link).text
        assert login_link == "Login or register", "'%s' is correct" % login_link

    def verify_logout_link(self):
        logout_link = self.find(ProductPageLocators.logout_link).text
        assert logout_link == "Logout", "'%s' is correct" % logout_link

    def go_to_login_page(self):
        login_link = self.find(ProductPageLocators.login_link)
        login_link.click()

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
        alert_of_add_product = self.find(ProductPageLocators.alert_of_add_product).text
        assert "has been added to your basket." in alert_of_add_product, \
            "'%s' has been added to your basket." % ProductPage.product_name

    def press_basket_button(self):
        basket = self.find(ProductPageLocators.basket)
        basket.click()

    def press_view_basket_in_alert(self):
        view_basket = self.find_by_link_text(ProductPageLocators.basket_in_alert)
        view_basket.click()

    def press_checkout_in_alert(self):
        checkout_in_alert = self.find_by_link_text(ProductPageLocators.checkout_in_alert)
        checkout_in_alert.click()

    def user_in_system(self):
        login = self.find(ProductPageLocators.login_link)
        login.click()
        login_page_email = self.find(LoginPageLocators.email_login)
        login_page_email.send_keys("user2020@gmail.com")
        login_page_pass = self.find(LoginPageLocators.password_login)
        login_page_pass.send_keys("QRTYvvbbnmYU")
        enter_button = self.find(LoginPageLocators.button_login)
        enter_button.click()
        product_page = self.find(MainPageLocators.item_name_link1)
        product_page.click()

    def logout(self):
        logout = self.find(ProductPageLocators.logout_link)
        logout.click()

