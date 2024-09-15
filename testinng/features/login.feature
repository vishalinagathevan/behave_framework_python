Feature: Login functionality

  Scenario: Successful login with valid credentials
    Given I navigate to the Login page
    When I enter valid username and valid password into the fields
    And I click on the Login button
    Then I should get logged in