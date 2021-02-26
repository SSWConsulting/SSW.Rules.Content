---
type: rule
archivedreason: 
title: Do you create a Sprint Forecast? (aka The functionality that will be developed during the Sprint)
guid: f749bf03-8785-4433-a5c5-6c21cda9b782
uri: do-you-create-a-sprint-forecast-aka-the-functionality-that-will-be-developed-during-the-sprint
created: 2010-12-02T03:53:59.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-create-a-sprint-forecast-(aka-the-functionality-that-will-be-developed-during-the-sprint)

---

After the [Sprint Planning](/do-you-know-what-happens-at-a-sprint-planning-meeting)[Meeting](/do-you-know-what-happens-at-a-sprint-planning-meeting), it is useful for the Development Team to send the Product Owner (PO) a Sprint Forecast for the next Sprint. Doing this helps to improve common understanding in, and sometimes to enforce, the relationship between the PO and the Team.



This is simply an agreement between the Development Team and the PO for one Sprint and should be confirmed via an e-mail at the beginning of every Sprint.


<!--endintro-->


> “The implementation team agrees to do its best to deliver an agreed on set of features (scope) to a defined quality standard by the end of the sprint. (Ideally they deliver what they promised, or even a bit more.) The Product Owner agrees not to change his instructions before the end of the Sprint.”
> 
> **- Agile Project management**


Each of the Sprints in a Scrum project can be considered a mini-project that has Time (Sprint Length), Scope (Sprint Backlog), Quality (Definition of Done) and Cost (Team Size\*Sprint Length). Only the scope can vary and this is measured every sprint.

::: email-template  
|          |     |
| -------- | --- |
| To:      | [Product Owner] |
| Subject: | <Client Name>: Sprint xxx Forecast |  
::: email-content  

**Hi [Product Owner],**

| Current Sprint: | [Sprint Number] |
| --- | --- |
| Sprint Duration: | [Number of weeks] |
| Sprint Goal: | [Main goal of Sprint] |
| Project: | [Project Name] |
| Project Portal: | [Link to project Portal] |
| Product Owner: | [Product Owner Name] |
| Sprint Review Meeting: | [Date and Time] |

Attendees: [Names of Attendees]

As per our Sprint Planning Meeting, and as the Product Owner, you have agreed to the following Product Backlog Items (PBIs) being included in the current sprint backlog.

The Team will do its best to deliver this set of features (Scope), to a defined quality standard (Definition of Done) by the end of the sprint. Ideally, the team will deliver what they forecast, or even a bit more, but this can't be guaranteed.

| **ID** | **Title** | **State** | **Effort** |
| --- | --- | --- | --- |
|     |     |     |     |
|     | &lt; generate this table as per the instruction on the rule below &gt; |   |   |
|     |     |     |     |

**Figure: The sprint backlog**

&lt;This is as per rule:        [https://rules.ssw.com.au/do-you-create-a-sprint-forecast-(aka-the-functionality-that-will-be-developed-during-the-sprint)](/do-you-create-a-sprint-forecast-aka-the-functionality-that-will-be-developed-during-the-sprint) /&gt;

:::  
:::  
::: good
 **Figure: Good Example - copy this as email template and send to Product Owner. 
** **Subject: &lt;Client Name&gt;: Sprint xxx Forecast** 
:::

Tip: Use this     [Outlook email template](https://github.com/SSWConsulting/SSW.Rules.Content/raw/main/rules/do-you-create-a-sprint-forecast-aka-the-functionality-that-will-be-developed-during-the-sprint/SprintContract.oft)

More instructions are as below:

1. Go to Azure DevOps and navigate to the current sprint's backlog view. E.g. `https://dev.azure.com/Northwind/ProjectName/\_sprints/backlog/Northwind/ProjectName/Sprint%201`
2. Paste to the Forecast email, and format the table:
    * Remove any useless columns!

::: good  
[Good Example of a Table](Sprint forecast example table.jpg)
:::

