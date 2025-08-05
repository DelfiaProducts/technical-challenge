Feature: Create categorization

  Scenario: Create a global categorization
    Given a categorization data
    | field            | value       |
    | name             |  "Expenses" |
    | budget           |  10000      |
    When create a categorization "global" with the provided data
    Then the output should contain the categorization ID
    And the categorization should be created successfully

  Scenario: Create a local categorization
    Given an existing parent categorization with ID "1"
    And a categorization data
    | field               | value                                  |
    | name                | "Marketing Expenses"                   |
    | budget              | 5000                                   |
    | integration_data_id | "de582392-37ad-490d-91fe-c0ecd58d43ed" |
    | groups              | ["mteam-1", "mteam-2"]                 |
    | parent_id           | "1"                                    |
    When create a categorization "local" with the provided data
    Then the output should contain the categorization ID
    And the categorization should be created successfully
    And the categorization should be linked to its parent categorization

  Scenario: fail to create a child categorization with budget exceeding parent's budget
    Given an existing parent categorization with ID "1"
    And a categorization data
    | field               | value                                  |
    | name                | "Expenses"                             |
    | budget              | 15000                                  |
    | parent_id           | "1"                                    |
    When create a categorization "global" with the provided data
    Then the categorization creation should fail
    And the error message should indicate budget exceeds parent's budget
