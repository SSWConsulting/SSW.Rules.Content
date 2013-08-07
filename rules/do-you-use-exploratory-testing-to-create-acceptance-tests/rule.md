---
type: rule
title: Do you use Exploratory Testing to create Acceptance Tests?
uri: do-you-use-exploratory-testing-to-create-acceptance-tests
created: 2013-08-07T22:15:34.0000000Z
authors:
- id: 23
  title: Damian Brady

---



<span class='intro'> In an agile team, pre-planning all your tests is not always the most efficient use of time for testers. &#160;PBIs can change direction, scope, and priority, and pre-planned tests are likely to change.<div><br></div><div>Exploratory testing gives you an easy way&#160;to create repeatable tests from the acceptance criteria - as you need them.</div> </span>

There are two ways to run an exploratory test in Microsoft Test Manager.<div><br></div><div><img src="/SoftwareDevelopment/RulesToBetterUserAcceptanceTests/PublishingImages/exploratory_2.png" alt="exploratory_2.png" style="margin&#58;5px;width&#58;650px;" /><br></div><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example - go to the Test tab, choose Do Exploratory Testing, choose a PBI, then click Explore. Too many steps.</dd><div><br></div><div><img src="/SoftwareDevelopment/RulesToBetterUserAcceptanceTests/PublishingImages/exploratory_1.png" alt="exploratory_1.png" style="margin&#58;5px;" /><br></div><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example - Right-click on a requirement in your test suite&#160;and choose Explore requirement</dd><div><strong>Note&#58; </strong>You should always run an exploratory test against a PBI. This will automatically relate any&#160;bugs and test cases to that&#160;PBI (not to mention&#160;the exploratory test run).</div><div><br></div><div>When you run an Exploratory test, you don't see any test steps, but you can click on the title of the requirement to see its Acceptance Criteria.</div><div><br></div><div><img src="/SoftwareDevelopment/RulesToBetterUserAcceptanceTests/PublishingImages/show_criteria.png" alt="show_criteria.png" style="margin&#58;5px;" /><br></div><div><strong>Figure&#58; Clicking on the title will show you the Acceptance Criteria</strong></div>


