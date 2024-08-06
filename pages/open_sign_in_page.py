from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page

class OpenSignInPage(Page):
    # TC_LINK = (By.XPATH, "//a[@href='/c/terms-conditions/-/N-4sr7l']")-- DOES NOT WORK
    TC_LINK = (By.CSS_SELECTOR, 'div a[href*="/c/terms-conditions"][target="_blank"]')


    def open_sign_in(self):
        self.open_url('https://www.target.com/account?prehydrateClick=true')

    def click_tc_link(self):
        self.click(*self.TC_LINK)

# self.driver.find_elements(By.XPATH, "//h1[@text()='Terms & Conditions']")
