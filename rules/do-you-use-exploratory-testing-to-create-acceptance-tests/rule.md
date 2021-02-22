---
type: rule
archivedreason: 
title: Do you use Exploratory Testing to create Acceptance Tests?
guid: fb39e79c-8749-4467-9327-518a768b0495
uri: do-you-use-exploratory-testing-to-create-acceptance-tests
created: 2013-08-07T22:15:34.0000000Z
authors:
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related: []
redirects: []

---


In an agile team, pre-planning all your tests is not always the most efficient use of time for testers.  PBIs can change direction, scope, and priority, and pre-planned tests are likely to change.<div><br></div><div>Exploratory testing provides the best way to create repeatable tests from the acceptance criteria - as you need them.​</div>
<br><excerpt class='endintro'></excerpt><br>
<p>There are two ways to run an exploratory test in Microsoft Test Manager.</p><dl class="badImage"><dt><img src="exploratory_2.png" alt="exploratory_2.png" style="width:750px;" /></dt><dd>Figure: Bad Example - go to the Test tab, choose Do Exploratory Testing, choose a PBI, then click Explore. Too many steps​<br></dd></dl><dl class="goodImage"><dt><img src="exploratory_1.png" alt="exploratory_1.png" style="width:750px;" /><br></dt><dd>Figure: Good Example - Right-click on a requirement in your test suite and choose "Explore requirement"<br></dd></dl><p>
   <strong>Note: </strong>You should always run an exploratory test against a PBI. This will automatically relate any bugs and test cases to that PBI (not to mention the exploratory test run).</p><p>When you start an Exploratory test, you don't see any test steps, but you can click on the title of the requirement to see its Acceptance Criteria.</p><dl class="image"><dt><img src="show_criteria.png" alt="show_criteria.png" style="width:750px;" /></dt><dd>Figure: Clicking on the title will show you the Acceptance Criteria</dd></dl><p>
   <strong>Note:</strong> <a href="/Pages/Do-Your-User-Stories-Include-Acceptance-Criteria.aspx">You should always have Acceptance Criteria on your PBIs!</a></p><p>If you find a bug while testing, click the <strong>Create bug</strong> button to add a bug related to the PBI.</p><dl class="image"><dt><img src="create_bug.png" alt="create_bug.png" style="width:750px;" /></dt><dd>Figure: Creating a bug from exploratory test links to the PBI</dd></dl><p>By default, the reproduction steps will be populated with the last 10 actions you took (you can <a href="http://geekswithblogs.net/TarunArora/archive/2011/12/14/mtm-11-configuration-settings-amp-customization.aspx">change this and other defaults with configuration</a>).  You can cut this down to just the relevant actions by clicking Change steps.</p><dl class="image"><dt><img src="change_bug_steps.png" alt="change_bug_steps.png" style="width:750px;" /></dt><dd>Figure: You can change the repro steps captured in the bug very easily</dd></dl><p>Now you have a bug, you should create a matching test case so you can verify when the bug is fixed.  This also gives you a handy regression test to help ensure the problem isn't reproduced later.</p><dl class="image"><dt><img src="save_create_test.png" alt="save_create_test.png" style="width:750px;" /></dt><dd>Figure: Click Save and create test to create a matching test case</dd></dl><p>Again, the steps are prepopulated from your bug steps.</p><dl class="image"><dt><img src="create_test.png" alt="create_test.png" style="width:750px;" /></dt><dd>Figure: The test steps are prepopulated from the action recording</dd></dl><h3 class="ssw15-rteElement-H3">Related Links</h3><div><ul><li>​<a href=/do-you-do-exploratory-testing-2>Do you do exploratory testing?</a>​<br></li></ul></div>


