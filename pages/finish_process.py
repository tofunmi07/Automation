import time
from selenium.webdriver.common.by import By
from Bases.basedriver import BaseDriver

class FinishPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    FINISH_BUTTON = "finish"
    MENU_ICON = "//button[@id='react-burger-menu-btn']"
    HOME_BUTTON = "back-to-products"
    LOGOUT_BUTTON = "//a[@id='logout_sidebar_link']"


    def click_finish_button(self):
        self.wait_until_element_is_clickable(By.NAME, self.FINISH_BUTTON).click()


    def click_menu(self):
        self.wait_until_element_is_clickable(By.XPATH, self.MENU_ICON).click()
        time.sleep(1)

    def click_logout(self):
        self.wait_until_element_is_clickable(By.XPATH, self.LOGOUT_BUTTON).click()
        time.sleep(3)


    def click_home_button(self):
        self.wait_until_element_is_clickable(By.NAME, self.HOME_BUTTON).click()
        time.sleep(3)

    def finish_details(self):
        self.click_finish_button()
        self.click_menu()
        #self.click_home_button()
        self.click_logout()
