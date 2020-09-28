from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    should_be_login_page = (By.CSS_SELECTOR, "div.page_inner li.active")
    should_be_login_url = (By.LINK_TEXT, "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
    should_be_login_form = (By.CSS_SELECTOR, "should_be_login_form")
    should_be_register_form = (By.CSS_SELECTOR, "div.col-sm-6.register_form")


class ProductPageLocators():
    button_add_from_product_page = (By.CSS_SELECTOR, "button[type='submit'].btn.btn-lg.btn-primary.btn-add-to-basket")
    product_name_on_product_page = (By.TAG_NAME, "h1")
    alert_of_add_product = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon:nth-child(1)")
    name_in_alert_add_product = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon:nth-child(1) strong")
