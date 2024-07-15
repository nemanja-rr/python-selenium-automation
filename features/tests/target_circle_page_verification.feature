Feature: Target circle benefit cells verification test

  Scenario: Verify Target Circle has 10 benefit cells
    Given Open target circle page
    When Page fully loads all sections
    Then Verify green section has 6 benefit cells
    Then Verify red section has 2 benefit cells
    Then Verify purple section has 2 benefit cells