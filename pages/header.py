from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGN_IN_BTN = (By.XPATH, "//a[@aria-label='Account, sign in']")
    VERIFY_FORM_OPENED_FROM_RIGHT_SIDE = (By.ID, 'listaccountNav-signIn')
    ADD_TO_CART = (By.ID, 'addToCartButtonOrTextIdFor79832816')

    def search(self):
        self.input_text('pikachu sleeping', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        # wait for the page with search results to load
        sleep(6)

    def add_to_cart(self):
        self.wait_and_click(*self.ADD_TO_CART)
    def sign_in(self):
        self.click(*self.SIGN_IN_BTN)