from .base_page import BasePage
from .login_page import LoginPage

from .locators import MainPageLocators
from .locators import LoginPageLocators


class MainPage(BasePage):
    main_page = "http://selenium1py.pythonanywhere.com/en-gb/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, MainPage.main_page)

    def verify_site_name(self):
        site_name = self.find(MainPageLocators.shop_name).text
        assert site_name == "Oscar", "Shop name is '%s'" % site_name

    def verify_site_subname(self):
        site_subname = self.find(MainPageLocators.shop_subname).text
        assert site_subname == "Sandbox", "Shop subname is '%s'" % site_subname

    def go_to_login_page(self):
        login_link = self.find(MainPageLocators.login_page_link)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def verify_login_link(self):
        login_link = self.find(MainPageLocators.login_page_link)
        assert login_link, "Login link is not presented"

    def verify_account_icon_link(self):
        icon_link = self.find(MainPageLocators.icon_link)
        assert icon_link is not None

    def change_language_to_it(self):
        language1 = self.find(MainPageLocators.language_field)
        language1.click()
        language1 = self.find(MainPageLocators.language_italian)
        language1.click()
        button_language = self.find(MainPageLocators.button_change_language_submit)
        button_language.click()

    def change_language_to_deutsch(self):
        language2 = self.find(MainPageLocators.language_field)
        language2.click()
        language2 = self.find(MainPageLocators.language_deutsch)
        language2.click()
        button_language = self.find(MainPageLocators.button_change_language_submit)
        button_language.click()

    def verify_menu_and_basket_text_in_it(self):
        all_products_button = self.find(MainPageLocators.all_products)
        assert "Naviga nel negozio" == all_products_button.text, "Translate is correct"
        basket_button = self.find(MainPageLocators.basket)
        assert "Visualizza carrello" == basket_button.text, "Translate is correct"

    def verify_menu_and_basket_text_in_deutsch(self):
        all_products_button = self.find(MainPageLocators.all_products)
        assert "Im Webshop stöbern" == all_products_button.text, "Translate is correct"
        basket_button = self.find(MainPageLocators.basket)
        assert "Warenkorb anzeigen" == basket_button.text, "Translate is correct"

    def verify_another_method_deutsch(self, menu_deutsch, basket_deutsch):
        all_products_button = self.find(MainPageLocators.all_products)
        assert menu_deutsch == all_products_button.text, "Translate is correct"
        basket_button = self.find(MainPageLocators.basket)
        assert basket_deutsch == basket_button.text, "Translate is correct"

    def verify_welcome_success_alert(self):
        alert_welcome = self.find(MainPageLocators.alert_welcome_user).text
        assert alert_welcome is not None

    def verify_all_products_button_menu(self):
        all_products_button = self.find(MainPageLocators.all_products_menu_link)
        assert all_products_button is not None, "Button '%s' is presented on page" % all_products_button

    def go_to_all_products_button_menu(self):
        all_products_button = self.find(MainPageLocators.all_products_menu_link)
        all_products_button.click()

    def verify_clothing_button_menu(self):
        clothing_button = self.find(MainPageLocators.clothing_menu_link)
        assert clothing_button is not None, "Button '%s' is presented on page" % clothing_button

    def go_to_clothing_button_menu(self):
        clothing_button = self.find(MainPageLocators.clothing_menu_link)
        clothing_button.click()

    def verify_books_button_menu(self):
        books_button = self.find(MainPageLocators.books_menu_link)
        assert books_button is not None, "Button '%s' is presented on page" % books_button

    def go_to_books_button_menu(self):
        books_button = self.find(MainPageLocators.books_menu_link)
        books_button.click()

    def verify_offers_button_menu(self):
        offers_button = self.find(MainPageLocators.offers_menu_link)
        assert offers_button is not None, "Button '%s' is presented on page" % offers_button

    def go_to_offers_button_menu(self):
        offers_button = self.find(MainPageLocators.offers_menu_link)
        offers_button.click()

    def verify_basket_view_button(self):
        basket_view_button = self.find(MainPageLocators.basket)
        assert basket_view_button is not None, "Button '%s' is presented on page" % basket_view_button

    def go_to_basket_view_button(self):
        basket_view_button = self.find(MainPageLocators.basket)
        basket_view_button.click()

    def go_to_basket_menu_button(self):
        basket_menu_button = self.find(MainPageLocators.basket_switch)
        basket_menu_button.click()

    def searching_item(self, product_name):
        search_field_text = self.find(MainPageLocators.search_field)
        search_field_text.send_keys(product_name)
        push_search_button = self.find(MainPageLocators.button_search)
        push_search_button.click()

    def verify_search_items_is_correct(self, product_name1):
        found_item = self.find(MainPageLocators.item_found)
        assert found_item is not None, "Item '%s' is found in searching"

        found_item_name = self.find(MainPageLocators.item_found_name_link).text
        assert found_item_name == product_name1, \
            "Found item name '%s' is correct as '%s'" % (found_item_name, product_name1)

    def verify_image_found_item_is_correct(self, product_name1):
        item_image = self.find(MainPageLocators.image_found_item)
        assert item_image is not None, "Item image is on the page"
        assert product_name1 == item_image.get_attribute("alt"), \
            "Item should contain image with correct alt, but it doesn't"

    def verify_menu_block(self):
        menu_block = self.find(MainPageLocators.menu_block)
        assert menu_block is not None, "Menu block is presented on page"

    def verify_welcome_block(self):
        welcome_block = self.find(MainPageLocators.welcome_block)
        assert welcome_block is not None, "Welcome block is on the page"
        welcome_article = self.find(MainPageLocators.welcome_name_article).text
        assert welcome_article == "Welcome!", "'%s' is correct name of article" % welcome_article

    def verify_recommended_reading_block(self):
        recommended_reading = self.find(MainPageLocators.recommended_reading_block)
        assert recommended_reading is not None, "'%s' is on the page" % recommended_reading
        recommended_reading_article = self.find(MainPageLocators.recommended_reading_article).text
        assert recommended_reading_article == "Recommended reading", \
            "'%s' is correct name of article" % recommended_reading_article

    def verify_other_good_books_block(self):
        other_books_block = self.find(MainPageLocators.other_good_books_block)
        assert other_books_block is not None, "'%s' is on the page" % other_books_block
        other_books_article = self.find(MainPageLocators.other_good_books_article).text
        assert other_books_article == "Other good books", "'%s' is correct name of article " % other_books_article

    def add_to_basket_from_main_page(self):
        add_to_basket_button = self.find_by_xpath(MainPageLocators.add_item_to_basket_button)
        add_to_basket_button.click()

    def press_basket_button(self):
        press_button = self.find(MainPageLocators.basket)
        press_button.click()

    def verify_alert_of_add_item_to_basket(self):
        alert1 = self.find_by_xpath(MainPageLocators.alert1_of_add).text
        assert "has been added to your basket." in alert1, "Alert of adding item to basket"

    def verify_alert_of_offer(self):
        alert2 = self.find_by_xpath(MainPageLocators.alert2_of_offer).text
        assert "offer" in alert2

    def verify_alert_basket_total(self):
        alert3 = self.find(MainPageLocators.alert3_of_add).text
        assert "Your basket total is now" in alert3, "Alert of total prise in basket"

    def verify_view_basket_button_in_alert(self):
        alert_basket = self.find(MainPageLocators.view_basket_in_alert).text
        assert "View basket" == alert_basket, "'%s' is in alert"

    def verify_checkout_in_alert(self):
        checkout_alert = self.find(MainPageLocators.checkout_now_in_alert).text
        assert "Checkout now" == checkout_alert, "'%s' is in alert"

    def go_to_basket_from_alert(self):
        alert_basket = self.find(MainPageLocators.view_basket_in_alert)
        alert_basket.click()

    def go_to_checkout_from_alert(self):
        checkout_alert = self.find(MainPageLocators.checkout_now_in_alert)
        checkout_alert.click()

    def go_to_product_page_from_product_name_link(self):
        product_page_link = self.find(MainPageLocators.item_name_link)
        product_page_link.click()

    def go_to_product_page_from_product_name_image(self):
        product_page_image = self.find(MainPageLocators.item_name_image)
        product_page_image.click()

    def go_to_basket_page(self):
        go_to_basket = self.find(MainPageLocators.basket)
        go_to_basket.click()

    def user_in_system(self):
        login = self.find(MainPageLocators.login_page_link)
        login.click()
        login_page_email = self.find(LoginPageLocators.email_login)
        login_page_email.send_keys("user2020@gmail.com")
        login_page_pass = self.find(LoginPageLocators.password_login)
        login_page_pass.send_keys("QRTYvvbbnmYU")
        enter_button = self.find(LoginPageLocators.button_login)
        enter_button.click()





