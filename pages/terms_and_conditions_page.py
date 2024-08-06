from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page

# class TermsConditionsPage(Page):
#     def verify_tc(self):
#         self.verify_partial_url('/terms-conditions')

class TermsConditionsPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_partial_url(self):

        expected_url = "/terms-conditions"
        current_url = self.driver.current_url
        assert expected_url in current_url, f"Expected {expected_url} to be in {current_url}"
