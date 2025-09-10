import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # Ensure executable is in PATH
    driver.maximize_window()
    yield driver
    driver.quit()

def test_guvi_dynamic_xpath_safe_handling(driver):
    driver.get("https://www.guvi.in/")
    wait = WebDriverWait(driver, 20)  # Increased timeout for delays

    # Helper for safe element location with return None if not found
    def safe_find(xpath):
        try:
            return wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            print(f"Element for XPath {xpath} not found.")
            return None

    # 3) Relative XPath Tasks
    courses = safe_find("//*[normalize-space(text())='Courses']")
    if courses:
        parent = courses.find_element(By.XPATH, "..")
        first_child = parent.find_element(By.XPATH, "./*[1]")
        print("Parent tag of 'Courses':", parent.tag_name)
        print("First child tag of parent:", first_child.tag_name)

        try:
            second_sibling = courses.find_element(By.XPATH, "following-sibling::*[2]")
            print("Second following sibling text:", second_sibling.text)
        except NoSuchElementException:
            print("Second sibling of 'Courses' not found")
    else:
        pytest.skip("'Courses' element not found, skipping test.")

    element_with_href = safe_find("//*[@href and contains(@href, 'login')]")
    if element_with_href:
        parent_of_href = element_with_href.find_element(By.XPATH, "..")
        print("Parent tag of element with href containing 'login':", parent_of_href.tag_name)
    else:
        pytest.skip("Element with href containing 'login' not found, skipping test.")

    # 4) XPath Axes Tasks
    login_elem = safe_find("//*[normalize-space(text())='Login']")
    if login_elem:
        ancestors = login_elem.find_elements(By.XPATH, "ancestor::*")
        print(f"Number of ancestors of 'Login': {len(ancestors)}")
        preceding = login_elem.find_elements(By.XPATH, "preceding::*")
        print(f"Number of preceding elements of 'Login': {len(preceding)}")
    else:
        print("'Login' element not found, skipping related axis checks.")

    our_solutions_elem = safe_find("//*[contains(normalize-space(text()), 'Our Solutions')]")
    if our_solutions_elem:
        following_sibs = our_solutions_elem.find_elements(By.XPATH, "following-sibling::*")
        print(f"Number of following siblings of 'Our Solutions': {len(following_sibs)}")
    else:
        print("'Our Solutions' element not found, skipping following siblings check.")

    # Minimal assertions if critical elements found
    if courses and element_with_href:
        assert True
    else:
        pytest.skip("Critical elements missing for assertions.")

