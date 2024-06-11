---
seoDescription: Create a separate test plan per sprint to track testing progress and gain historical data on test pass rates for previous milestones.
type: rule
title: Do you create one test plan per Sprint?
uri: do-you-create-one-test-plan-per-sprint
authors:
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []
created: 2013-08-19T19:37:13.000Z
archivedreason: null
guid: e1300a89-ecb8-4612-a0aa-4e77ed12dc43
---

When you use Microsoft Azure Test Plans to create test plans and test suites for your project, there are several approaches that you can take.

<!--endintro-->

You could create 1 test plan that you use for all milestones and add test suites and tests as you progress. This is not a good approach because you then do not have historical data for your test pass rates for previous milestones.

::: bad  
![Figure: Bad Example – no historical data for your test pass rates for previous milestones](project-test-plan-bad.jpg)  
:::

By creating test plans for each Sprint, you can see when a Sprint is complete, based on your testing goals. You can also prepare the test plan for the next Sprint while you complete your testing for the current Sprint.

By using this approach, you can track your testing progress for each of your test plans to help you understand whether the quality of your application is improving.

::: good  
![Figure: Good Example -  Create test plans based on your testing goals for a specific Sprint](project-test-plan-good.jpg)  
:::

**Tip:** If you add both manual (scripted or exploratory) and automated tests to your test suites, you can view the overall testing status based on both of these types of tests for your test suites and test plans.

**Reference:** [Create test plans and suites](https://docs.microsoft.com/en-us/azure/devops/test/create-a-test-plan?view=azure-devops)
