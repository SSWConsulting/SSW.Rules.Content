---
type: rule
title: Scrum – Do you know where to discuss the backlog?
uri: discuss-the-backlog
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Goldman
    url: https://ssw.com.au/people/matt-goldman
related: []
redirects:
  - do-you-know-where-to-discuss-the-backlog
created: 2020-09-24T03:52:45.000Z
archivedreason: null
guid: de9846d4-5b51-417b-afdc-946cc096243e
---

When discussing a PBI/Issue, Pull Request, or a project in general, it is important to do it in the right place.

![](Kanban-on-Screen.jpg)  

<!--endintro-->


::: bad  
![Figure: Bad Example – don't use emails to discuss tasks](bad-mention-pbi.jpg)  
:::

### For code

Sometimes developers need to discuss code implementations - sometimes to improve the code, other times to explain why something was done a certain way.

This should be done in the Pull Request, if possible comment directly on the line of the code change and once resolved, make sure that the important information is captured in the merge's commit description.


::: good  
![Figure: You can add a comment on a specific line of code](comment on code in pull request.png)  
:::

### For a new PBI/Issue


As per[Do you know when you use @ mentions in a PBI?](/when-you-use-mentions-in-a-pbi) - Create a new issue mentioning the Product Owner and the related people




::: good  
![Figure: Good Example - When adding a GitHub issue, @ mention the Product Owner and other related people so they receive a notification e.g, an email](Create-Issue.png)  
:::

### For an existing PBI/Issue

Discuss it in the existing PBI/Issue.


::: good  
![Figure: You can discuss an existing issue, even when it has been closed](existing issue discussion.png)  
:::

### For other topics (brainstorm ideas, general discussion, etc.)

You can:

* Create a PBI/Issue
    * use a "discussion" label so that others know that it is just a discussion point and not actionable work yet
    * have it checked by the client before publishing it (recommended)
* Discuss it in the discussion tab in GitHub



::: good  
![Figure: You can create discussions on your project using the Discussion tab in your GitHub repository](Discussion Tab in GitHub.png)  
:::

* In the team channel in Teams



::: good  
![Figure: You can discuss your idea in Teams on the team channel](Team channel.png)  
:::

In summary, Email should be the last resort.
