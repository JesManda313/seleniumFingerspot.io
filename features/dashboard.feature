Feature: Dashboard Navigation and Login

Background:
  Given I am on the "Login Page"
  When I login with email "haniatester@gmail.com" and password "Admin@123"
  Then I should be redirected to the "home" page

Scenario: Navigate Periods
  When I click the "Day" navigation button
  And I click the "Week" navigation button
  And I click the "Month" navigation button
  And I perform logout
  Then I should be redirected to the "login" page

