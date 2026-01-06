from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_until_element_is_visible(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located((locator_type, locator)))
        return element

    def scroll_down(self):
        current_pos = self.driver.execute_script("return window.scrollY;")
        if current_pos < 100:
            print("Scrolling down to the bottom...")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
