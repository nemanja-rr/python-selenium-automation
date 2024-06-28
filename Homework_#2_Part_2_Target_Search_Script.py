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
driver.get('https://www.target.com/')

sleep(2)

# click SignIn button
driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']").click()

sleep(2)

# click SignIn from side navigation
driver.find_element(By.ID, 'listaccountNav-signIn').click()

sleep(2)

# find by XPATH Privacy Notice Link
driver.find_elements(By.XPATH, "//class[@text()='Sign into your Target account']")

