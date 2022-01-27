---
type: rule
title: Do you estimate all tasks at the start of the sprint?
uri: do-you-estimate-all-tasks-at-the-start-of-the-sprint
authors:
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
related:
  - do-you-use-the-best-deployment-tool
  - do-you-know-when-to-use-an-on-premises-build-server-with-visual-studio-online
redirects: []
created: 2014-01-09T01:21:38.000Z
archivedreason: null
guid: 16b13572-063c-4e7f-88e8-f6403e0550ea
---

In Scrum it's important to flesh out the details of a PBI when it makes sense to do so.

You should estimate your PBIs as soon as you can, but you don't need to break all of your PBIs down into fully-estimated tasks as soon as they're added to the backlog.

However, before starting work on a Sprint, you should always break the PBIs in that sprint into estimated tasks.

<!--endintro-->

Azure DevOps can use the remaining hours assigned to Tasks to calculate the burndown. By breaking the PBIs down into tasks with estimates, your burndown will start looking correct right from the first day of the sprint.

::: bad
![Figure: Bad Example - The tasks weren't estimated at the start of the sprint](burndown_bad_example.png)
:::

::: good
![Figure: Good Example - The tasks were estimated from day one](burndown_good_example.png)
:::

**Note:** If you're not using Task estimates, you can configure Azure DevOps to create a Sprint Burndown using PBI Effort instead.
