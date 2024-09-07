---
seoDescription: Include URLs in tasks and "Done" emails to enhance transparency and collaboration by providing easy access to relevant information.
type: rule
title: Do you include URLs in tasks and "Done" emails?
uri: include-links-in-emails
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Cameron Shaw
    url: https://ssw.com.au/people/cameron-shaw
  - title: Ulysses Maclaren
    url: https://ssw.com.au/people/ulysses-maclaren
related:
  - add-context-reasoning-to-emails
  - dones-do-you-include-useful-details-in-your-done-email
redirects:
  - dones-do-your-done’s-include-a-url
  - dones-do-your-dones-include-a-url
created: 2009-12-10T06:55:30.000Z
archivedreason: null
guid: ed0fa76a-418b-4b59-9e3b-2544c08b910e
---

Always include the relevant URL to your emails, like when you want to request or just made a change to a webpage or document. This way people can easily check the details of the tasks. This is especially important for ["Done" emails](/reply-done-and-delete-the-email).

If you are using a task tracking system like **Azure DevOps**, **GitHub**, or Jira, also include the link to the PBI/Issue/task.

<!--endintro-->

::: info
**Tip:** It is [important to give context and reasoning](/do-you-add-context-reasoning-to-your-emails) to your emails too.
:::

::: greybox
Done
:::
::: bad
Figure: Bad example - How can we check the task was done correctly?
:::

::: greybox
Done - northwind&#46;com/about-us

:::
::: good
Figure: Good example - Easy to check what was done
:::

::: greybox
Done - northwind&#46;com/about-us/ as requested on ssw2&#46;visualstudio&#46;com/Northwind/\_workitems/edit/00001
:::
::: good
Figure: Good example - Easy to check what was done + includes the context of the task within the Sprint
:::

### Ensure changes are live

Before declaring a task 'done' with a link, ensure that your changes are live and accessible for verification.

::: info
**Note:** It is the PR author's responsibility to [avoid merge debt](/merge-debt) by getting the PR reviewed ASAP.
:::

#### Scenario: PR waiting for approval

::: greybox
Done - ssw&#46;com&#46;au/rules/dones-is-your-inbox-a-task-list-only
:::
::: bad
Figure: Bad example - Link is included but changes are not live yet
:::

::: greybox
Done - github&#46;com/SSWConsulting/SSW.Rules&#46;Content/pull/0001

:::
::: bad
Figure: Bad example - Using the PR link instead of the final page link
:::

::: greybox
(PR waiting for approval - github&#46;com/SSWConsulting/SSW.Rules.Content/pull/0001)  
Done - Changes will be on ssw&#46;com&#46;au/rules/dones-is-your-inbox-a-task-list-only

:::
::: ok
Figure: OK example - Changes are not live yet, but people are aware and have the links
:::

#### Scenario: PR is approved and merged

::: greybox
Done - ssw&#46;com&#46;au/rules/dones-is-your-inbox-a-task-list-only
:::
::: good
Figure: Good example - Final link is included and changes are live to be checked
:::

### Ensure others have permissions

It is a common problem where someone CC'd will not have permissions to see a file and the sender knows this. You should still add the link but inform the recipient.

#### Scenario: Recipient doesn't have permissions

::: greybox
Done - onedrive.live.com/file-name.xls
:::
::: bad
Figure: Bad example - Link is included but recipient won't be able to open it, potentially generating more emails
:::

::: greybox
(link for reference - you don't have permissions)  
Done - onedrive.live.com/file-name.xls
:::
::: good
Figure: Good example - Link is included and people are aware of permission issues
:::

**Video:** [Top 10+ Rules to Better Email Communication with Ulysses Maclaren](https://www.youtube.com/watch?v=LAqRokqq4jI)
