import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver_init")
class TestLogin:

    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        login = LoginPage(self.driver)
        login.login("standard_user", "secret_sauce")
        assert "Swag Labs" in self.driver.title

    def test_invalid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        login = LoginPage(self.driver)
        login.login("invalid_user", "invalid_pass")
        error = login.get_error_message()
        assert "Epic sadface" in error
