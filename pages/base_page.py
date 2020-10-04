from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def find(self, locator):
        return self.browser.find_element_by_css_selector(locator)

    def find_all(self, locator):
        return self.browser.find_elements_by_css_selector(locator)

    def find_by_xpath(self, locator):
        return self.browser.find_element_by_xpath(locator)

    @staticmethod
    def find_in_element(parent, locator):
        return parent.find_elements_by_css_selector(locator)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
