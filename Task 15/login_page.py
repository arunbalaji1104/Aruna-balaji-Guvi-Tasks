from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.NAME, "username")
        self.password_locator = (By.NAME, "password")
        self.login_button_locator = (By.XPATH, "//button[@type='submit']")
        self.dashboard_locator = (By.XPATH, "//h6[text()='Dashboard']")

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_locator)
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_locator)
        ).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button_locator)
        ).click()

    def is_login_successful(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.dashboard_locator)
            )
            return True
        except:
            return False
