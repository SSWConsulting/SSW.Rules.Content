---
type: rule
archivedreason:
title: How to set up GitHub scrum workflow
guid: e63da194-c5d2-4830-9106-d164aafcddb5
uri: do-you-know-the-how-to-set-up-github-workflow
created: {date_created}
authors: []
related:

---
### How to set up GitHub scrum workflow

There are several ways of turning your GitHub repository into a simple but powerful agile work environment, the following is the recommended:

<!--endintro-->

#### How it works

- Product Backlog Items (PBIs) are reported as **issues**
- Points and meta data are assigned to items as **labels**
- **milestones** are used to group issues in Sprints

#### 1. Create issues as backlog items

To create a new backlog item, just create a new issue.

Once a new issue has been created, assign it the right labels and/or assign it to a sprint (milestone).

Issues allow you to have a conversation about the item and even allow you to create task lists inside the issue using [GitHub's markdown](https://guides.github.com/features/mastering-markdown/).

#### 2. Add labels to issues

Add the following labels to your repository:

### Estimates

`estimate` labels allow you to set estimates in your backlog e.g.:

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

### Types

`type` labels allow you to easily filter items (issues) in the dashboard e.g.:

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

#### 3. Define sprints as milestones

You can create a milestone for every sprint and add items (issues) from the backlog to a milestone.

This allows you to group items in sprints and track them by milestone in your [issue dashboard](https://github.com/issues).

The backlog then consists of all items (issues) that have no `milestone` attached to it.

**TIP**: Use `no:milestone` in the search field on your [issue dashboard](https://github.com/issues) to find backlog items.


