

---
authors:
  - id: 69
    title: Jean Thirion
  - id: 78
    title: Matt Wicks
---




<span class='intro'> <p class="ssw15-rteElement-P">If you use a Team per client, it is likely that you want to have a link between your Teams instances and the associated CRM record.​​<br></p> </span>

<p class="ssw15-rteElement-P">​At SSW we have a custom property for each client that stores the Teams URL&#58;​​​<br></p><dl class="image"><dt><img src="/PublishingImages/live-crm.jpg" alt="live-crm.jpg" /></dt><dd>Figure&#58; Live CRM | Company/Account Form – added Teams URL field</dd></dl><p>To get that URL, simply click the ellipsis next to your Team name and click &quot;Get link to Team&quot;</p><dl class="image"><dt><img src="/PublishingImages/get-teams-url.jpg" alt="get-teams-url.jpg" /></dt><dd>Figure&#58; get the Teams URL</dd></dl><p>This process can even be automated using Azure functions and Graph API to provision a new Team every time a new client is created in CRM.</p>


