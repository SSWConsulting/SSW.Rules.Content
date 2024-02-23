---
type: rule
title: Do you configure your GitHub Notifications?
uri: github-notifications
authors:
  - title: Luke Parker
    url: https://ssw.com.au/people/luke-parker
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Bryden Oliver
    url: https://ssw.com.au/people/bryden-oliver
related: []
created: 2022-03-03T12:25:15.000Z
archivedreason: null
guid: 10489ca4-5e42-49af-b502-d3572d573e7f
---
Notifications from GitHub can be quite a pain, as they send a lot of emails. This leads to many developers ignoring the important emails they receive.

`youtube: https://www.youtube.com/embed/Lb1slP9jSGk`

<!--endintro-->

::: bad
![Figure: Bad example - lots of notifications](./notifications.png)
:::

To reduce this spam and to make the notifications have value, make sure to configure your [GitHub Notifications](https://github.com/settings/notifications). 

::: good
![Figure: Good example - Turn off Watching settings](watching-notification.png)
:::

Turning off Watching notifications significantly reduces the number of spam emails you receive. With this setting, you won't get notified about actions like PR approvals or comments that aren't related to you.

::: good
![Figure: Good example - Workflow notification settings](actions-notification.png)
:::

The important one here is to make sure the item marked **Send notifications for failed workflows only** is checked, so that you receive emails for failures in your deployments.
