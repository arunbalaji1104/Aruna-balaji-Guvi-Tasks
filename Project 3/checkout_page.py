from selenium.webdriver.common.by import By

class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    CONFIRMATION = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.ZIP_CODE).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def finish_order(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def get_confirmation_message(self):
        return self.driver.find_element(*self.CONFIRMATION).text
