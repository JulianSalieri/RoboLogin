Feature: Login

  Scenario Outline: Successful login on <browser>
  Given I open the login page
  When I login with valid credentials
  Then I am redirected to the Trading page and it is loaded

Examples:
  | browser  |
  | chrome   |
  | firefox  |
