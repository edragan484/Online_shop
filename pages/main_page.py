from .base_page import BasePage
from .login_page import LoginPage

from .locators import MainPageLocators


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

    def verify_welcome_success_alert(self):
        alert_welcome = self.find(MainPageLocators.alert_welcome_user).text
        assert alert_welcome is not None

    def go_to_all_products_button_menu(self):
        all_products_button = self.find(MainPageLocators.all_products)
        all_products_button.click()

    def go_to_clothing_button_menu(self):
        clothing_button = self.find(MainPageLocators.clothing_menu_link)
        clothing_button.click()

    def go_to_books_button_menu(self):
        books_button = self.find(MainPageLocators.books_menu_link)
        books_button.click()

    def go_to_offers_button_menu(self):
        offers_button = self.find(MainPageLocators.offers_menu_link)
        offers_button.click()

    def go_to_basket_view_button(self):
        basket_view_button = self.find(MainPageLocators.basket)
        basket_view_button.click()

    def go_to_basket_menu_button(self):
        basket_menu_button = self.find(MainPageLocators.basket_switch)
        basket_menu_button.click()

    def searching_item(self):
        search_field_text = self.find(MainPageLocators.search_field)
        search_field_text.send_keys("The City and the Stars")
        push_search_button = self.find(MainPageLocators.button_search)
        push_search_button.click()

    def verify_search_items_is_correct(self):
        found_item = self.find(MainPageLocators.item_found)
        assert found_item is not None, "Item '%s' is found in searching" % found_item

        found_item_name = self.find(MainPageLocators.item_found_name).text
        search_field_text = self.find(MainPageLocators.search_field).text
        assert found_item_name == search_field_text, "Found items '%s' name is correct" % found_item_name

        item_image = self.find(MainPageLocators.image_found_item)
        assert item_image is not None, "Item image is on the page"
        assert search_field_text in item_image.get_attribute("alt"), \
            "Item should contain image with correct alt, but it doesn't"
        item_desc = MainPage.find(MainPageLocators.item_found_name)
        assert search_field_text in item_desc.text, "Search result should contain searching string in its text"

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

    def verify_alert_of_add_item_to_basket(self):
        alert1 = self.find_by_xpath(MainPageLocators.alert1_of_add).text
        assert "has been added to your basket." in alert1, "Alert of adding item to basket"

    def verify_alert_of_offer(self):
        alert2 = self.find_by_xpath(MainPageLocators.alert2_of_offer).text
        assert "offer" in alert2

    def verify_alert_basket_total(self):
        alert3 = self.find_by_xpath(MainPageLocators.alert3_of_add).text
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


    def go_to_product_page_from_main_page(self):
        item_name_link = self.find(MainPageLocators.item_name_link)
        item_name_link.click()
