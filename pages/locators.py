from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    language_field = (By.CSS_SELECTOR, "select[name='language']")
    language_italian = (By.CSS_SELECTOR, "[value='it']")
    language_deutsch = (By.CSS_SELECTOR, "[value='de']")
    button_change_language_submit = (By.CSS_SELECTOR, "button.btn.btn-default[type='submit']")
    all_products = (By.CSS_SELECTOR, "a.dropdown-toggle")
    basket = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    all_products_menu_link = (By.CSS_SELECTOR, ".dropdown-menu[data-navigation='dropdown-menu'] li:nth-child(1)")
    clothing_menu_link = (By.CSS_SELECTOR, ".dropdown-menu[data-navigation='dropdown-menu'] li:nth-child(3)")
    books_menu_link = (By.CSS_SELECTOR, ".dropdown-menu[data-navigation='dropdown-menu'] li:nth-child(4)")
    offers_menu_link = (By.CSS_SELECTOR, ".dropdown-menu[data-navigation='dropdown-menu'] li:nth-child(6)")
    search_field = (By.CSS_SELECTOR, "input[type='search']")
    button_search = (By.CSS_SELECTOR, "input[type='submit']")
    button_view_basket = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    basket_switch = (By.CSS_SELECTOR, "span.caret")
    basket_total_text = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs")
    shop_name = (By.CSS_SELECTOR, ".col-sm-7.h1 a")
    shop_subname = (By.CSS_SELECTOR, ".col-sm-7.h1 small")


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


class BasketPageLocators():
    page_name = (By.CSS_SELECTOR, "h1")
    basket_items = (By.CSS_SELECTOR, "div.basket-items")
    sum_price = (By.CSS_SELECTOR, "h3.price_color")
    button_proceed_to_checkout = (By.CSS_SELECTOR, "a.btn.btn-lg.btn-primary")
    free_shipping = (By.CSS_SELECTOR, "tr:nth-child(5) th.total.align-right")


class WhoAreYouPageLocators():
    email_field = (By.CSS_SELECTOR, "input[type='email']")
    checkbox1_guest = (By.CSS_SELECTOR, "div.radio [value='anonymous']")
    checkbox2_existing = (By.CSS_SELECTOR, "div.radio [value='existing']")
    password_field = (By.CSS_SELECTOR, "input[type='password']")
    checkbox3_new = (By.CSS_SELECTOR, "div.radio [value='new']")
    button_continue = (By.CSS_SELECTOR, "button[type='submit']")


class ShippingAddressPageLocators():
    new_address_form = (By.CSS_SELECTOR, ".well")
    address_form_existing = (By.CSS_SELECTOR, "div.well address")
    title_field = (By.CSS_SELECTOR, "select#id_title")
    first_name_field = (By.CSS_SELECTOR, "input[name='first_name']")
    last_name_field = (By.CSS_SELECTOR, "input[name='last_name']")
    address_field1 = (By.CSS_SELECTOR, "input[name='line1']")
    address_field2 = (By.CSS_SELECTOR, "input[name='line2']")
    address_field3 = (By.CSS_SELECTOR, "input[name='line3']")
    city_field = (By.CSS_SELECTOR, "input[name='line4']")
    state_field = (By.CSS_SELECTOR, "input[name='state']")
    postcode_field = (By.CSS_SELECTOR, "input[name='postcode']")
    county_field = (By.CSS_SELECTOR, "select[name='country']")
    phone_field = (By.CSS_SELECTOR, "input[name='phone_number']")
    textarea_field = (By.CSS_SELECTOR, "textarea[name='notes']")
    button_continue = (By.CSS_SELECTOR, "button[type='submit']")
    return_to_basket_link = (By.CSS_SELECTOR, ".col-sm-offset-4.col-sm-8 a")
    choose_address_button = (By.CSS_SELECTOR, "button[type='submit'].btn.ship-address")


class EnterPaymentDetailsPageLocators():
    page_name = (By.CSS_SELECTOR, "h1")
    paypal_payment = (By.CSS_SELECTOR, ".page_inner li:nth-child(1) a")
    datacash_payment = (By.CSS_SELECTOR, ".page_inner li:nth-child(2) a")
    button_continue = (By.CSS_SELECTOR, "a#view_preview")


class PreviewOrderPageLocators():
    address_review = (By.CSS_SELECTOR, ".well.well-info address")
    payment_review = (By.CSS_SELECTOR, ".well.well-success")
    basket_items_review = (By.CSS_SELECTOR, ".basket-items")
    button_place_order = (By.CSS_SELECTOR, "button#place-order")


class ConfirmationPageLocators():
    order_number_confirmation = (By.CSS_SELECTOR, "div.sub-header h1")
    address_review = (By.CSS_SELECTOR, ".well.well-info address")
    basket_items_review = (By.CSS_SELECTOR, ".basket-items")
    button_print_this_page = (By.CSS_SELECTOR, "div.col-sm-4:nth-child(1) a")
    button_continue_shopping = (By.CSS_SELECTOR, "div.col-sm-4:nth-child(2) a")
