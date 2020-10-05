from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    language_field = (By.CSS_SELECTOR, "select[name='language']")
    language_italian = (By.CSS_SELECTOR, "[value='it']")
    language_deutsch = (By.CSS_SELECTOR, "[value='de']")
    button_change_language_submit = (By.CSS_SELECTOR, "button.btn.btn-default[type='submit']")
    all_products = (By.CSS_SELECTOR, "a.dropdown-toggle")
    basket = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")


class LoginPageLocators():
    should_be_login_page = (By.CSS_SELECTOR, "div.page_inner li.active")
    should_be_login_url = (By.LINK_TEXT, "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
    should_be_login_form = (By.CSS_SELECTOR, "should_be_login_form")
    should_be_register_form = (By.CSS_SELECTOR, "div.col-sm-6.register_form")
    email_registration_field = (By.CSS_SELECTOR, "input[name='registration-email']")
    password_registration_field = (By.CSS_SELECTOR, "input[name='registration-password1']")
    password_confirmation_field = (By.CSS_SELECTOR, "input[name='registration-password2']")
    button_submit_registration = (By.CSS_SELECTOR, "button[name='registration_submit']")
    email_login = (By.CSS_SELECTOR, "input[name='login-username']")
    password_login = (By.CSS_SELECTOR, "input[name='login-password']")
    button_login = (By.CSS_SELECTOR, "button[name='login_submit']")
    recover_password_link = (By.CSS_SELECTOR, "form#login_form a")


class UserPageLocators():
    registration_alert = (By.CSS_SELECTOR, "div#messages")
    link_to_account = (By.CSS_SELECTOR, "a i.icon-user")
    logout_link = (By.CSS_SELECTOR, "a#logout_link")
    profile_link_in_menu = (By.CSS_SELECTOR, ".nav.nav-pills.nav-stacked li:nth-child(1)")
    order_history_link_in_menu = (By.CSS_SELECTOR, ".nav.nav-pills.nav-stacked li:nth-child(2)")
    address_book_link_in_menu = (By.CSS_SELECTOR, ".nav.nav-pills.nav-stacked li:nth-child(3)")
    email_history_link_in_menu = (By.CSS_SELECTOR, ".nav.nav-pills.nav-stacked li:nth-child(4)")
    product_alerts_link_in_menu = (By.CSS_SELECTOR, ".nav.nav-pills.nav-stacked li:nth-child(5)")
    notification_link_in_menu = (By.CSS_SELECTOR, ".nav.nav-pills.nav-stacked li:nth-child(6)")
    wish_lists_link_in_menu = (By.CSS_SELECTOR, ".nav.nav-pills.nav-stacked li:nth-child(7)")


class ProductPageLocators():
    button_add_from_product_page = (By.CSS_SELECTOR, "button[type='submit'].btn.btn-lg.btn-primary.btn-add-to-basket")
    product_name_on_product_page = (By.TAG_NAME, "h1")
    alert_of_add_product = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon:nth-child(1)")
    name_in_alert_add_product = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon:nth-child(1) strong")


class PasswordResetPageLocators():
    email_field = (By.CSS_SELECTOR, "input[name='email']")
    send_reset_email_button = (By.CSS_SELECTOR, "button.btn.btn-primary.btn-lg")
    alert_reset = (By.CSS_SELECTOR, "div#content_inner")