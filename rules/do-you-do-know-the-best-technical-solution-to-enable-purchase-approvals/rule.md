---
type: rule
archivedreason: 
title: Do you do know the best technical solution to enable purchase approvals?
guid: b47b2645-8106-4f8a-8474-4bb691783115
uri: do-you-do-know-the-best-technical-solution-to-enable-purchase-approvals
created: 2013-04-19T19:04:02.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 4
  title: Ulysses Maclaren
related: []

---


<p>This is quintessential workflow and online forms. Basically you have purchase requests, then business rules, then approvals.<br>
E.g. Less than $1K your direct manager can approve.</p>
<br><excerpt class='endintro'></excerpt><br>
<ul> Choices&#58; 
   <li>
      <b>TFS 2012</b> (too hard)<br> You can have requests go in as a work items but there is no workflow service that runs on the server, so the workflow would have to be in a separate web service using WF4.</li><li>
      <b>SharePoint 2013</b> (recommended)<br> SharePoint needs an out of the box solution. You can have requests go into SharePoint lists and then there is a workflow service that runs on the server, using WF3 under the covers.</li><li>
      <b>CRM 2011</b>
      <br> CRM also needs an out of the box solution. You can have requests go into as CRM Entities and there is a workflow service that runs on the server, using WF3 under the covers.</li><li>
      <b>JIRA</b><br> Jira supports workflows and approvals (non .NET)</li></ul>


