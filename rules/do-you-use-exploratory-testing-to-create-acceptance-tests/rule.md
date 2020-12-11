---
type: rule
archivedreason: 
title: Do you use Exploratory Testing to create Acceptance Tests?
guid: fb39e79c-8749-4467-9327-518a768b0495
uri: do-you-use-exploratory-testing-to-create-acceptance-tests
created: 2013-08-07T22:15:34.0000000Z
authors:
- id: 23
  title: Damian Brady
related: []

---

In an agile team, pre-planning all your tests is not always the most efficient use of time for testers.  PBIs can change direction, scope, and priority, and pre-planned tests are likely to change.



Exploratory testing provides the best way to create repeatable tests from the acceptance criteria - as you need them.

<!--endintro-->

There are two ways to run an exploratory test in Microsoft Test Manager.
<dl class="badImage">&lt;dt&gt;<img src="exploratory_2.png" alt="exploratory_2.png" style="width:750px;">&lt;/dt&gt;<dd>Figure: Bad Example - go to the Test tab, choose Do Exploratory Testing, choose a PBI, then click Explore. Too many steps<br></dd></dl><dl class="goodImage">&lt;dt&gt;<img src="exploratory_1.png" alt="exploratory_1.png" style="width:750px;"><br>&lt;/dt&gt;<dd>Figure: Good Example - Right-click on a requirement in your test suite and choose "Explore requirement"<br></dd></dl>
**Note:** You should always run an exploratory test against a PBI. This will automatically relate any bugs and test cases to that PBI (not to mention the exploratory test run).

When you start an Exploratory test, you don't see any test steps, but you can click on the title of the requirement to see its Acceptance Criteria.
<dl class="image">&lt;dt&gt;<img src="show_criteria.png" alt="show_criteria.png" style="width:750px;">&lt;/dt&gt;<dd>Figure: Clicking on the title will show you the Acceptance Criteria</dd></dl>
**Note:** [You should always have Acceptance Criteria on your PBIs!](/Pages/Do-Your-User-Stories-Include-Acceptance-Criteria.aspx)

If you find a bug while testing, click the  **Create bug** button to add a bug related to the PBI.
<dl class="image">&lt;dt&gt;<img src="create_bug.png" alt="create_bug.png" style="width:750px;">&lt;/dt&gt;<dd>Figure: Creating a bug from exploratory test links to the PBI</dd></dl>
By default, the reproduction steps will be populated with the last 10 actions you took (you can [change this and other defaults with configuration](http://geekswithblogs.net/TarunArora/archive/2011/12/14/mtm-11-configuration-settings-amp-customization.aspx)).  You can cut this down to just the relevant actions by clicking Change steps.
<dl class="image">&lt;dt&gt;<img src="change_bug_steps.png" alt="change_bug_steps.png" style="width:750px;">&lt;/dt&gt;<dd>Figure: You can change the repro steps captured in the bug very easily</dd></dl>
Now you have a bug, you should create a matching test case so you can verify when the bug is fixed.  This also gives you a handy regression test to help ensure the problem isn't reproduced later.
<dl class="image">&lt;dt&gt;<img src="save_create_test.png" alt="save_create_test.png" style="width:750px;">&lt;/dt&gt;<dd>Figure: Click Save and create test to create a matching test case</dd></dl>
Again, the steps are prepopulated from your bug steps.
<dl class="image">&lt;dt&gt;<img src="create_test.png" alt="create_test.png" style="width:750px;">&lt;/dt&gt;<dd>Figure: The test steps are prepopulated from the action recording</dd></dl>
### Related Links


* [Do you do exploratory testing?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=14be0d02-79ad-4286-8b78-4f28b0ed4eea)
