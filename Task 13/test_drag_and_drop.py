# Filename: test_drag_and_drop.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def setup_browser():
    # Setup Chrome WebDriver (make sure chromedriver is in PATH)
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_drag_and_drop_positive(setup_browser):
    """
    Positive Test Case:
    Perform drag and drop of the white box onto the yellow box.
    """
    driver = setup_browser
    driver.get("https://jqueryui.com/droppable/")

    # Switch to iframe containing drag and drop elements
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame"))
    )
    driver.switch_to.frame(iframe)

    # Locate draggable and droppable elements
    draggable = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "draggable"))
    )
    droppable = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "droppable"))
    )

    # Perform drag and drop operation
    ActionChains(driver).drag_and_drop(draggable, droppable).perform()

def test_drag_and_drop_negative_wrong_target(setup_browser):
    """
    Negative Test Case:
    Drag and drop white box onto itself (not the yellow box) to simulate failure.
    """
    driver = setup_browser
    driver.get("https://jqueryui.com/droppable/")

    # Switch to iframe containing drag and drop elements
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame"))
    )
    driver.switch_to.frame(iframe)

    # Locate draggable element
    draggable = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "draggable"))
    )

    # Try to drag and drop onto itself (wrong target)
    ActionChains(driver).drag_and_drop(draggable, draggable).perform()

if __name__ == "__main__":
    # Run tests with HTML report generation (requires pytest-html package)
    # Command to run from terminal:
    # pytest test_drag_and_drop.py --html=report.html --self-contained-html
    pytest.main()
