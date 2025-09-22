from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTN)).click()

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MSG)).text
