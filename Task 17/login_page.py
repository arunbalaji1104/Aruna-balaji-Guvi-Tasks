# pages/login_page.py

from playwright.sync_api import Page, TimeoutError

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        self.submit_btn = page.locator("button[type='submit']")
        self.logout_btn = page.locator("button#logout")  # Update selector as per portal

    def navigate(self, url):
        self.page.goto(url)

    def login(self, username, password):
        try:
            self.username_input.fill(username)
            self.password_input.fill(password)
            self.submit_btn.click()
        except TimeoutError:
            print("Element not found or not interactable")

    def logout(self):
        try:
            self.logout_btn.click()
        except TimeoutError:
            print("Logout button not found")

    def validate_elements(self):
        return (
            self.username_input.is_visible() and
            self.password_input.is_visible() and
            self.submit_btn.is_visible()
        )
