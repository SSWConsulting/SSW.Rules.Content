---
type: rule
archivedreason: 
title: Do you know the 3 steps to completing a PBI?
guid: 1de9df77-9b69-4242-b648-e08e5980e9a6
uri: do-you-know-the-3-steps-to-completing-a-pbi
created: 2013-08-30T06:33:21.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 3
  title: Eric Phan
related: []

---


​​​​​​The lifecycle of a PBI can be broken down into 3 steps&#58;<br>
<br><excerpt class='endintro'></excerpt><br>
<h3>1. Ready</h3><ol><li>Take the next PBI that was approved​ by the 
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=d3fc9341-c12c-465c-800b-c8575375d138" target="_blank">Product Owner​​</a><br></li><li>Is the PBI ready?<br>Check your PBI against your 
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=e01abde1-9a3e-4e4c-84a8-50e98e9c44d0" target="_blank">Definition of Ready​</a>. &quot;Ready&quot;​ PBIs must have Acceptance Criteria. A good Definition of Ready also encourages a test-first mentality in requirements e.g. Use Spec Flow (Given, When, Then) and/or create Test Cases and Test Steps first.<br></li><li>Attach and copy the Product Owner's&#160;email&#160;into the Acceptance Criteria (as per&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=bc6e26c0-855a-43d7-a1f4-3d816b7651d3">Do you attach and copy emails to the PBI?​</a>​).​</li><li>Email notification to the Product Owner - 
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=efd6c91e-7cc5-4473-a299-9104c8fd6e0d">use the @ mention rule</a><br></li><li>Break down your PBI into tasks.<br></li><li>Don't forget to make a task for testing! (So that it is visible in the task board). Note&#58; You can also 
      <a href="https&#58;//www.visualstudio.com/en-us/get-started/work/work-from-the-kanban-board-vs" target="_blank">customize the kanban board​</a> by adding a new column for testing, but we recommend adding a testing task to the PBI instead.</li></ol><dl class="badImage"><dt>
      <img src="/PublishingImages/KB-customize-board-columns.png" alt="KB-customize-board-columns.png" style="width&#58;750px;" />​</dt><dd>​​​Figure&#58; Adding a new &quot;Test&quot; state. This is only visible in the Product Backlog and not the Sprint Backlog</dd></dl><dl class="goodImage"><dt> 
      <img src="/PublishingImages/Testing-task.png" alt="Testing task.png" style="width&#58;750px;" />
   </dt><dd>F​igure&#58; Testing Task added to PBI. This is the board the team will use for 90% of the Sprint, so testing should be clearly visible here<br></dd></dl><h3>2. Code</h3><ol><li>From the PBI, create a new branch (so that your work is automatically tagged to the PBI)<br></li><li>On the Kanban Board, move your Task into &quot;In Progress&quot;<br></li><li>Checkout your new branch and start coding!<br></li><li>Code, code, code… (Red, Green, Refactor)</li><li>Push your changes, open a Pull Request<br></li><li>If you want feedback early, record a ​Done&#160;Video. E.g. Snagit<br></li></ol><h3>3. Done</h3><p>Is the PBI &quot;Done&quot;? Check your Definition of Done, and then&#58;</p><ol><li>Open a Pull Request<br></li><li>Get another engineer in your team to do an &quot;over the shoulder&quot; check of the code</li><li>Use&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=14be0d02-79ad-4286-8b78-4f28b0ed4eea">Microsoft's &quot;Test and Feedback&quot; Chrome extension </a>&#160;to test the app&#160;</li><li>Make changes based on feedback (and then get more feedback)</li><li>Complete the Pull Request! Merge changes to master, this automatically deploys (to either Test, Staging or Prod based on process maturity)</li><li>Email notification to the Product Owner – send a 
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=29d5ca5d-c191-475f-8db2-0086c44ca46c">Done Email (reply to the original)​</a>. Big items should have a 
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=f5fc27ce-af9d-4b57-ad64-3893dacc09e3">Done Video​​</a></li><li>Check the Acceptance Criteria for notes about email attachments (as per 
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=5baf5235-c66a-4e3d-9b27-55a4859ae8a2">Do you attach emails to the PBI?​</a>).​<br></li></ol>​<span style="line-height&#58;1.6;">Congrats. Your PBI is now ready to be demonstrated during your Sprint Review! (Note&#58; This is also the same process you follow for a Bug work&#160;item)</span> 
<dl class="goodImage"><dt>
      <a href="/PublishingImages/livecycle.jpg"></a><img src="/SiteAssets/do-you-know-the-3-steps-to-a-pbi/3StepsToAPBI.jpg" alt="3StepsToAPBI.jpg" style="width&#58;750px;" />​ </dt><dd>Good Figure&#58; This image includes all the important steps in a PBI lifecycle. Print this &quot;<a href="/Documents/3StepsToAPBI.pdf">SSW 3 Step​s to a PBI pdf</a>&quot; and put it on your 'War Room' wall<br></dd></dl>


