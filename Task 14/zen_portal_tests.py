# zen_portal_tests.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, NoSuchFrameException

class ZenLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.email_input = (By.XPATH, "//input[@placeholder='Enter your mail']")
        self.password_input = (By.XPATH, "//input[@placeholder='Password']")
        self.login_button = (By.XPATH, "//button[text()='Login']")

    def switch_to_login_frame_if_present(self):
        try:
            # Adjust selector to actual iframe if possible; example generic:
            iframe = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
            self.driver.switch_to.frame(iframe)
        except (TimeoutException, NoSuchFrameException):
            # No iframe present, continue on default content
            pass

    def enter_email(self, email):
        self.switch_to_login_frame_if_present()
        element = self.wait.until(EC.visibility_of_element_located(self.email_input))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(email)

    def enter_password(self, password):
        element = self.wait.until(EC.visibility_of_element_located(self.password_input))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(password)

    def click_login(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.login_button))
        btn.click()

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

class ZenHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.profile_dropdown = (By.CSS_SELECTOR, "button[aria-label='account of current user']")
        self.logout_button = (By.XPATH, "//a[text()='Logout']")

    def open_profile_menu(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.profile_dropdown))
        btn.click()

    def click_logout(self):
        self.open_profile_menu()
        logout_btn = self.wait.until(EC.element_to_be_clickable(self.logout_button))
        logout_btn.click()

    def is_logged_in(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.profile_dropdown))
            return True
        except TimeoutException:
            return False

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.zenclass.in/login")
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestZenPortal:

    valid_email = "arunbalaji1104@gmail.com"
    valid_password = "Aishu2201@"
    invalid_email = "invalid@example.com"
    invalid_password = "invalidpass"

    def test_successful_login(self):
        login_page = ZenLoginPage(self.driver)
        login_page.enter_email(self.valid_email)
        login_page.enter_password(self.valid_password)
        login_page.click_login()
        login_page.switch_to_default_content()

        home_page = ZenHomePage(self.driver)
        assert home_page.is_logged_in(), "Login failed with valid credentials."

    def test_unsuccessful_login(self):
        login_page = ZenLoginPage(self.driver)
        self.driver.get("https://www.zenclass.in/login")

        login_page.enter_email(self.invalid_email)
        login_page.enter_password(self.invalid_password)
        login_page.click_login()
        login_page.switch_to_default_content()

        try:
            error = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Invalid')]"))
            )
            assert error.is_displayed(), "Error message not displayed on invalid login."
        except TimeoutException:
            pytest.fail("Login error message not found for invalid login.")

    def test_validate_email_password_input_box(self):
        login_page = ZenLoginPage(self.driver)
        self.driver.get("https://www.zenclass.in/login")

        login_page.switch_to_login_frame_if_present()
        email_elem = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(login_page.email_input)
        )
        password_elem = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(login_page.password_input)
        )
        assert email_elem.is_enabled(), "Email input box is not enabled."
        assert password_elem.is_enabled(), "Password input box is not enabled."
        login_page.switch_to_default_content()

    def test_validate_login_button(self):
        login_page = ZenLoginPage(self.driver)
        self.driver.get("https://www.zenclass.in/login")

        login_page.switch_to_login_frame_if_present()
        login_btn = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(login_page.login_button)
        )
        assert login_btn.is_enabled(), "Login button is not enabled."
        login_page.switch_to_default_content()

    def test_logout_functionality(self):
        login_page = ZenLoginPage(self.driver)
        self.driver.get("https://www.zenclass.in/login")

        login_page.enter_email(self.valid_email)
        login_page.enter_password(self.valid_password)
        login_page.click_login()
        login_page.switch_to_default_content()

        home_page = ZenHomePage(self.driver)
        assert home_page.is_logged_in(), "Login failed with valid credentials."

        home_page.click_logout()

        try:
            login_page.switch_to_login_frame_if_present()
            email_elem = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(login_page.email_input)
            )
            assert email_elem.is_displayed(), "Logout failed - login page not displayed."
            login_page.switch_to_default_content()
        except TimeoutException:
            pytest.fail("Did not return to login page after logout.")


if __name__ == "__main__":
    # Run using: pytest zen_portal_tests.py --html=report.html
    pass

