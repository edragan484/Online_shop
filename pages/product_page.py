from .base_page import BasePage

from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_name(self):
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
