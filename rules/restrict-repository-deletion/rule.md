---
seoDescription: Prevent accidental GitHub repository deletions by restricting access to only organization owners.
type: rule
archivedreason:
title: Do you restrict repository deletion?
guid: 89bf3b1d-a3dd-4430-8a77-afb170184493
uri: restrict-repository-deletion
created: 2021-03-08T15:13:00.0000000Z
authors:
  - title: Brady Stroud
    url: https://www.github.com/bradystroud
related: []
redirects: []
---

When deleting GitHub repositories, it can be hard to tell if you are on a fork or the base repository as the interface is very similar. This can lead to accidental deletions of base repositories.

<!--endintro-->

To avoid this, the organisation owners should be the only members allowed to delete repositories. Follow these instructions:

1. Go to your organisation | Settings | Member privileges.
2. Under 'Repository deletion and transfer', ensure 'Allow members to delete or transfer repositories for this organization' is **deselected**
3. Save

See GitHub docs [Setting permissions for deleting or transferring repositories](https://docs.github.com/en/github/setting-up-and-managing-organizations-and-teams/setting-permissions-for-deleting-or-transferring-repositories)

This will ensure that even Admin users cannot accidentally delete or transfer repositories

::: good
![Figure: 'Allow members to delete or transfer repositories for this organization' is disabled](dontAllowDeletion.png)
:::
