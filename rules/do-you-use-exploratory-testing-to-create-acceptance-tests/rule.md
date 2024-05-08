---
type: rule
title: Do you use Exploratory Testing to create Acceptance Tests?
uri: do-you-use-exploratory-testing-to-create-acceptance-tests
authors:
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
related:
  - do-you-do-exploratory-testing
redirects: []
created: 2013-08-07T22:15:34.000Z
archivedreason: "Microsoft Test Manager has been deprecated. Learn how to use the \"Test & Feedback\" extension for exploratory testing: [https://www.ssw.com.au/rules/do-you-do-exploratory-testing](/rules/do-you-do-exploratory-testing)"
guid: fb39e79c-8749-4467-9327-518a768b0495
---

In an agile team, pre-planning all your tests is not always the most efficient use of time for testers. PBIs can change direction, scope, and priority, and pre-planned tests are likely to change.

Exploratory testing provides the best way to create repeatable tests from the acceptance criteria - as you need them.

<!--endintro-->

There are two ways to run an exploratory test in Microsoft Test Manager.

::: bad  
![Figure: Bad example - Go to the Test tab, choose Do Exploratory Testing, choose a PBI, then click Explore. Too many steps](exploratory\_2.png)  
:::

::: good  
![Figure: Good example - Right-click on a requirement in your test suite and choose "Explore requirement"](exploratory\_1.png)  
:::

::: info
**Note:** You should always run an exploratory test against a PBI. This will automatically relate any bugs and test cases to that PBI (not to mention the exploratory test run).
:::

When you start an Exploratory test, you don't see any test steps, but you can click on the title of the requirement to see its Acceptance Criteria.

![Figure: Clicking on the title will show you the Acceptance Criteria](show\_criteria.png)  

::: info
**Note:** [You should always have Acceptance Criteria on your PBIs!](/do-your-user-stories-include-acceptance-criteria-aka-never-assume-automatic-gold-plating)
:::

If you find a bug while testing, click the  **Create bug** button to add a bug related to the PBI.

![Figure: Creating a bug from exploratory test links to the PBI](create\_bug.png)  

By default, the reproduction steps will be populated with the last 10 actions you took (you can change this and other defaults with configuration). You can cut this down to just the relevant actions by clicking Change steps.

![Figure: You can change the repro steps captured in the bug very easily](change\_bug\_steps.png)  

Now you have a bug, you should create a matching test case so you can verify when the bug is fixed.  This also gives you a handy regression test to help ensure the problem isn't reproduced later.

![Figure: Click Save and create test to create a matching test case](save\_create\_test.png)  

Again, the steps are prepopulated from your bug steps.

![Figure: The test steps are prepopulated from the action recording](create\_test.png)  
