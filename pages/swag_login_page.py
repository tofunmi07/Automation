import time
from selenium.webdriver.common.by import By
from Bases.basedriver import BaseDriver


class LoginPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    USERNAME_FIELD = "user-name"
    PASSWORD_FIELD = "password"
    LOGIN_BUTTON = "login-button"

    def enter_username(self, username):
        self.wait_until_element_is_clickable(By.NAME, self.USERNAME_FIELD).send_keys(username)
        time.sleep(1)

    def enter_password(self, password):
        self.wait_until_element_is_clickable(By.NAME, self.PASSWORD_FIELD).send_keys(password)


    def click_login(self):
        self.wait_until_element_is_clickable(By.NAME, self.LOGIN_BUTTON).click()
        time.sleep(5)

    def login_details(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()





