import pytest
import time
from utils.driver_setup import DriverSetup
from pages.homepage import HomePage
from pages.login_page import LoginPage

@pytest.fixture(scope="module")
def setup():
    driver_setup = DriverSetup()
    driver = driver_setup.start_driver()
    yield driver
    driver_setup.quit_driver()

def test_login_valid_credentials(setup):
    home = HomePage(setup)
    home.visit("https://www.guvi.in")
    home.click_login()
    login = LoginPage(setup)
    login.login("valid_email@example.com", "valid_password")
    time.sleep(2)
    assert "dashboard" in setup.current_url

def test_login_invalid_credentials(setup):
    home = HomePage(setup)
    home.visit("https://www.guvi.in")
    home.click_login()
    login = LoginPage(setup)
    login.login("invalid@example.com", "wrongpassword")
    time.sleep(2)
    assert login.get_error_message() != ""
