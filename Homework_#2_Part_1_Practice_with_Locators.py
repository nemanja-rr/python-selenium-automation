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
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

# find by ID
# driver.find_element(By.ID, '')
sleep(2)
# find by XPATH Amazon Logo
driver.find_element(By.XPATH, "//a[@class='a-link-nav-icon']")

# find by XPATH Email Field
driver.find_element(By.XPATH, "//input[@type='email']")

# find by ID Continue Button
driver.find_element(By.ID, 'continue')

# find by XPATH Privacy Notice Link
driver.find_elements(By.XPATH, "//a[@text()='Privacy Notice']")

# find by XPATH Conditions of Use Link
driver.find_elements(By.XPATH, "//a[@text()='Conditions of Use']")

# find by XPATH Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# find by ID Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

# find by ID Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

# find by ID Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')

