---
seoDescription: Set default permissions for all new GitHub repositories and streamline your workflow with automated repository creation.
type: rule
archivedreason:
title: Do you set default permissions for all new repositories?
guid: 6db01da5-81e9-43c8-8916-19d0161db58d
uri: set-default-permissions-for-new-repositories
created: 2021-03-08T15:13:00.0000000Z
authors:
  - title: Brady Stroud
    url: https://www.github.com/bradystroud
related: []
redirects: []
---

Using GitHub Webhooks, you can set some default permissions for every new repository inside an organisation.

You can use the [repository event](https://docs.github.com/en/developers/webhooks-and-events/webhook-events-and-payloads#repository) to trigger a GitHub action to set the permissions.

See the GitHub docs [Permissions API](https://docs.github.com/en/rest/reference/actions#permissions)

<!--endintro-->

::: todo
Add example of a GitHub action that sets the permissions
:::

By adding this to your organisation,
every new repo will already have the optimal permissions and privileges.
