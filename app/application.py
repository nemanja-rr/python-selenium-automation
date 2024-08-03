from pages.cart_checkout_page import CartCheckoutPage
from pages.header import Header
from pages.main_page import MainPage
from pages.base_page import Page
from pages.search_results_page import SearchResultsPage
from selenium.webdriver.support.wait import WebDriverWait

from pages.sign_in_page import SignInPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_page = SearchResultsPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.cart_checkout_page = CartCheckoutPage(driver)