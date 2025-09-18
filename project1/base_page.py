class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def visit(self, url):
        """Navigate to a URL"""
        try:
            self.driver.get(url)
        except Exception as e:
            print(f"Error navigating to {url}: {e}")

    def get_title(self):
        """Return the page title"""
        try:
            return self.driver.title
        except Exception as e:
            print(f"Error getting title: {e}")
            return ""

    def click(self, element):
        """Click on a web element"""
        try:
            element.click()
        except Exception as e:
            print(f"Error clicking element: {e}")

    def is_displayed(self, element):
        """Check if element is visible"""
        try:
            return element.is_displayed()
        except Exception:
            return False
