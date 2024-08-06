from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By



@given('Open sign in page')
def open_sign_in(context, self=None):
    context.app.open_sign_in_page.open_sign_in()
    sleep(1)
@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.open_sign_in_page.get_current_window()

@when('Click on Target terms and conditions link')
def click_on_target_terms_conditions_link(context):
    context.app.open_sign_in_page.click_tc_link()
    sleep(1)


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.open_sign_in_page.switch_to_new_window()
# print(context.driver.window.handles)


@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page(context):
    context.app.terms_and_conditions_page.verify_partial_url()


@then('User can close new window and switch back to original')
def close_new_window_and_switch_back_to_original(context):
    context.app.terms_and_conditions_page.verify_partial_url()
