import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_cart_operations(driver):
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)
    count = products.add_random_products_to_cart(4)
    assert products.get_cart_count() == count

    products.click_cart_icon()
    cart = CartPage(driver)
    items = cart.get_cart_items()
    assert len(items) == count
