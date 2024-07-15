Feature: Target product search BDD test

  Scenario: Using search function to look for products
    Given Open target home page
    When Search for product
    Then Verify search worked