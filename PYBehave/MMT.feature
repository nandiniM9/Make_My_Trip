Feature: HomeStay/Language
  Scenario:Varification of Home Stay booking
    Given launch chrome browser
    When open Make My Trip homepage
    Then Click on home stay button
    Then Select place in location bar
    And Click on selected place on dropdown
    Then select checkin date
    Then Select checkout date
    Then Select number of person
    And click on apply
    Then Click on search button
    Then Select hotel

  Scenario:Varification of language option
    Given launch chrome browser
    When open Make My Trip homepage
    Then Click on Language option
    And Click on dropdown of country selector
    And select country India
    And select languages hindi from radio button
    Then Click on apply button
    Then Click on Language option
    And select languages english from radio button
    Then Click on apply button
    Then Click on Language option
    And select languages tamil from radio button
    Then Click on apply button
    #UAE
    Then Click on Language option
    And Click on dropdown of country selector
    And select country uae
    And select languages english from radio button
    Then Click on apply button

    Then Click on Language option
    And select languages urdu from radio button
    Then Click on apply button

    #usa
    Then Click on Language option
    And Click on dropdown of country selector
    And select country usa
    And select languages english from radio button
    Then Click on apply button




