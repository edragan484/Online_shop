from selenium.webdriver.common.by import By


class MainPageLocators:
    login_page_link = "#login_link"
    language_field = "select[name='language']"
    language_italian = "[value='it']"
    language_deutsch = "[value='de']"
    button_change_language_submit = "button.btn.btn-default[type='submit']"
    all_products = "a.dropdown-toggle"
    basket = "span.btn-group a.btn.btn-default"
    all_products_menu_link = ".dropdown-menu[data-navigation='dropdown-menu'] li:nth-child(1)"
    clothing_menu_link = ".dropdown-menu[data-navigation='dropdown-menu'] li:nth-child(3)"
    books_menu_link = ".dropdown-menu[data-navigation='dropdown-menu'] li:nth-child(4)"
    offers_menu_link = ".dropdown-menu[data-navigation='dropdown-menu'] li:nth-child(6)"
    search_field = "input[type='search']"
    button_search = "input[type='submit']"
    button_view_basket = ".btn-group a.btn.btn-default"
    basket_switch = "span.caret"
    basket_total_text = ".basket-mini.pull-right.hidden-xs"
    shop_name = ".col-sm-7.h1 a"
    shop_subname = ".col-sm-7.h1 small"
    alert_welcome_user = "div.alert.alert-success"
    item_found = ".product_pod"
    item_found_name = "h3 a"
    image_found_item = ".image_container img"
    welcome_block = "section.well.well-blank:nth-child(1)"
    welcome_name_article = "section.well.well-blank h2"
    recommended_reading_block = ".well.promotion_single"
    recommended_reading_article = ".well.promotion_single h2"
    other_good_books_block = "section.well.well-blank:nth-child(3)"
    other_good_books_article = "div.sub-header h3"
    add_item_to_basket_button = "Add to basket"
    alert1_of_add = "//body/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]"
    alert2_of_offer = "//body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]"
    alert3_of_add = "div.alert.alert-info"
    view_basket_in_alert = "div.alertinner p a:nth-child(1)"
    checkout_now_in_alert = "div.alertinner p a:nth-child(2)"
    item_name_link = "a[title='The City and the Stars']"


class LoginPageLocators:
    login_page_button = "div.page_inner li.active"
    login_url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    login_form = "should_be_login_form"
    register_form = "div.col-sm-6.register_form"
    email_registration_field = "input[name='registration-email']"
    password_registration_field = "input[name='registration-password1']"
    password_confirmation_field = "input[name='registration-password2']"
    button_submit_registration = "button[name='registration_submit']"
    email_login = "input[name='login-username']"
    password_login = "input[name='login-password']"
    button_login = "button[name='login_submit']"
    recover_password_link = "form#login_form a"


class UserPageLocators:
    registration_alert = "div#messages"
    link_to_account = "a i.icon-user"
    logout_link = "a#logout_link"
    profile_link_in_menu = ".nav.nav-pills.nav-stacked li:nth-child(1)"
    order_history_link_in_menu = ".nav.nav-pills.nav-stacked li:nth-child(2)"
    address_book_link_in_menu = ".nav.nav-pills.nav-stacked li:nth-child(3)"
    email_history_link_in_menu = ".nav.nav-pills.nav-stacked li:nth-child(4)"
    product_alerts_link_in_menu = ".nav.nav-pills.nav-stacked li:nth-child(5)"
    notification_link_in_menu = ".nav.nav-pills.nav-stacked li:nth-child(6)"
    wish_lists_link_in_menu = ".nav.nav-pills.nav-stacked li:nth-child(7)"


class ProductPageLocators:
    button_add_from_product_page = "button[type='submit'].btn.btn-lg.btn-primary.btn-add-to-basket"
    product_name_on_product_page = "h1"
    alert_of_add_product = "div.alert.alert-safe.alert-noicon:nth-child(1)"
    name_in_alert_add_product = "div.alert.alert-safe.alert-noicon:nth-child(1) strong"


class PasswordResetPageLocators:
    email_field = "input[name='email']"
    send_reset_email_button = "button.btn.btn-primary.btn-lg"
    alert_reset = "div#content_inner"


class BasketPageLocators:
    page_name = "h1"
    basket_items = "div.basket-items"
    sum_price = "h3.price_color"
    button_proceed_to_checkout = "a.btn.btn-lg.btn-primary"
    free_shipping = "tr:nth-child(5) th.total.align-right"


class WhoAreYouPageLocators:
    email_field = "input[type='email']"
    checkbox1_guest = "div.radio [value='anonymous']"
    checkbox2_existing = "div.radio [value='existing']"
    password_field = "input[type='password']"
    checkbox3_new = "div.radio [value='new']"
    button_continue = "button[type='submit']"


class ShippingAddressPageLocators:
    new_address_form = ".well"
    address_form_existing = "div.well address"
    title_field = "select#id_title"
    first_name_field = "input[name='first_name']"
    last_name_field = "input[name='last_name']"
    address_field1 = "input[name='line1']"
    address_field2 = "input[name='line2']"
    address_field3 = "input[name='line3']"
    city_field = "input[name='line4']"
    state_field = "input[name='state']"
    postcode_field = "input[name='postcode']"
    county_field = "select[name='country']"
    phone_field = "input[name='phone_number']"
    textarea_field = "textarea[name='notes']"
    button_continue = "button[type='submit']"
    return_to_basket_link = ".col-sm-offset-4.col-sm-8 a"
    choose_address_button = "button[type='submit'].btn.ship-address"


class EnterPaymentDetailsPageLocators:
    page_name = "h1"
    paypal_payment = ".page_inner li:nth-child(1) a"
    datacash_payment = ".page_inner li:nth-child(2) a"
    button_continue = "a#view_preview"


class PreviewOrderPageLocators:
    address_review = ".well.well-info address"
    payment_review = ".well.well-success"
    basket_items_review = ".basket-items"
    button_place_order = "button#place-order"


class ConfirmationPageLocators:
    order_number_confirmation = "div.sub-header h1"
    address_review = ".well.well-info address"
    basket_items_review = ".basket-items"
    button_print_this_page = "div.col-sm-4:nth-child(1) a"
    button_continue_shopping = "div.col-sm-4:nth-child(2) a"
