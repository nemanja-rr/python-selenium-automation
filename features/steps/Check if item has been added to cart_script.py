from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Add product to cart')
def add_to_cart(context):
    # click on sleeping pikachu
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='product-title']").click()
    sleep(1)
    # click on shipping option
    context.driver.find_element(By.XPATH, "//button[@data-test='fulfillment-cell-shipping']").click()
    sleep(1)
    # click on add to cart button
    context.driver.find_element(By.ID, 'addToCartButtonOrTextIdFor79832816').click()
    sleep(1)

@then('Verify product has been added to cart')
def verify_product(context):
    # click on view cart & check out
    context.driver.find_element(By.XPATH, "//a[@href='/cart']").click()
    sleep(3)
    # total price check
    context.driver.find_element(By.XPATH, "//div[@data-test='cartItem-title']")
