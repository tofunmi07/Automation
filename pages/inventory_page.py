import time
from selenium.webdriver.common.by import By
from Bases.basedriver import BaseDriver


class InventoryPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    CLICK_PRODUCT1 = "add-to-cart-sauce-labs-backpack"
    CLICK_PRODUCT2 = "add-to-cart-sauce-labs-fleece-jacket"
    CART_BUTTON = "//a[@class='shopping_cart_link']"

    def click_product1(self):
        self.wait_until_element_is_clickable(By.NAME, self.CLICK_PRODUCT1).click()

    def click_product2(self):
        self.wait_until_element_is_clickable(By.NAME, self.CLICK_PRODUCT2).click()

    def click_cart(self):
        self.wait_until_element_is_clickable(By.XPATH, self.CART_BUTTON).click()
        time.sleep(3)


    def product_details(self):
        self.click_product1()
        self.click_product2()
        self.click_cart()




