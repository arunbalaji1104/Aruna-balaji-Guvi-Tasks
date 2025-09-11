# tests/test_login.py

import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from utils.config import URL, VALID_USERNAME, VALID_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD

@pytest.fixture(scope="function")
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)
        yield login_page
        browser.close()

def test_successful_login(setup):
    setup.navigate(URL)
    setup.login(VALID_USERNAME, VALID_PASSWORD)
    assert setup.logout_btn.is_visible(), "Login failed or Logout button not visible"

def test_unsuccessful_login(setup):
    setup.navigate(URL)
    setup.login(INVALID_USERNAME, INVALID_PASSWORD)
    assert setup.submit_btn.is_visible(), "Submit button disappeared; login validation failed"

def test_validate_input_boxes(setup):
    setup.navigate(URL)
    assert setup.validate_elements(), "Username, Password, or Submit button not visible"

def test_logout_functionality(setup):
    setup.navigate(URL)
    setup.login(VALID_USERNAME, VALID_PASSWORD)
    setup.logout()
    assert setup.submit_btn.is_visible(), "Logout failed, login button not visible"
