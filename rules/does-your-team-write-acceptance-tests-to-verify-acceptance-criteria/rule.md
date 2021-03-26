---
type: rule
archivedreason: 
title: Do you write acceptance tests to verify Acceptance Criteria?
guid: e8e0f82e-bee8-42a5-a880-729986e56ecd
uri: does-your-team-write-acceptance-tests-to-verify-acceptance-criteria
created: 2012-11-08T19:00:32.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []

---

**Acceptance Tests** (built by the developers) verify that the Acceptance Criteria are met.

The goal is for teams to move beyond manual testing and implement automated testing. E.g. CodedUI tests, Telerik Tests etc

Test cases answer the question, "How do I test and what are the test steps?"

<!--endintro-->

![Figure: Test Cases in a User Story (MSF For Agile Template)](acceptance-criteria-test-cases.jpg)

::: greybox
 Positive Test - When I enter ‘Adam’ in the Search box and click ‘Search’ I will see all entries starting with Adam in the Grid   
 Negative Test - When I enter ‘zzz’ in the Search box and click ‘Search’ I will see **no** entries in the Grid   
 Gold Plating - If no results are retuned show a message box ‘No results found’   
 Gold Plating – Validation: If no search text is entered, the ‘Search’ button should be disabled   
 Gold Plating – Validation: If the button is disable and search text is entered, the ‘Search’ button becomes enabled   
 Gold Plating – Right clicking on a column header and using the ‘Sort’ functionality, sorts the data by that column   
 Gold Plating – if a large set of results is returned, clicking the pagination page numbers shows the correct data   
 Gold Plating – if a large set of results is returned and we are on page &gt; 1, clicking the ‘Prev’ button goes to the previous page   
 Gold Plating – if a large set of results is returned and we are on page 1, ‘Prev’ button does not error   
 Gold Plating – if a large set of results is returned and we are on page &lt; MaxPage, clicking the ‘Next’ button goes to the next page   
 Gold Plating – if a large set of results is returned and we are on page = MaxPage, clicking the ‘Next’ button does not error   
:::
::: good
Figure: Good example - Acceptance Tests
:::

![Figure: The tester sees the Test Cases in Test Manager](test-cases.jpg)

![Figure: The tester follows each instruction (aka the Test Steps), and gives it a tick or cross](test-steps.jpg)
