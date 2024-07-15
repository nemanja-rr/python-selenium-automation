Feature: Check if item has been added to cart test

  Scenario: Add any Target’s product into the cart
    Given Open target home page
    When Search for product
    Then Add product to cart
    Then Verify product has been added to cart