from behave import given, when, then
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@given("I open the Zen Portal")
def step_open_portal(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.login_page = LoginPage(context.driver)
    context.dashboard_page = DashboardPage(context.driver)
    context.login_page.open("https://www.zenclass.in/")


@when('I login with "{username}" and "{password}"')
def step_login(context, username, password):
    try:
        context.login_page.enter_username(username)
        context.login_page.enter_password(password)
        context.login_page.click_login()
    except NoSuchElementException as e:
        assert False, f"Login elements not found: {str(e)}"


@then("I should see the dashboard")
def step_dashboard_visible(context):
    assert context.dashboard_page.is_dashboard_visible(), "Dashboard is not visible!"


@then("the username and password fields should be visible")
def step_validate_fields(context):
    assert context.login_page.are_fields_visible(), "Username/Password fields are not visible!"


@then("the submit button should be enabled")
def step_validate_submit(context):
    assert context.login_page.is_submit_enabled(), "Submit button is not enabled!"


@then("I should be able to logout")
def step_logout(context):
    context.dashboard_page.click_logout()
    assert context.login_page.is_login_page_visible(), "Failed to logout!"
    context.driver.quit()
