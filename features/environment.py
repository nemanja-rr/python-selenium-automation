import sys
import ssl
import os
from allure_behave.utils import scenario_name
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from time import sleep


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # driver_path = './chromedriver' # for macOS users
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # # HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # driver_path = './chromedriver'  # for macOS users
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ###BROWSER STACK#################################

    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'nemanjasimic_n1NRXu'
    bs_key = 'z7sz4eLYcBxscCLyi9GV'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        "os": "OS X",
        "osVersion": "Sonoma",
        'browserName': 'chrome',
        'sessionName': scenario_name
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)




############################################################

# def after_all(context):
#     context.driver.quit()


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
