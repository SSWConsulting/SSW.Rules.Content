---
type: rule
archivedreason: 
title: Do you turn an email into a GitHub Issue before starting work
guid: f866b251-c988-4e30-acc4-f6bac793c1d7
uri: do-you-turn-an-email-into-a-github-issue-before-starting-work
created: 2020-10-27T03:57:22.0000000Z
authors:
- id: 100
  title: Prem Radhakrishnan
- id: 1
  title: Adam Cogan
- id: 99
  title: Christian Morford-Waite
related: []

---


​​​​If a Product Owner sends an email to the development team with a request, that email should be turned into a Github Issue before any work is started or the work is prioritized on the backlog. <div><br></div><div>Power Automate has a connector to do this automatically when an email arrives in Outlook. It can create a new Github Issue by parsing the From, To, Subject and body of the email. </div><div><br></div><div>However, at the moment there is a limitation that it doesn't read inline attachments in emails and therefore you have to create your issues manually in Github.<br></div>
<br><excerpt class='endintro'></excerpt><br>
<div><dl class="image"><dt>
         <img src="email-to-github-issue2.png" alt="In Power Automate choose Github" style="width:800px;" />
      </dt><dd>Figure: Power Automate | Connectors | Github<br></dd></dl><dl class="image"><dt>
         <img src="email-to-github-issue1.png" alt="Use Flow connectors in Power Automate to create a new Github Issue from Outlook" />
      </dt><dd>​​Figure: Configure Flow connectors to create a new Github Issue from Outlook<br></dd></dl><p style="font-weight:bold;color:red;">🔥Warning: This Flow connector does not suport inline images.​</p><p style="font-weight:bold;color:red;"> 
      <br> 
   </p><dl class="goodImage"><dt>
         <img src="email-to-github-issue3.png" alt="Good Example - Github issue created automatically from Outlook" />
      </dt> ​ 
      <dd>Figure: Good Example - Github issue created from Outlook ​using Flow connectors <br></dd></dl>​ 
   <p></p> ​<br>
   <dl class="badImage"><dt>
         <img src="email-to-github-issue.png" alt="Bad Example - inline attachment shows up as junk characters" />
      </dt> ​ 
      <dd>Figure: Bad Example - Github issue created using Flow - inline attachment shows up as junk characters<br></dd></dl><p>
      <br>
   </p>​ 
   <h3>​Related rules<br></h3><ul><li> ​ 
         <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=2c4dfc14-8084-4277-ae5e-7f5f692e4065">Do you know the 3 steps to a PBI?</a> </li><li>
         <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=efd6c91e-7cc5-4473-a299-9104c8fd6e0d">Do you know when you use @ mentions in a PBI?</a><br> </li></ul>​<br><br></div>


