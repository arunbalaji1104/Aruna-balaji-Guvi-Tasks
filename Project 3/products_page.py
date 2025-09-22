from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

class ProductsPage:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_COUNT = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_random_products_to_cart(self, count):
        buttons = self.wait.until(EC.presence_of_all_elements_located(self.ADD_TO_CART_BTN))
        random_buttons = random.sample(buttons, count)
        for btn in random_buttons:
            btn.click()
        return count

    def get_cart_count(self):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.CART_COUNT))
            return int(element.text)
        except:
            return 0

    def click_cart_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_ICON)).click()
