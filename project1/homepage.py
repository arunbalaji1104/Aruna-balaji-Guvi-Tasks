from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    LOGIN_BUTTON = (By.LINK_TEXT, "Login")
    SIGNUP_BUTTON = (By.LINK_TEXT, "Sign Up")
    COURSES_MENU = (By.LINK_TEXT, "Courses")
    LIVE_CLASSES_MENU = (By.LINK_TEXT, "LIVE Classes")
    PRACTICE_MENU = (By.LINK_TEXT, "Practice")
    DOBBY_WIDGET = (By.ID, "dobby-widget")  # Example ID, replace if different

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def click_signup(self):
        self.driver.find_element(*self.SIGNUP_BUTTON).click()

    def is_element_visible(self, locator):
        return self.driver.find_element(*locator).is_displayed()
