import pytest
import time
from utils.driver_setup import DriverSetup
from pages.homepage import HomePage

@pytest.fixture(scope="module")
def setup():
    driver_setup = DriverSetup()
    driver = driver_setup.start_driver()
    yield driver
    driver_setup.quit_driver()

def test_homepage_url(setup):
    home = HomePage(setup)
    home.visit("https://www.guvi.in")
    assert "guvi.in" in setup.current_url

def test_homepage_title(setup):
    home = HomePage(setup)
    home.visit("https://www.guvi.in")
    assert home.get_title() == "GUVI | Learn to code in your native language"

def test_login_button(setup):
    home = HomePage(setup)
    home.visit("https://www.guvi.in")
    assert home.is_element_visible(HomePage.LOGIN_BUTTON)

def test_signup_button(setup):
    home = HomePage(setup)
    home.visit("https://www.guvi.in")
    assert home.is_element_visible(HomePage.SIGNUP_BUTTON)

def test_signup_navigation(setup):
    home = HomePage(setup)
    home.visit("https://www.guvi.in")
    home.click_signup()
    time.sleep(2)
    assert "register" in setup.current_url

def test_menu_items(setup):
    home = HomePage(setup)
    home.visit("https://www.guvi.in")
    assert home.is_element_visible(HomePage.COURSES_MENU)
    assert home.is_element_visible(HomePage.LIVE_CLASSES_MENU)
    assert home.is_element_visible(HomePage.PRACTICE_MENU)

def test_dobby_widget(setup):
    home = HomePage(setup)
    home.visit("https://www.guvi.in")
    assert home.is_element_visible(HomePage.DOBBY_WIDGET)
