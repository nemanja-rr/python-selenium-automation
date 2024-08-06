from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=15)
    def open_url(self, url):
        self.driver.get(url)
    def find_element(self, *locator):
        return self.driver.find_element(*locator)
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)
    def click(self, *locator):
        self.driver.find_element(*locator).click()
    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def get_current_window(self):
        window = self.driver.current_window_handle
        print('Current window:', window)
        return window

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        windows = self.driver.window_handles
        print(f'All windows {windows}')
        self.driver.switch_to.window(windows[1])
        print(f'Switched to window => {windows[1]}')

    def close(self):
        self.driver.close()

    def switch_to_window_by_id(self, window_id):
        self.driver.switch_to.window(window_id)
        print(f'Switched to window => {window_id}')

    def close(self):
        self.driver.close()

    def wait_until_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by locator {locator} not clickable'
        )
    def wait_and_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by locator {locator} not clickable'
        ).click()
    def wait_for_element_appear(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by locator {locator} did not appear'
        )
    def wait_for_element_disappear(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element by locator {locator} shown, but should not appear'
        )