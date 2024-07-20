from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

HEADER_TEXT = (By.XPATH, "//div[@data-test='resultsHeading']")


@given('Open target home page')
def open_target_home_page(context):
    context.driver.get('https://www.target.com/')


@when('Search for product')
def search_for_product(context):
    # find search field and enter text
    context.driver.find_element(By.ID, 'search').send_keys('pikachu sleeping')
    # click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # wait for the page with search results to load
    context.wait.until(EC.visibility_of_element_located(HEADER_TEXT))

@then('Verify search worked')
def verify_search_worked(context):
    expected_text = 'pikachu sleeping'
    actual_text= context.driver.find_element(*HEADER_TEXT).text
    assert expected_text in actual_text, f'Expected {expected_text} or in actual {actual_text}'
