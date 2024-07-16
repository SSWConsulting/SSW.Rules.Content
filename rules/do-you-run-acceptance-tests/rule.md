---
type: rule
title: Do You Run Acceptance Tests?
uri: do-you-run-acceptance-tests
authors:
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
created: 2012-08-01T15:07:10.000Z
archivedreason: "Details of how to write and run acceptance tests can be found
  in the following rule:
  [https://www.ssw.com.au/rules/does-your-team-write-acceptance-tests-to-verify-acceptance-criteria](/rules/does-your-team-write-acceptance-tests-to-verify-acceptance-criteria)"
guid: edb1e5ff-cbbd-45d1-89ab-778ed8fdc95a
---

Once the coding is done by the developers, the functionality must then be stepped through in the required browsers. You can do this manually or automating it using a great tool like Microsoft Test Manager.

The 1st step in getting automated tests, is to setup Acceptance Tests:

<!--endintro-->

![Figure: Run each 'test case' with a prescribed configuration](run-acceptance-tests-1.jpg)  

![Figure: As you progress through each step, 'Pass' or 'Fail' the expected results. Take screen captures or video as appropriate](run-acceptance-tests-2.jpg)  

::: bad  
![Figure: Bad Example -After checking all the ‘Expected’ results in your MTM test, do not forget to 'Pass' or 'Fail' the Test Case](run-acceptance-tests-3.jpg)  
:::

::: good  
![Figure: Good example - After all 'Test Steps' have been checked off, choose the overall status for the test. Otherwise it will continue to show as 'Active' on the reports](run-acceptance-tests-4.jpg)  
:::

::: bad  
![Figure: Bad Example – No Tests should remain as 'Active' or 'Failed' at the end of a Sprint](run-acceptance-tests-5.jpg)  
:::

::: good  
![Figure: Good Example – every test is 'Passed'](run-acceptance-tests-6.jpg)  
:::

**Tip:** You can pass a test from the test list. Select the Test menu, then the Test Suite. Choose the Test Case to pass and then click the green button ‘Pass Test’.

The next step is to        [review the Statistics of the Sprint](/do-you-know-how-to-check-the-status-and-statistics-of-the-current-sprint).
