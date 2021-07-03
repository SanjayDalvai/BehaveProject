Feature: OrangeHRM Login

Scenario: Login to OrangeHRM Page with valid parameters
  Given launch chrome browser
  When open orange hrm homepage
  And Enter username "admin" and password "admin123"
  And click on the Login Button
  Then user must successfully login to the Dashboard