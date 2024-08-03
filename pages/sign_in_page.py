from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_BTN = (By.XPATH, "//a[@aria-label='Account, sign in']")

    def verify_car_page(self):
        actual_page = self.driver.find_elements(By.XPATH, "//h1[@text()='Sign into your Target account']")
