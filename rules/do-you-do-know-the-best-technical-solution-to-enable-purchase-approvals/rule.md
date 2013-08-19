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


<p>This is one of the most common workflows that every company needs. </p><p>Companies have employees who make purchase requests, then business rules get fired, then you wait for approval.<br>
E.g. If less than $1K, then&#160;your direct manager can approve.</p><p>Unfortunately, no one has an out of the box solution for this, so here are your choices&#58;</p>
<br><excerpt class='endintro'></excerpt><br>
<ul> Choices&#58; 
   <li>
      <b>TFS 2012</b> (too hard)<br> You can have requests go in as a work items but there is no workflow service that runs on the server, so the workflow would have to be in a separate web service using WF4.</li><li>
      <b>SharePoint 2013</b> (recommended)<br>SharePoint doesn't have an out of the box solution. To configure it, have the purchase requests go into SharePoint lists and then the workflow service that runs on the server (using WF3 under the covers) can have business rules added.</li><li>
      <b>CRM 2011</b>
      <br> CRM also needs an out of the box solution. You can have requests go into as CRM Entities and there is a workflow service that runs on the server, using WF3 under the covers.</li><li>
      <b>JIRA</b><br> Jira supports workflows and approvals, like SharePoint, but it is not .NET</li></ul><p><strong>Suggestion to Microsoft&#58;</strong> Please provide an out of the box solution for CRM and SharePoint, so we dont have to configure this for each client. </p>


