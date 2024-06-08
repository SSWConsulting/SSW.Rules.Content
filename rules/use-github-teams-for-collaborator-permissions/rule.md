---
type: rule
archivedreason:
title: GitHub - Do you use GitHub teams for collaborator permissions?
guid: e7f5cfe1-aa86-41ef-bc27-d367b2e36420
uri: use-github-teams-for-collaborator-permissions
created: 2021-03-08T15:13:00.0000000Z
authors:
  - title: Brady Stroud
    url: https://www.ssw.com.au/people/brady-stroud
  - title: Gordon Beeming
    url: https://www.ssw.com.au/people/gordon-beeming
related:
 - when-you-use-mentions-in-a-pbi
 - limit-admin-access
redirects: 
 - use-teams
---

You can use teams within a repository to manage a whole group's permissions instead of setting permissions for each new member of the organisation.

See [Organizing members into teams](https://docs.github.com/en/github/setting-up-and-managing-organizations-and-teams/organizing-members-into-teams).

::: good
![Figure: Good example - Using a good teams structure to organize access](GoodExampleUsingTeams.png)
:::

Correctly configuring your organisation's teams structure will make it easy to give members the permissions level that they need. You can add teams to repositories to manage their roles.

::: good
![Figure: Good example - Using teams to assign roles in a repository](TeamsOnRepo.png)
:::

<!--endintro-->

Another benefit of using teams is that you can mention a whole team in a discussion instead of individual members. See [Mentioning people and teams](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax#mentioning-people-and-teams)

#### Use teams as maintainers over individuals

When you add a team to a repository, you can give the team a role that determines their access level to the repository. You can also add teams to issues and pull requests to manage their access to those resources. Often individuals are added to repositories as administrators, but this is not a good idea as it gives them destructive access to the repository. Instead, add a team to the repository and give the team the maintainer role.

::: bad
![Figure: Bad example - Individuals should not have Admin access to a repository](individuals-added-as-admins.png)
:::


::: good
![Figure: Good example - Teams should have Maintainer access to a repository](teams-added-as-maintainers.png)
:::
