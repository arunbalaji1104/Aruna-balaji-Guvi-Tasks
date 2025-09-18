from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_FIELD = (By.ID, "email")  # Replace with actual ID
    PASSWORD_FIELD = (By.ID, "password")  # Replace with actual ID
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Login']")  # Replace if needed
    ERROR_MESSAGE = (By.CLASS_NAME, "error-msg")  # Replace with actual class

    def login(self, email, password):
        try:
            self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
            self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
            self.driver.find_element(*self.LOGIN_BUTTON).click()
        except Exception as e:
            print(f"Error during login: {e}")

    def get_error_message(self):
        try:
            return self.driver.find_element(*self.ERROR_MESSAGE).text
        except:
            return ""
