import time
from selenium.webdriver.common.by import By
from Bases.basedriver import BaseDriver

class CheckoutPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    CHECKOUT_BUTTON = "checkout"
    FIRSTNAME_FIELD = "firstName"
    LASTNAME_FIELD = "lastName"
    ZIPCODE_FIELD = "postalCode"
    CONTINUE_BUTTON = "continue"

    def click_checkout_button(self):
        self.wait_until_element_is_clickable(By.NAME, self.CHECKOUT_BUTTON).click()


    def enter_firstname(self, firstname):
        self.wait_until_element_is_clickable(By.NAME, self.FIRSTNAME_FIELD).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.wait_until_element_is_clickable(By.NAME, self.LASTNAME_FIELD).send_keys(lastname)

    def enter_zipcode(self, zipcode):
        self.wait_until_element_is_clickable(By.NAME, self.ZIPCODE_FIELD).send_keys(zipcode)

    def click_continue_button(self):
        self.wait_until_element_is_visible(By.NAME, self.CONTINUE_BUTTON).click()
        time.sleep(3)

    def checkout_details(self, firstname, lastname, zipcode):
        self.click_checkout_button()
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_zipcode(zipcode)
        self.click_continue_button()