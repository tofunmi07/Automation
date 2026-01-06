from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By



@given(u'user open browser, enter the URL and arrives on the login page.')
def step_impl(context):
    context.driver.get('https://www.saucedemo.com/')


@when(u'user enters valid credentials')
def step_impl(context):
    context.driver.find_element(By.NAME, 'user-name').send_keys('problem_user')
    context.driver.find_element(By.NAME, 'password').send_keys('secret-sauce')


@when(u'user clicks on the login page')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//input[@id="login-button"]').click()


@then(u'user should be on the inventory page')
def step_impl(context):
    print("user should be on the inventory page")
    #assertion should be used

