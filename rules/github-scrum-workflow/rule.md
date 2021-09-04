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
related:
- do-you-create-a-sprint-forecast-aka-the-functionality-that-will-be-developed-during-the-sprint
- estimating-do-you-know-how-to-size-user-stories-effectively

---
### How to set up GitHub Scrum workflow

GitHub issues (classic) offers a great way to have an agile development process following a kanban process. Unfortunately it requires a bit of effort (or a 3rd party tool) to set it up for good Scrum.

<!--endintro-->

Based on [GitHub Scrum workflow](https://github.com/jvandemo/github-scrum-workflow)

#### How it works

- Product Backlog Items (PBIs) are reported as **issues**
- Points and metadata are assigned to PBIs as **labels**
- **milestones** are used to group issues in Sprints

#### 1. Create issues as Product Backlog Items

To create a new backlog item, it is best practice to configure GitHub issue templates for your repository. See [Configuring issue templates for your repository](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)

Make sure you assign suitable labels to the issue. Later on during the [Sprint Forecast meeting](https://www.ssw.com.au/rules/do-you-create-a-sprint-forecast-aka-the-functionality-that-will-be-developed-during-the-sprint), the issue should be prioritized and added to a Sprint (milestone) if appropriate.

Issues allow you to have a conversation about the item and even allow you to create task lists inside the issue using [GitHub's markdown](https://guides.github.com/features/mastering-markdown/).

#### 2. Add labels to issues

Add the following labels to your repository:

### Estimates

`estimate` labels allow you to set estimates in your backlog:
e.g.:
| Label        | Time Estimate |
| -------------|:-------------:|
| `estimate: 1` | 2 hour |
| `estimate: 2` | 4 hours |
| `estimate: 4` | 1 day |
| `estimate: 8` | 2 days |
| `estimate: 16` | 4 days |
| `estimate: 32` | 2 weeks |
| `estimate: 64` | 1 month |

Your actual estimates should align with the rule [Estimating - Do you know how to size Product Backlog Items (PBIs) effectively?](https://www.ssw.com.au/rules/estimating-do-you-know-how-to-size-user-stories-effectively)

### Types

`type` labels allow you to easily filter PBIs in the dashboard e.g.:

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

You can create a milestone for every Sprint and add Product PBIs from the backlog to a milestone.

This process allows you to group PBIs in Sprints and track them by milestone in your [issue dashboard](https://github.com/issues).

The backlog then consists of all PBIs that have no `milestone` attached to them.

**TIP**: Use `no:milestone` in the search field on your [issue dashboard](https://github.com/issues) to find PBIs.

See [Rules to Awesome Documentation](https://www.ssw.com.au/rules/awesome-documentation) to follow best practice setting up a projects README
