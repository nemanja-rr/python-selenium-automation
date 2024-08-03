from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page


class CartCheckoutPage(Page):
    VERIFY_CART_PAGE = (By.XPATH, "//div[@data-test='cartItem-title']")

    def verify_text(self):
        actual_item = self.driver.find_elements(By.XPATH, "//h1[@text()='Sign into your Target account']")
