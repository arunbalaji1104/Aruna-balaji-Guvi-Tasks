import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_checkout_process(driver):
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)
    products.add_random_products_to_cart(4)
    products.click_cart_icon()

    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_checkout_info("John", "Doe", "12345")
    checkout.finish_order()

    confirmation = checkout.get_confirmation_message()
    assert "Thank you for your order" in confirmation
