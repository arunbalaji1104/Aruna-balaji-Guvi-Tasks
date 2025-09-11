# pages/dashboard_page.py
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        # ✅ Update locators with actual ZenClass dashboard elements
        self.profile_icon = (By.CSS_SELECTOR, ".profile-icon")  
        self.logout_button = (By.CSS_SELECTOR, "button.logout")

    def is_loaded(self):
        try:
            return self.driver.find_element(*self.profile_icon).is_displayed()
        except NoSuchElementException:
            return False

    def logout(self):
        self.driver.find_element(*self.logout_button).click()
