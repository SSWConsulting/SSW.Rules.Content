---
type: rule
archivedreason: 
title: Do you create a Sprint Review/Retro email?
guid: aac90a70-58a3-4b10-97a1-fef2dc6bda39
uri: do-you-create-a-sprint-reviewretro-email
created: 2012-08-06T05:48:37.0000000Z
authors:
- id: 4
  title: Ulysses Maclaren
- id: 38
  title: Drew Robson
- id: 45
  title: Chris Briggs
related: []

---


​​After any Sprint Review and Retrospective, an email should be sent to all the stakeholders to update them on the outcome from the sprint:<br>
<br><excerpt class='endintro'></excerpt><br>
<ul><li>Subject: <Client Name> Sprint XX Review/Retro </li><li>This is a reply to the 
      <a href="/Pages/Do-you-create-a-Sprint-Forecast-email.aspx">Sprint Forecast email </a></li><li>Screenshot of Burndown from Azure DevOps<br></li><li>Breakdown of work completed (including current code coverage value)<br></li><li>Link to test environment </li><li>Relevant notes from the retrospective<br></li><li>CC - SSWSprintReviews@sswcom.onmicrosoft.com<br>​<br></li></ul><div class="greyBox"><p>Hi [Product Owner], </p><table><tbody><tr><td>Sprint in Review: </td><td>[Sprint Number]</td></tr><tr><td>Sprint Goal: </td><td>[Goal​]</td></tr><tr><td>Sprint Duration: </td><td>[Numbe​r of weeks]</td></tr><tr><td>Project: </td><td>[Project Name]</td></tr><tr><td>Project Portal: </td><td>[Link to project Portal]</td></tr><tr><td>Test Environment:     </td><td>[Link to test environment]</td></tr><tr><td>Product Owner: </td><td>[Product Owner Name]</td></tr></tbody></table><p>Attendees: 
      <em>(Optional as they may be in the to and CC)</em></p><p> <br></p><h3 class="ssw15-rteElement-H3">Sprint Review<br></h3><p> <br></p><table><tbody><tr><td> 
               <strong>ID</strong></td><td> 
               <strong>Title</strong></td><td> 
               <strong>State</strong></td><td colspan="1">​<strong>Effort</strong><br></td></tr><tr><td>24124 <br></td><td>UI Improvements<br></td><td>Done<br></td><td colspan="1">​4<br></td></tr><tr><td>24112 <br></td><td>Integrate Business Logic to MVC app  <br></td><td>Done</td><td colspan="1">​8<br></td></tr><tr><td>24097 <br></td><td>Styling<br></td><td>Committed  <br></td><td colspan="1">​16<br></td></tr></tbody></table> 
   <span class="ms-rteCustom-FigureNormal">Figure: Sprint Backlog from [Link to Sprint Backlog in Azure DevOps]</span> 
   <p> <br></p><p>As per <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=4f02d28d-5375-4530-abcb-0b541683bcbc">https://rules.ssw.com.au/do-you-know-what-happens-at-a-sprint-retrospective-meeting​</a>, we review:</p><p>1. Sprint Burndown (a quick overview of the sprint)</p><dl class="image"><dt>
         <img src="burndown.JPG" alt="" />
      </dt><dd>Figure: Sprint Burndown</dd></dl><p>2. Code Coverage (hopefully tests are increasing each sprint)<br>XXX</p><p>3. Velocity 
      <em>(Optional)</em><br>XXX</p><p>4. Burnup (for the release - the whole project, how are we tracking for the big picture?)</p><dl class="image"><dt>
         <img alt="Release Burnup.jpg" src="Release Burnup.jpg" style="width:600px;" />
      </dt><dd>Figure: Release Burnup</dd></dl><p>5. Production Deployments (How many times did we deploy to Production?)<br></p><dl class="image"><dt>
         <img alt="production-deploy.jpg" src="production-deploy.png" style="width:600px;" />
      </dt><dd>Figure: Deployments from Octopus Deploy</dd></dl><p class="ssw15-rteElement-P">6​​. Application Health Overview Timeline (For the entire Sprint)​​<br></p><p><span style="background-color:#f5f5f5;"><img alt="Application Health Overview Timeline.png" src="Application Insights.jpg" style="margin:5px;width:800px;height:188px;" /><br></span> </p><h3 class="ssw15-rteElement-H3">R&D <br></h3><p></p><p><strong>Did we do any experimental work?<br></strong></p><p><insert details of any trial/error processes, and ensure all detail is captured as per https://rules.ssw.com.au/do-you-record-your-failures><br></p><p>​<insert details of any problems for which no solutions existed, and ensure detail is captured as per https://rules.ssw.com.au/do-you-record-your-research-under-the-pbi><br>​<br></p><h3 class="ssw15-rteElement-H3">​Sprint Retrospective<br></h3><p>As part of our commitment to inspect and adapt as a team we conduct a Sprint Retrospective at the end of every Sprint. Here are the results of our Sprint Retrospective:<br></p><p> 
      <strong>What went well?</strong><br><insert what went well from retro><br></p><p> 
      <strong>What didn’t go so well?</strong><br><insert what did not went well from retro></p><p> 
      <strong>What improvements will be made for the next Sprint?</strong><br><insert what improvements will be made for the next Sprint></p><p> 
      <strong>Definition of Ready </strong>
      <em>
         <strong>- Optional​​​​​</strong></em></p><p><insert the definition of Ready. Normally that the PBIs are Sized with Acceptance criteria added></p><p> 
      <strong>Definition of Done </strong>
      <em>
         <strong>- Optional</strong></em></p><p><insert Definition of Done. Normally that it compiles, meets the acceptance criteria, and a test please has been sent if relevant>​</p><p><This is as per the rule: 
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=2a845add-b4b9-45ac-b47f-c646fe7d0c40">https://rules.ssw.com.au/do-you-create-a-sprint-review-retro-email​</a> /></p></div>
<span class="ms-rteCustom-FigureNormal">Figure: Good Example - Template for Sprint Review/Retro Email. Subject: Sprint xxx Review/Retro</span>


