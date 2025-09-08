# Filename: test_guvi_login.py

"""
Python Selenium - Pytest script to automate GUVI login functionality:
1) Visit GUVI URL
2) Click Login and validate redirection to login page URL
3) Verify Username and Password inputs visibility and enabled
4) Test login submit button - positive and negative cases
5) Generate pytest HTML report with results

Instructions:
- Replace USERNAME and PASSWORD with valid credentials
- Run: pytest -v --html=report.html
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.guvi.in/"
LOGIN_URL = "https://www.guvi.in/sign-in/"

# Provide valid GUVI credentials here for positive test
USERNAME = "your_valid_username"
PASSWORD = "your_valid_password"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_button_redirect(driver):
    """Verify Login button redirects to Login URL."""
    driver.get(BASE_URL)
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
    )
    login_button.click()
    WebDriverWait(driver, 10).until(EC.url_contains(LOGIN_URL))
    assert driver.current_url.startswith(LOGIN_URL), f"Login button did not redirect to {LOGIN_URL}"

def test_username_password_fields_visible_enabled(driver):
    """Check Username and Password input fields are visible and enabled."""
    driver.get(LOGIN_URL)
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user_email"))
    )
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user_password"))
    )
    assert username_input.is_displayed() and username_input.is_enabled(), "Username field not visible/enabled"
    assert password_input.is_displayed() and password_input.is_enabled(), "Password field not visible/enabled"

def test_submit_button_functionality_positive(driver):
    """Positive test: Valid login should redirect from login page."""
    driver.get(LOGIN_URL)
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user_email"))
    )
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user_password"))
    )
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "commit"))
    )
    username_input.clear()
    username_input.send_keys(USERNAME)
    password_input.clear()
    password_input.send_keys(PASSWORD)
    submit_button.click()
    # Wait for URL change indicating successful login
    WebDriverWait(driver, 10).until_not(EC.url_contains(LOGIN_URL))
    assert driver.current_url != LOGIN_URL, "Login failed - URL did not change after submit"

def test_submit_button_functionality_negative(driver):
    """Negative test: Invalid credentials should not redirect from login page."""
    driver.get(LOGIN_URL)
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user_email"))
    )
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user_password"))
    )
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "commit"))
    )
    username_input.clear()
    username_input.send_keys("invalid@example.com")
    password_input.clear()
    password_input.send_keys("wrongpassword")
    submit_button.click()
    # Check for error alert visibility or that URL remains on login page
    WebDriverWait(driver, 10).until(
        EC.visibility_of_any_elements_located((By.CSS_SELECTOR, ".alert,.alert-danger"))
    )
    assert LOGIN_URL in driver.current_url, "Negative login test failed - unexpected URL change"
