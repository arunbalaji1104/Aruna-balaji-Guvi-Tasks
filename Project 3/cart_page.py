from selenium.webdriver.common.by import By

class CartPage:
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        product_names = [item.find_element(By.CLASS_NAME, "inventory_item_name").text for item in items]
        product_prices = [item.find_element(By.CLASS_NAME, "inventory_item_price").text for item in items]
        return list(zip(product_names, product_prices))

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
