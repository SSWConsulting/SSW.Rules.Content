---
type: rule
title: Dynamics and Teams - Do you link your customers in CRM to their
  respective Teams?
uri: connect-crm-to-microsoft-teams
authors:
  - title: Jean Thirion
    url: https://ssw.com.au/people/jean-thirion
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
  - title: Calum Simpson
    url: https://www.ssw.com.au/people/calum-simpson
  - title: Chris Schultz
    url: https://www.ssw.com.au/people/chris-schultz
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
  - title: Lu Zhang
    url: https://www.ssw.com.au/people/lu-zhang
  - title: Jonty Gardner
    url: https://www.ssw.com.au/people/jonty-gardner
related: []
redirects:
  - dynamics-and-teams-do-you-link-your-customers-in-crm-to-their-respective-teams
  - link-your-customers-in-crm-to-their-respective-teams
created: 2020-03-27T21:55:12.000Z
archivedreason: null
guid: 1b2a7623-45c8-4a45-a46a-c2c9150f9180
---
Microsoft Teams is a great solution for organizing client files and conversations. Create a new Team for each of your clients, and if you have multiple projects for one client, use channels to keep them separate (there's no need to create a new Team for a new project).

Once you have this set up, it is likely that you want to have a link between your Teams instances and the associated CRM record.

<!--endintro-->

At SSW we have a custom property for each client that stores the Teams URL:

![Figure: CRM | Company/Account Form – added Teams URL field](dynamics-and-teams.png)

:::greybox
**NOTE:** Each client should have its own Team. You might have two associated clients - e.g. Northwind Australia and Northwind USA - but if they are separate legal entities and have separate accounts in CRM, they should have separate Teams.
:::

### Level 1: Manual

To get that URL, simply click the ellipsis next to your Team name and click "Get link to Team"

![Figure: get the Teams URL](get-teams-url.jpg)

### Level 2: Automatic (Basic)

Add a button to the Ribbon to provision a new team and link to it 

![Figure: Use the Ribbon](account_createteamssite.png)

### Level 3: Automatic (Advanced - best UX)

Using a PCF control you can add a button directly into the form that can do everything for you. 

Click on this section on your CRM Dynamics to have a Team created:

![Figure: PCF control allows you to add a button to create a Team](click-to-create.png)

Alternatively, this process can even be automated using Azure functions and Graph API to provision a new Team every time a new client is created in CRM.