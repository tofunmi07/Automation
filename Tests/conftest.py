import pytest
from selenium import webdriver
from Library import configreader


@pytest.fixture(scope="function")
def openbrowser():
    #global driver
    driver = webdriver.Chrome()
    driver.get(configreader.readconfig('Details','Application URL'))
    driver.maximize_window()
    assert "Swag Labs" in driver.title, "Error: Did not land on the right page"

    yield driver
    driver.quit()