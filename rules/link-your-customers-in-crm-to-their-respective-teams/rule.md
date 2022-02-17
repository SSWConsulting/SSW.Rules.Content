---
type: rule
title: Dynamics and Teams - Do you link your customers in CRM to their
  respective Teams?
uri: link-your-customers-in-crm-to-their-respective-teams
authors:
  - title: Jean Thirion
    url: https://ssw.com.au/people/jean-thirion
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
related: []
redirects:
  - dynamics-and-teams-do-you-link-your-customers-in-crm-to-their-respective-teams
created: 2020-03-27T21:55:12.000Z
archivedreason: null
guid: 1b2a7623-45c8-4a45-a46a-c2c9150f9180
---
If you use a Team per client, it is likely that you want to have a link between your Teams instances and the associated CRM record.

<!--endintro-->

At SSW we have a custom property for each client that stores the Teams URL:

![Figure: CRM | Company/Account Form – added Teams URL field](dynamics-and-teams.png)

### Simple:

To get that URL, simply click the ellipsis next to your Team name and click "Get link to Team"

![Figure: get the Teams URL](get-teams-url.jpg)

This process can even be automated using Azure functions and Graph API to provision a new Team every time a new client is created in CRM.

### Medium: 

**TODO: Lu to update**

![Figure: Use the Ribbon]()

### Optimal (Recommended) 

This process can even be automated using Azure functions and Graph API to provision a new Team every time a new client is created in CRM.

Click on this section on your CRM Dynamics to have a Team created:

![Figure: PCF control allows you to add a button to create a Team](click-to-create.png)