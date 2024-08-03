from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

VIEW_CART_CHECKOUT = (By.XPATH, "//a[@href='/cart']")
ADD_TO_CART = (By.ID, 'addToCartButtonOrTextIdFor79832816')
TOTAL_PRICE = (By.XPATH, "//div[@data-test='cartItem-title']")

@then('Add product to cart')
def add_to_cart(context):
    # click on sleeping pikachu
    context.driver.find_element(By.XPATH, "//picture[@data-test='@web/ProductCard/ProductCardImage/primary']").click()
    sleep(1)
    # click on shipping option
    context.driver.find_element(By.XPATH, "//button[@data-test='fulfillment-cell-shipping']").click()
    # wait for add to cart button to load
    context.wait.until(EC.visibility_of_element_located(ADD_TO_CART))
    # click on add to cart button
    context.driver.find_element(By.ID, 'addToCartButtonOrTextIdFor79832816').click()
    # wait for side navigation to pop-out
    context.wait.until(EC.visibility_of_element_located(VIEW_CART_CHECKOUT))

@then('Verify product has been added to cart')
def verify_product(context):
    # click on view cart & check out
    context.driver.find_element(By.XPATH, "//a[@href='/cart']").click()
    # wait for total price check to show
    context.wait.until(EC.visibility_of_element_located(TOTAL_PRICE))
    # total price check
    context.driver.find_element(By.XPATH, "//div[@data-test='cartItem-title']")
