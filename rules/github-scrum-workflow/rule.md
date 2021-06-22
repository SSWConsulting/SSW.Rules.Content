---
type: rule
archivedreason:
title: How to set up GitHub Scrum workflow
guid: e63da194-c5d2-4830-9106-d164aafcddb5
uri: do-you-know-the-how-to-set-up-github-workflow
created: 2021-06-21T06:44:34.0000000Z
authors:
  - title: Tom Bui
    url: https://www.ssw.com.au/people/tom-bui
related: []

---
### How to set up GitHub Scrum workflow

There are several ways of turning your GitHub repository into a simple but powerful agile work environment, the following is the recommended:

<!--endintro-->

Based on [GitHub Scrum workflow](https://github.com/jvandemo/github-scrum-workflow)

#### How it works

- Product Backlog Items (PBIs) are reported as **issues**
- Points and meta data are assigned to PBIs as **labels**
- **milestones** are used to group issues in Sprints

#### 1. Create issues as Product Backlog Items

To create a new backlog item, it is best practice to configure GitHub issue templates for your repository 

Issue templates configuration guide can be found at [Configuring issue templates for your repository](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)

Assign the issue the right labels and/or assign it to a Sprint (milestone).

Issues allow you to have a conversation about the item and even allow you to create task lists inside the issue using [GitHub's markdown](https://guides.github.com/features/mastering-markdown/).

#### 2. Add labels to issues

Add the following labels to your repository:

### Estimates

`estimate` labels allow you to set estimates in your backlog:
e.g.:
| Label        | Time Estimate |
| -------------|:-------------:|
| `estimate: 1` | trivial |
| `estimate: 2` | 1 hour |
| `estimate: 3` | 2 hours |
| `estimate: 5` | 4 hours |
| `estimate: 8` | 1 day |
| `estimate: 13` | 1.5 days |
| `estimate: 21` | 3 days |
| `estimate: 34` | 1 week |

Your actual estimates should align with https://www.ssw.com.au/rules/estimating-do-you-know-how-to-size-user-stories-effectively

### Types

`type` labels allow you to easily filter PBIs (issues) in the dashboard e.g.:

| Label | Type |
| ------| :----|
| `type:bug`| bug |
| `type:chore`| chore, maintenance work |
| `type:feature`| new feature |
| `type:infrastructure` | infrastructure related |
| `type:performance` | performance related |
| `type:refactor` | refactor |
| `type:test` | test related |

### Other

You can define and assign custom labels that you need within your workflow or organization.

#### 3. Define Sprints as milestones

You can create a milestone for every Sprint and add Product PBIs (issues) from the backlog to a milestone.

This allows you to group PBIs in Sprints and track them by milestone in your [issue dashboard](https://github.com/issues).

The backlog then consists of all PBIs (issues) that have no `milestone` attached to it.

**TIP**: Use `no:milestone` in the search field on your [issue dashboard](https://github.com/issues) to find PBIs.

