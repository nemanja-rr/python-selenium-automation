Feature: Target cart icon empty verification message test

  Scenario:  User clicks on empty cart on target
  Given Open target main page
  When Click on empty cart
  Then Verify "Your cart is empty" message is shown
    # Enter steps here