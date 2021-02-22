---
type: rule
archivedreason: 
title: Done - Do you go beyond 'Done' and follow a 'Definition of Done'?
guid: f8b61f21-7d1f-497f-a63f-4b9b98c2156c
uri: done-do-you-go-beyond-done-and-follow-a-definition-of-done
created: 2010-02-10T00:09:02.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Peter Gfader
  url: https://ssw.com.au/people/peter-gfader
- title: Paul Neumeyer
  url: https://ssw.com.au/people/paul-neumeyer
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related: []
redirects: []

---


​Having a clear Definition of Done for your team is critical to your success and quality management in Scrum.<br><br>Every team is different, but all need to agree on which items are in their "Definition of Done". 
<br><excerpt class='endintro'></excerpt><br>
<h1>There are 3 levels of 'Done' in communication</h1><h2>Level 1</h2><ul><li>Sending a <a href=/dones-do-you-reply-done-and-delete-the-original-email>"Done" email</a>​</li></ul><h2>Level 2</h2><ul><li>Sending a "Done" email</li><li>Screenshots</li><li>Code</li></ul><h2>Level 3</h2><ul><li>Sending a "Done" email</li><li>Recording a quick and dirty "<a href=/record-a-quick-and-dirty-done-video>Done Video</a>"</li><li>Code (showing a full scenario e.g. a user story)</li></ul><h4>Example of a level 3 "done"</h4><div class="greyBox"><p>Subject: RE: Manad - Coded UI Tests #2</p><p style="margin-left:20px;">&gt; Create a new CodedUI test on your feedback form – search only to test the Telerik</p><p>Done</p>
   <img class="ms-rteCustom-ImageArea" alt="Coded UI Test passes in Visual Studio" src="level-3-done.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure – Coded UI Test passes in Visual Studio</span>
   <p>Jing Video of the test running: <a href="http://screencast.com/t/ps17fqsV" target="_blank">http://screencast.com/t/ps17fqsV</a> </p></div>
<span class="ms-rteCustom-FigureGood">Figure: Good example - The "done" shows a full scenario</span>
<h1>There are 8 levels of 'Done' in software quality</h1><p>Start with these examples showing typical "Definitions of Done" from beginner teams to more mature teams:</p><h2>Team - Level 1</h2><ul><li>The code compiles</li><li>All tasks are updated and closed</li><li>No high priority defects/bugs are on that user story</li></ul><h2>Team - Level 2</h2><ul><li> 
      <em>All of the above, plus</em> </li><li>All unit tests passed</li><li>Greater than 1% code coverage (not earth shattering, but you need to start somewhere)</li></ul><h2>Team - Level 3</h2><ul><li> 
      <em>All of the above, plus</em> </li><li>Successful build on the Build Server<br></li><li>
      <a href=/protect-your-master-branch>Git Branch Policies</a> <br>or<br>TFS Check in Policy - Change set Comments Policy (all check-ins must have a comment)<br></li><li>TFS Check in Policy - Work Items (all check-ins must be associated with a work item)</li><li>Code reviewed by one other team member (e.g. Checked by Bill)<br></li><li>Sending a Done email with screenshots<br></li></ul><dl class="goodImage"><dt> <img class="ms-rteCustom-ImageArea" alt="Check in policy" src="CheckinPolicy.jpg" /> </dt><dd>Figure: Good example - Add check in policies to enforce your Definition of Done</dd></dl><h2>Team - Level 4</h2><ul><li> 
      <em>All of the above, plus</em> </li><li>All acceptance criteria have been met</li><li>All acceptance criteria have an associated test passing (aka. Automated functional testing with Web Tests (Selenium), Coded UI Tests, or Telerik Tests)<br></li><li>Tip: Use Microsoft | <a href="https://marketplace.visualstudio.com/items?itemName=ms.vss-testmanager-web">Test Manager</a><br></li><li>Sending a Done email (with video recording using SnagIt) <br></li></ul><dl class="goodImage"><dt> <img src="TestPlanning-1.png" alt="TestPlanning-1.png" style="margin:0px;width:750px;height:532px;" /> </dt><dd>Figure: Organize tests in suites with built-in E2E traceability across requirements, test artifacts and defects</dd></dl><dl class="goodImage"><dt> <img src="MTR-2.png" alt="MTR-2.png" style="margin:0px;width:750px;" /> </dt><dd>Figure: Use the client, Microsoft Test Manager, to run tests and not just capture the pass/fail of steps, comments/attachments and bugs, but also capture diagnostic data during execution, such as screen recording, system info, image action log etc</dd></dl><dl class="goodImage"><dt> <img src="XT-3.png" alt="XT-3.png" style="margin:0px;width:750px;height:566px;" /> </dt><dd>Figure: Explore your web applications, find and submit bugs directly from your Chrome browser – no need for predefined test cases or test steps <br></dd></dl><div class="ms-rtestate-read ms-rte-embedcode ms-rte-embedil ms-rtestate-notify"> 
   <iframe width="750" height="422" src="https://www.youtube.com/embed/JJCgP7XcpNA" frameborder="0"></iframe> </div>
<font class="ms-rteCustom-FigureGood" size="+0">Figure: Good example - Done video showing the features worked on</font>
<h2>Team - Level 5</h2><ul><li> 
      <em>All of the above, plus</em> </li><li>Deployed to UAT (ideally using Continuous Deployment)</li><li>Complex code is documented (removing technical debt)</li><li>Product Owner acceptance</li></ul><h2>Team - Level 6</h2><ul><li> 
      <em>All of the above, plus</em> </li><li>Multiple environments automatically tested using Lab Management</li></ul><dl class="goodImage"><dt> <img class="ms-rteCustom-ImageArea" alt="Lab management" src="LabManagement.jpg" /> </dt><dd>Figure: Good example - A tester Lab Management to create VMs for testing the application, then defines a test plan for that application with Test Case Management</dd></dl><h2>Team - Level 7</h2><ul><li> 
      <em>All of the above, plus</em> </li><li>Automated Load Testing</li><li>Continuous Deployment</li></ul><dl class="goodImage"><dt> <img class="ms-rteCustom-ImageArea" alt="Acceptance Tests in MTM" src="LoadTesting.jpg" /> </dt><dd>Figure: Good example - Load testing involves multiple test agents running Web Performance Tests and pounding the application (simulating the behavior of many simultaneous users)</dd></dl><h2>Team - Level 8 (Gold)</h2><ul><li> 
      <em>All of the above, plus</em></li><li>Deployed to Production</li></ul><ul><p class="ssw15-rteElement-P">Congratulations! You are frequently deploying to production. This is called “Continuous Delivery” and allows you to gather quick feedback from your end users. </p><p class="ssw15-rteElement-P">You might have everything deployed to production, but it might not yet be visible to the end user. This can be achieved by having “<a href="http://martinfowler.com/bliki/FeatureToggle.html">Feature toggles</a> ” in place. The actual release of the functionality is a decision that the Product Owner and business takes.</p>
   <font face="Calibri"> <i></i></font></ul><p> 
   <strong>More Information: </strong></p><ul><li> 
      <a href=/do-your-user-stories-include-acceptance-criteria-aka-never-assume-automatic-gold-plating>Do your user stories include acceptance criteria?</a></li><li> 
      <a title="Do you enforce comments with check-ins?" href="http://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterSourceControlwithTFS.aspx#EnforceComments" target="_blank">Do you enforce comments with check-ins?</a> </li><li> 
      <a title="Do you enforce work item association with check-in?" href="http://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterSourceControlwithTFS.aspx#EnforceWorkItemAss" target="_blank">Do you enforce work item association with check-in?</a> </li><li> 
      <a title="Do you follow a Test Driven Process?" href="http://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterVersionControlwithTFS%28AKASourceControl%29.aspx#TestDrivenProcess" target="_blank" shape="rect">Do you follow a Test Driven Process?</a> </li><li>​<a href=/have-a-definition-of-ready>Do you have a "Definition of Ready"?</a></li></ul>


