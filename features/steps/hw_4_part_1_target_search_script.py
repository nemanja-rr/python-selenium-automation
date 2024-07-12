from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target home page')
def open_target_home_page(context):
    context.driver.get('https://www.target.com/')


@when('Search for product')
def search_for_product(context):
    # find search field and enter text
    context.driver.find_element(By.ID, 'search').send_keys('pokemon')
    # click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # wait for the page with search results to load
    sleep(6)

@then('Verify search worked')
def verify_search_worked(context):
    expected_text = 'pokemon'
    actual_text= context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_text in actual_text, f'Expected {expected_text} or in actual {actual_text}'
