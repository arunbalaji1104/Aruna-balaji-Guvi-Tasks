# Filename: test_saucedemo_task.py

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

LOGIN_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
EXPECTED_TITLE = "Swag Labs"
EXPECTED_HOMEPAGE_URL = LOGIN_URL
EXPECTED_DASHBOARD_URL = "https://www.saucedemo.com/inventory.html"
OUTPUT_FILE = "Webpage_task_11.txt"

@pytest.fixture(scope="module")
def driver():
    # Setup Chrome driver (chromedriver must be in PATH)
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def login(driver):
    driver.get(LOGIN_URL)
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    # Wait for potential page load/redirect
    time.sleep(3)

def save_page_content(driver, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(driver.page_source)

# Positive tests

def test_title_after_login(driver):
    login(driver)
    assert driver.title == EXPECTED_TITLE, f"Expected title '{EXPECTED_TITLE}', but got '{driver.title}'"

def test_homepage_url(driver):
    driver.get(LOGIN_URL)
    assert driver.current_url == EXPECTED_HOMEPAGE_URL, f"Expected homepage URL '{EXPECTED_HOMEPAGE_URL}', but got '{driver.current_url}'"

def test_dashboard_url_after_login(driver):
    login(driver)
    # Wait for URL to update after login
    for _ in range(10):
        if driver.current_url == EXPECTED_DASHBOARD_URL:
            break
        time.sleep(1)
    assert driver.current_url == EXPECTED_DASHBOARD_URL, f"Expected dashboard URL '{EXPECTED_DASHBOARD_URL}', but got '{driver.current_url}'"

def test_save_webpage_content(driver):
    login(driver)
    save_page_content(driver, OUTPUT_FILE)
    with open(OUTPUT_FILE, "r", encoding="utf-8") as file:
        content = file.read()
    assert len(content) > 0, "Webpage content saved is empty"

# Negative tests

def test_title_after_failed_login(driver):
    driver.get(LOGIN_URL)
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert error_message.is_displayed(), "Error message not displayed after failed login"

def test_url_after_failed_login(driver):
    driver.get(LOGIN_URL)
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    assert LOGIN_URL in driver.current_url, f"Expected to remain on login URL after failed login, but current URL is {driver.current_url}"

if __name__ == "__main__":
    # Command to run the test with HTML report:
    # pytest test_saucedemo_task.py --html=report.html --self-contained-html
    pass
