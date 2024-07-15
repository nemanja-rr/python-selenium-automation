from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')
    sleep(4)

@when ('Page fully loads all sections')
def circle_page_is_loaded(context):
    context.driver.find_elements(By.XPATH, "//span[@text()='Meet the new Target Circle']")
    #page has fully loaded

@then ('Verify green section has 6 benefit cells')
def green_benefit_cells_are_verified(context):
    context.driver.find_elements(By.XPATH, "//a[@data-lnk='Join Circle ']")
    # Join Target Circle
    context.driver.find_elements(By.XPATH, "//a[@data-lnk='Circle Deals ']")
    # See today's Target Circle deals
    context.driver.find_elements(By.XPATH, "//a[@data-lnk='Bonus']")
    # Target Circle Bonuses
    context.driver.find_elements(By.XPATH, "//a[@data-lnk='Partner']")
    # Target Circle Partners
    context.driver.find_elements(By.XPATH, "//a[@data-lnk='Voting']")
    # Community support votes
    context.driver.find_elements(By.XPATH, "//a[@data-lnk='Circe FAQs']")
    # Learn more about the loyalty program.

@then ('Verify red section has 2 benefit cells')
def red_benefit_cells_are_verified(context):
    context.driver.find_elements(By.XPATH, "//h3[@text()='Find a card right for you']")
    # Find a card right for you
    context.driver.find_elements(By.XPATH, "//p[@text()='Learn more about your Target Circle Card.']")
    # Learn more about your Target Circle Card.
    sleep(1)

@then('Verify purple section has 2 benefit cells')
def purple_benefit_cells_are_verified(context):
    context.driver.find_elements(By.XPATH, "//h3[@text()='Get unlimited Same Day Delivery']")
    # Get unlimited Same Day Delivery
    context.driver.find_elements(By.XPATH, "//p[@text()='Learn more about Target Circle 360™.']")
    # Learn more about Target Circle 360™.

