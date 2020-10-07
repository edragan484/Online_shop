import math
from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage

from .locators import ProductPageLocators


class ProductPage(BasePage):
    page_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, ProductPage.page_link)

    def verify_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.product_name_on_product_page)
        product_name_text = product_name.text
        assert product_name_text == product_name.text, "Product name '%s' is '%s'" % (product_name, product_name_text)

    def add_to_basket(self):
        button_add_to_basket_from_product_page = self.browser.find_element(
            *ProductPageLocators.button_add_from_product_page)
        button_add_to_basket_from_product_page.click()

    def alert_of_add_product_from_product_page(self):
        button_add_to_basket_from_product_page = self.browser.find_element(
            *ProductPageLocators.button_add_from_product_page)
        button_add_to_basket_from_product_page.click()
        alert_of_add_product = self.browser.find_element(*ProductPageLocators.alert_of_add_product)
        assert "has been added to your basket." in alert_of_add_product % "Product has been added to your basket"

    def check_alert_of_add_on_product_page(self):
        product_name = self.browser.find_element(*ProductPageLocators.product_name_on_product_page)
        product_name_text = product_name.text
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.button_add_from_product_page)
        button_add_to_basket.click()
        alert_of_add_product = self.browser.find_element(*ProductPageLocators.alert_of_add_product)
        alert_of_add_product_text = alert_of_add_product.text
        assert product_name_text in alert_of_add_product_text, \
            "'%s' has been added to your basket." % product_name_text

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
