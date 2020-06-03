---
type: rule
title: Do you use Exploratory Testing to create Acceptance Tests?
uri: do-you-use-exploratory-testing-to-create-acceptance-tests
created: 2013-08-07T22:15:34.0000000Z
authors:
- id: 23
  title: Damian Brady

---



<span class='intro'> In an agile team, pre-planning all your tests is not always the most efficient use of time for testers. &#160;PBIs can change direction, scope, and priority, and pre-planned tests are likely to change.<div><br></div><div>Exploratory testing provides the best&#160;way&#160;to create repeatable tests from the acceptance criteria - as you need them.​</div> </span>

<p>There are two ways to run an exploratory test in Microsoft Test Manager.</p><dl class="badImage"><dt><img src="/PublishingImages/exploratory_2.png" alt="exploratory_2.png" style="width&#58;750px;" /></dt><dd>Figure&#58; Bad Example - go to the Test tab, choose Do Exploratory Testing, choose a PBI, then click Explore. Too many steps​<br></dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/exploratory_1.png" alt="exploratory_1.png" style="width&#58;750px;" /><br></dt><dd>Figure&#58; Good Example - Right-click on a requirement in your test suite&#160;and choose&#160;&quot;Explore requirement&quot;<br></dd></dl><p>
   <strong>Note&#58; </strong>You should always run an exploratory test against a PBI. This will automatically relate any&#160;bugs and test cases to that&#160;PBI (not to mention&#160;the exploratory test run).</p><p>When you start&#160;an Exploratory test, you don't see any test steps, but you can click on the title of the requirement to see its Acceptance Criteria.</p><dl class="image"><dt><img src="/PublishingImages/show_criteria.png" alt="show_criteria.png" style="width&#58;750px;" /></dt><dd>Figure&#58; Clicking on the title will show you the Acceptance Criteria</dd></dl><p>
   <strong>Note&#58;</strong> <a href="/Pages/Do-Your-User-Stories-Include-Acceptance-Criteria.aspx">You should always have Acceptance Criteria on your PBIs!</a></p><p>If you find a bug while testing, click the <strong>Create bug</strong> button to add a bug related to the PBI.</p><dl class="image"><dt><img src="/PublishingImages/create_bug.png" alt="create_bug.png" style="width&#58;750px;" /></dt><dd>Figure&#58; Creating a bug from exploratory test links to the PBI</dd></dl><p>By default, the reproduction steps will be populated with the last 10 actions you took (you can <a href="http&#58;//geekswithblogs.net/TarunArora/archive/2011/12/14/mtm-11-configuration-settings-amp-customization.aspx">change this and other&#160;defaults&#160;with&#160;configuration</a>). &#160;You can cut this down to just&#160;the relevant&#160;actions by clicking Change steps.</p><dl class="image"><dt><img src="/PublishingImages/change_bug_steps.png" alt="change_bug_steps.png" style="width&#58;750px;" /></dt><dd>Figure&#58; You can change the repro steps captured in the bug very easily</dd></dl><p>Now you have a bug, you should create a matching test case so you can verify when the bug is fixed. &#160;This also gives you a handy regression test to help ensure the problem isn't reproduced later.</p><dl class="image"><dt><img src="/PublishingImages/save_create_test.png" alt="save_create_test.png" style="width&#58;750px;" /></dt><dd>Figure&#58; Click Save and create test to create a matching test case</dd></dl><p>Again, the steps are prepopulated from your bug steps.</p><dl class="image"><dt><img src="/PublishingImages/create_test.png" alt="create_test.png" style="width&#58;750px;" /></dt><dd>Figure&#58; The test steps are prepopulated from the action recording</dd></dl><h3 class="ssw15-rteElement-H3">Related Links</h3><div><ul><li>​<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=14be0d02-79ad-4286-8b78-4f28b0ed4eea">Do you do exploratory testing?</a>​<br></li></ul></div>


