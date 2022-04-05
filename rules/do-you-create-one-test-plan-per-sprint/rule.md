---
type: rule
archivedreason: 
title: Do you create one test plan per Sprint?
guid: e1300a89-ecb8-4612-a0aa-4e77ed12dc43
uri: do-you-create-one-test-plan-per-sprint
created: 2013-08-19T19:37:13.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []

---

When you use Microsoft Test Manager to create test plans and test suites for your team project, there are several approaches that you can take.  

<!--endintro-->

You may only create 1 test plan that you use for all milestones and add test suites and tests as you progress. This is bad because if you use this approach, you do not have historical data for your test pass rates for previous milestones.

::: bad  
![Figure: Bad Example – no historical data for your test pass rates for previous milestones](project-test-plan-bad.jpg)  
:::

By creating test plans for each Sprint, you can see when a Sprint is complete, based on your testing goals. You can also prepare the test plan for the next Sprint while you complete your testing for the current Sprint.

By using this approach, you can track your testing progress for each of your test plans and see that the quality of your application is improving.

::: good  
![Figure: Good Example -  Create test plans based on your testing goals for a specific Sprint](project-test-plan-good.jpg)  
:::

**Tip:** If you add both manual and automated tests to your test suites, you can view the overall quality based on both of these types of tests for your test suites and test plans.

**Reference:** [Guidance for Creating Test Plans and Test Suites](http://msdn.microsoft.com/en-us/library/ff972304.aspx)
