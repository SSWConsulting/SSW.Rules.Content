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
related:
  - customize-dynamics-user-experience
redirects:
  - dynamics-and-teams-do-you-link-your-customers-in-crm-to-their-respective-teams
  - link-your-customers-in-crm-to-their-respective-teams
created: 2020-03-27T21:55:12.000Z
archivedreason: null
guid: 1b2a7623-45c8-4a45-a46a-c2c9150f9180
---
At your company, you never want to have a person asking "Where is that file?"
The answer should be "The answer is Teams, the question is irrelevant".

Microsoft Teams is a great solution for organizing client files and conversations. Create a new Team for each of your clients, and if you have multiple projects for one client, use Channels to keep them separate. There's no need to create a new Team just for a new project.

Once you have this set up, it is likely that you want to have a link between your Teams instances and the associated CRM record.

<!--endintro-->

`youtube: https://www.youtube.com/embed/3nkO8BxG8Sc`

In the video, Adam Cogan describes how they connect Dynamics 365 and Teams with an extra field. They change the Account table to add a custom column 'Teams-URL'.

![Figure: CRM | Company/Account Form – added Teams URL field](dynamics-and-teams.png)

:::greybox
**Note:** Each client should have its own Team. You might have two associated clients - e.g. Northwind Australia and Northwind USA - but if they are separate legal entities and have separate accounts in CRM, they should have separate Teams.
:::

### Level 1: Manual method

To get that URL, simply click the ellipsis next to your Team name and click "Get link to Team".

![Figure: Get the Teams URL](get-teams-url.jpg)

### Level 2: Automatic (Basic)

Add a button to the Ribbon to provision a new team and link to it.

##### How to add the button to the Dynamics Ribbon?

* [Customize the command bar - Power Apps | Microsoft Docs](https://docs.microsoft.com/en-us/powerapps/maker/model-driven-apps/use-command-designer) (new approach - customizing command bar using the command designers)

or

* [Ribbon Workbench](https://www.develop1.net/public/rwb/ribbonworkbench.aspx) (old approach -  using the ribbon workbench)

![Figure: Use the Ribbon](account_createteamssite.png)

### Level 3: Automatic (Advanced - best UX)

Using a PCF control you can add a button directly into the form that can do everything for you.

Click on this section on your CRM Dynamics to have a Team created:

![Figure: PCF control allows you to add a button to create a Team](click-to-create.png)

**Note #1:** Alternatively, this process can even be automated using Azure functions and Graph API to provision a new Team every time a new client is created in CRM. This has the disadvantage that every single Account would get a Team...and that could create a real mess of unused Teams.

**Note #2:** The Team's name can get out of sync if the Dynamics client name is changed, therefore you need one extra flow that is called when the client name is changed to keep them in sync.

See [how the PCF can make UI's shine](/customize-dynamics-user-experience).
