from .base_page import BasePage

from .locators import ShippingAddressPageLocators


class ShippingAddressPage(BasePage):
    page_link = "http://selenium1py.pythonanywhere.com/en-gb/checkout/shipping-address/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, ShippingAddressPage.page_link)

    def verify_name_page(self):
        page_name = self.find(ShippingAddressPageLocators.page_name)
        assert page_name == "Shipping address", "'%s' is correct name page"

    def verify_new_shipping_form(self):
        shipping_form = self.find(ShippingAddressPageLocators.new_address_form)
        assert shipping_form is not None, "Shipping form is on page"

    def fill_shipping_title(self):
        title_tag = self.find_by_tag_name(ShippingAddressPageLocators.title_name_tag)
        title_tag.click()
        title_value = self.find_by_value(ShippingAddressPageLocators.title_value)
        title_value.click()

    def fill_first_name(self):
        first_name = self.find(ShippingAddressPageLocators.first_name_field)
        first_name.send_keys("Elena")

    def fill_last_name(self):
        last_name = self.find(ShippingAddressPageLocators.last_name_field)
        last_name.send_keys("Dragan")

    def fill_address1(self):
        address1 = self.find(ShippingAddressPageLocators.address_field1)
        address1.send_keys("1776 Hankock avenue")

    def fill_address2(self):
        address1 = self.find(ShippingAddressPageLocators.address_field2)
        address1.send_keys("San Jose")

    def fill_address3(self):
        address1 = self.find(ShippingAddressPageLocators.address_field3)
        address1.send_keys("California")

    def fill_city(self):
        city = self.find(ShippingAddressPageLocators.city_field)
        city.send_keys("San Jose")

    def fill_state(self):
        state = self.find(ShippingAddressPageLocators.state_field)
        state.send_keys("CA")

    def fill_zip(self):
        zipcode = self.find(ShippingAddressPageLocators.postcode_field)
        zipcode.send_keys("95123")

    def fill_country(self):
        self.find_by_tag_name(ShippingAddressPageLocators.country_field)
        self.find_by_value("United States")

    def fill_phone(self):
        phone_number = self.find(ShippingAddressPageLocators.phone_field)
        phone_number.send_keys("+14068049090")

    def fill_instructions_field(self):
        instructions = self.find(ShippingAddressPageLocators.textarea_field)
        instructions.send_keys("Hello, Oscar!")

    def push_button_continue(self):
        continue_button = self.find(ShippingAddressPageLocators.button_continue)
        continue_button.click()

    def push_return_to_basket(self):
        return_to_basket = self.find(ShippingAddressPageLocators.return_to_basket_link)
        return_to_basket.click()



