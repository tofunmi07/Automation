Feature: Customer Login Functionality
   As a registered user i want to login
  into the application with my username and password
  so that i can access the inventory page.

  Scenario: Registered users logging in with their verified details
    Given user open browser, enter the URL and arrives on the login page.
    When  user enters valid credentials
    And   user clicks on the login page
    Then  user should be on the inventory page
    When  user is on the inventory page
    And   user adds a product to cart
    And   user click on add to cart
    And   user sees the price of product right next to product name
    And   user clicks on checkout
    Then  user should be on the payment page