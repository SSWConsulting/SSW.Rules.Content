---
type: rule
archivedreason: 
title: Dynamics and Teams - Do you link your customers in CRM to their respective Teams?
guid: 1b2a7623-45c8-4a45-a46a-c2c9150f9180
uri: dynamics-and-teams---do-you-link-your-customers-in-crm-to-their-respective-teams
created: 2020-03-27T21:55:12.0000000Z
authors:
- id: 69
  title: Jean Thirion
- id: 78
  title: Matt Wicks
related: []

---


<p class="ssw15-rteElement-P">​If you use a Team per client, it is likely that you want to have a link between your Teams instances and the associated CRM record.​​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-P">​At SSW we have a custom property for each client that stores the Teams URL:​​​<br></p><dl class="image"><dt><img src="live-crm.jpg" alt="live-crm.jpg" /></dt><dd>Figure: Live CRM | Company/Account Form – added Teams URL field</dd></dl><p>To get that URL, simply click the ellipsis next to your Team name and click "Get link to Team"</p><dl class="image"><dt><img src="get-teams-url.jpg" alt="get-teams-url.jpg" /></dt><dd>Figure: get the Teams URL</dd></dl><p>This process can even be automated using Azure functions and Graph API to provision a new Team every time a new client is created in CRM.</p>


