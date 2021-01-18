# -- FILE: features/remove_all_items.feature
Feature: Remove all itmes from card


  Scenario: Remove all card items and continue shopping
    Given standard user log in to app
     When add Sauce Labs backpack and bike light to card
      And user click on shopping trolley icon to open his card
      And remove each items from card
      And click CONTINUE SHOPPING button
     Then system back to inventory page
      And items counter icon disappeared