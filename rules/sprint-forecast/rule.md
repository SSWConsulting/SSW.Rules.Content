---
type: rule
title: Do you create a Sprint Forecast? (aka The functionality that will be developed during the Sprint)
uri: sprint-forecast
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Christian Morford-Waite
    url: https://ssw.com.au/people/christian-morford-waite
related:
  - github-sprint-templates
redirects:
  - do-you-create-a-sprint-forecast-aka-the-functionality-that-will-be-developed-during-the-sprint
created: 2010-12-02T03:53:59.000Z
archivedreason: null
guid: f749bf03-8785-4433-a5c5-6c21cda9b782
---
After the [Sprint Planning meeting](/do-you-know-what-happens-at-a-sprint-planning-meeting), it is useful for the Development Team to send the Product Owner (PO) a Sprint Forecast for the next Sprint. Doing this helps to improve common understanding in, and sometimes to enforce, the relationship between the PO and the Team.

This is simply an agreement between the Development Team and the PO for one Sprint and should be confirmed via an email at the beginning of every Sprint.

<!--endintro-->

> “The implementation team agrees to do its best to deliver an agreed on set of features (scope) to a defined quality standard by the end of the Sprint. (Ideally they deliver what they promised, or even a bit more). The Product Owner agrees not to change his instructions before the end of the Sprint.”  
> **Agile Project management**

Each Sprint in a Scrum project can be considered a mini-project that has **time** (Sprint Length), **scope** (Sprint Backlog), **quality** (Definition of Done) and **cost** (Team Size * Sprint Length). Only the scope can vary and this is measured every Sprint.

::: email-template
|          |     |
| -------- | --- |
| To:      | {{Product Owner}} |
| Subject: | {{Client Name}}: Sprint XXX Forecast |
::: email-content  

### Hi {{Product Owner}},

Sprint Goals (in priority order):

* Bugfixes
* WDM Integration
* SSO/Roles APIs
* Download Documents APIs

Please see below for a more detailed breakdown of the upcoming Sprint:

| **Current Sprint:**    | **{{ SPRINT NUMBER }}**      |
| ---------------------- | ------------------------------ |
| Sprint Duration:       | {{ NUMBER OF WEEKS }}        |
| Project:               | {{ PROJECT NAME }}           |
| Project Portal:        | {{ LINK TO PROJECT PORTAL }} |
| Product Owner:         | {{ PRODUCT OWNER NAME }}     |
| Sprint Review Meeting: | {{ DATE AND TIME }}          |
| Attendees:             | {{ NAMES OF THE ATTENDEES }}     |

As per our Sprint Planning Meeting, and as the Product Owner, you have agreed to the following Product Backlog Items (PBIs) being included in the current Sprint backlog.

The Team will do its best to deliver this set of features (Scope), to a defined quality standard (Definition of Done) by the end of the Sprint. Ideally, the team will deliver what they forecast, or even a bit more, but this can't be guaranteed.

| **ID** | **Title**                           | **State** | **Effort** |
| ------ | ----------------------------------- | --------- | ---------- |
| 24124  | UI Improvements                     | Done      | 4          |
| 24112  | Integrate Business Logic to MVC app | Done      | 8          |
| 24097  | Styling                             | Committed | 16         |

**Figure: The Sprint Backlog**

&lt;This is as per rule: [Do you create a Sprint Forecast?](/sprint-forecast)&gt;

:::
:::
::: good
Figure: Good example - Copy this as email template and send to Product Owner
:::

::: info
**Tip:** You can copy and paste the Sprint Backlog as a table into the email body:

1. Go to Azure DevOps and navigate to the Sprint's Backlog view  
   E.g. `https://dev.azure.com/ssw/Northwind/_sprints/backlog/Northwind%20Team/Northwind/Sprint%201`
2. Remove the unnecessary columns so it looks clean
3. Select all items, copy, then paste into the Sprint Forecast email
:::
