import time

from pages.finish_process import FinishPage
from pages.inventory_page import InventoryPage
from pages.swag_checkout_page import CheckoutPage
from pages.swag_login_page import LoginPage




def test_valid_login(openbrowser):
    driver = openbrowser
    lp = LoginPage(driver)
    lp.login_details("standard_user", "secret_sauce")
    driver.get_screenshot_as_file("./loginpage.png")
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "did not reach inventory page."
    ac = InventoryPage(driver)
    ac.product_details()
    assert driver.current_url == "https://www.saucedemo.com/cart.html", "did not reach cart page."
    cp = CheckoutPage(driver)
    cp.checkout_details("Oliver", "Queen", "783772")
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html", "did not reach checkout page"
    cp.scroll_down()
    time.sleep(2)
    fp = FinishPage(driver)
    fp.finish_details()


