---
type: rule
title: Do you know how to update a GitHub issue?
uri: update-a-github-issue
authors:
  - title: Brook Jeynes
    url: https://www.ssw.com.au/people/brook-jeynes/
related:
  - when-you-use-mentions-in-a-pbi
  - close-pbis-with-context
created: 2023-10-03T00:48:22.310Z
guid: cec9aa77-4234-470b-bcab-557b39de6789
---
As issues evolve, it's common for their initial descriptions to become outdated or for significant developments to occur that must be recorded for the benefit of the entire team.

<!--endintro-->

Whenever an issue necessitates an update, the team should add a comment to the issue, detailing the change or event. 

::: good

![Figure: Extra context added via comment.](good-example-adding-context-via-comment.png)

:::

In cases where an update is long standing or important, it should be appended to the bottom of the issue description. This update must include the date it was made, serving as a chronological record of changes. In addition, a comment should be left on the issue thread to inform team members that significant information has been added to the issue.

This does not include changes regarding to who is currently working on the issue. GitHub and Azure DevOps both track via some version of an “Assignees” tag.

::: good

![Figure: Important information added to the issue itself with a comment.](good-example-update.png)

:::

It's also important to CC anyone who may need to see this additional information.

::: good

![Figure: Important users CC'd within the issue but addressed to the team.](good-example-cc-in-issue.png)

:::

::: good

![Figure: Important users CC'd within comments added extra context.](good-example-cc-in-comment.png)

:::