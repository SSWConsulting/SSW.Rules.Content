---
type: rule
title: Do you know how to create a Test Case with Azure Test Plans?
uri: create-a-test-case-with-azure-test-plans
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
created: 2022-08-15T00:25:19.555Z
guid: 6c6202a0-a01a-4435-8e3b-acaa84975c47
---
You can create a test case in Azure Test Plans directly from a Work Item (e.g. a Product Backlog Item or Bug) and also from a Test Plan or Test Suite.

<!--endintro-->

## Creating a test case from a Work Item

You can create a new test case from any list of work items (e.g. a Sprint Backlog).

![Figure: Double click the Work Item that you want to create a Test Case for to open it](create-test-case-from-work-item.jpg)

![Figure: Under "Related Work", choose Add Link and select New Item](create-test-case-from-work-item-new-item.jpg)

![Figure: Ensure that the link type is 'Tested By', that the work item type is 'Test Case' and enter a title for the Test Case. Click OK](create-test-case-from-work-item-add-link.jpg)

![Figure: Update the State and Details sections (making sure to select the correct iteration) and click on 'Click or type here to add a step' and proceed to add the steps required to test the Work Item](create-test-case-from-work-item-new-test-case.jpg)

![Figure: After entering each action and its expected result, click Save and Close to create the new test case](create-test-case-from-work-item-new-test-case-save.jpg)

## Creating a test case from a Test Plan or Test Suite

re-use most of the above steps, maybe just split out the launch points into this and make rest generic?

** REMEMBER TO DO THIS Add your rule to a category