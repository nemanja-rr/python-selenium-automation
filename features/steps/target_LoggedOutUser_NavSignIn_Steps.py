from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target landing page')
def open_target(context):
    context.app.main_page.open()
    # context.driver.get('https://www.target.com/')
    sleep(1)

@when('Click on Sign In Button')
def click_signin_button(context):
    context.app.header.sign_in()
    # context.driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']").click()
    sleep(1)

@then('Verify Sign In form opened from right side navigation menu')
def verify_signin_form_opened_from_right_side_panel(context):
    context.driver.find_element(By.ID, 'listaccountNav-signIn').click()
    sleep(1)
    context.driver.find_elements(By.XPATH, "//h1[@text()='Sign into your Target account']")

