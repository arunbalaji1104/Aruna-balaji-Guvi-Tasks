# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # ✅ Update these locators by inspecting ZenClass login page
        self.email_input = (By.NAME, "email")         
        self.password_input = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.error_message = (By.CSS_SELECTOR, ".error-message")  # adjust to actual error element

    def open(self, url="https://www.zenclass.in/"):
        self.driver.get(url)

    def login(self, username, password):
        self.driver.find_element(*self.email_input).clear()
        self.driver.find_element(*self.email_input).send_keys(username)
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def are_fields_visible(self):
        return (
            self.driver.find_element(*self.email_input).is_displayed() and
            self.driver.find_element(*self.password_input).is_displayed()
        )

    def is_submit_enabled(self):
        return self.driver.find_element(*self.login_button).is_enabled()

    def is_error_displayed(self):
        try:
            return self.driver.find_element(*self.error_message).is_displayed()
        except NoSuchElementException:
            return False

    def is_loaded(self):
        return self.are_fields_visible()
