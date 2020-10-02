from pages.product_page import ProductPage

from pages.main_page import MainPage

from pages.base_page import BasePage

def add_to_basket(browser):
        promo_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, promo_link)
        page.open()
        page.should_be_product_name()
        page.add_to_basket()
        prompt = browser.switch_to.alert
        page.solve_quiz_and_get_code()
        prompt.send_keys(base_page.solve_quiz_and_get_code(y))
        prompt.accept()

        button_add_to_basket = self.browser.find_element(*ProductPageLocators.button_add_from_product_page)
        button_add_to_basket.click()
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        alert_x = str(x)
        y = str(math(log10(abs(12*sin(x))))
        prompt = self.browser.switch_to.alert
        prompt.send_keys(y)
        prompt.accept()
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        return str(alert_text)
