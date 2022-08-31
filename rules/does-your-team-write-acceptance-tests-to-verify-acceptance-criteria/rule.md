---
type: rule
title: Do you write acceptance tests to verify Acceptance Criteria?
uri: does-your-team-write-acceptance-tests-to-verify-acceptance-criteria
authors:
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []
created: 2012-11-08T19:00:32.000Z
archivedreason: null
guid: e8e0f82e-bee8-42a5-a880-729986e56ecd
---
**Acceptance Tests** check that the Acceptance Criteria on a story are met. 

Test cases that define these acceptance tests should be written during story development and managed in the same system as the code, e.g. Azure DevOps. This allows for easier traceability between the code and the tests related to that code.

A combination of human and automated tests is likely to be required to complete the acceptance tests for a story.

<!--endintro-->

Suppose we have a user story to implement searching on customers with the following acceptance criteria on the story:

::: greybox

* When I enter ‘Adam’ in the Search box and click ‘Search’ I will see all entries starting with Adam in the Grid   
* When I enter ‘zzz’ in the Search box and click ‘Search’ I will see **no** entries in the Grid   
* If no results are retuned show a message box ‘No results found’   
* If no search text is entered, the ‘Search’ button should be disabled   
* If the button is disable and search text is entered, the ‘Search’ button becomes enabled   
* Right-clicking on a column header and using the ‘Sort’ functionality, sorts the data by that column
:::

**intro this screenshot from Azure DevOps**

![Figure: Acceptance test cases for a User Story (in Azure DevOps)](acceptance-tests.jpg)

**how to add the tests to the story - Tested By link type**

**show Azure Test Plans**
![Figure: The tester sees the Test Cases in Test Manager](test-cases.jpg)

![Figure: The tester follows each instruction (aka the Test Steps), and gives it a tick or cross](test-steps.jpg)