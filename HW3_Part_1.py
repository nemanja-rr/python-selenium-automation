from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(1)
# Find the most optimal locators for Create Account on amazon.com (Registration) page elements:

#Find amazon logo
driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo")

#Find create account title
driver.find_element(By.CSS_SELECTOR, ".a-spacing-small")

#Find your name input box
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

#Find mobile number or email input box
driver.find_element(By.CSS_SELECTOR, "#ap_email")

#Find password input box
driver.find_element(By.CSS_SELECTOR, "#ap_password")

#Find re-enter password input box
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

#Find continue button
driver.find_element(By.CSS_SELECTOR, "#continue")

#Find Privacy Notice Link
driver.find_element(By.CSS_SELECTOR, "[href*='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice']")

#Find Conditions of Use Link
driver.find_element(By.CSS_SELECTOR, "[href*='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use']")

#Find Sign in button
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")

