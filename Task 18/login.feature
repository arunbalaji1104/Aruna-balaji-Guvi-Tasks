Feature: Login functionality of Zen Portal
  As a valid user
  I want to login and logout of the Zen Portal
  So that I can access and exit securely

  @positive
  Scenario: Successful Login
    Given I open the Zen Portal
    When I login with "valid_user" and "valid_pass"
    Then I should see the dashboard

  @negative
  Scenario: Unsuccessful Login
    Given I open the Zen Portal
    When I login with "invalid_user" and "invalid_pass"
    Then I should see an error message

  @validation
  Scenario: Validate Username and Password Input Box
    Given I open the Zen Portal
    Then the username and password fields should be visible

  @validation
  Scenario: Validate Submit button
    Given I open the Zen Portal
    Then the submit button should be enabled

  @logout
  Scenario: Validate Logout functionality
    Given I open the Zen Portal
    When I login with "valid_user" and "valid_pass"
    And I click the logout button
    Then I should be redirected to the login page
