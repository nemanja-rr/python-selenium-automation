from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')

sleep(1)

@when('Click on empty cart')
def click_cart(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()

sleep(1)

@then('Verify "Your cart is empty" message is shown')
def verify_cart_is_empty(context):
    context.driver.find_elements(By.XPATH, "//h1[@text()='Your cart is empty']")
