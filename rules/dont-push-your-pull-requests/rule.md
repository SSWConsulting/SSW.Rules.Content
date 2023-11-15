---
type: rule
title: Do you know to not 'push' your Pull Requests? (aka Discuss, then build)
uri: dont-push-your-pull-requests
authors:
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
related: []
redirects:
  - do-you-know-to-not-push-your-pull-requests-a-k-a-discuss-then-build
  - do-you-know-to-not-push-your-pull-requests-(a-k-a-discuss-then-build)
created: 2016-03-29T18:35:55.000Z
archivedreason: null
guid: 4a8b579b-c602-429c-84f2-0f306d7ab9c3

---

For the original article check out [Don't "Push" your Pull Requests](https://www.igvita.com/2011/12/19/dont-push-your-pull-requests/)by Ilya Grigorik.

Open source software projects love it when the community get involved and pitch in.

It's great when someone fixes a bug. A short Pull Request to fix a small problem is easy to review and accept.

<!--endintro-->

It's great when someone adds a much-needed feature...   
...as long as the feature fits in with the project the core contributors have for the project...   
...and it meets the existing coding patterns and engineering standards.

This is where frustration often starts to set in on open source projects.

A contributor has a great idea for a feature, or identifies an area where they can add value and does so without consulting with the core contributors who have often spent hundreds of hours working on the project.

Their contribution might solve their problem, but after it has been accepted it will most likely be left for the core contributors to maintain.

::: greybox

**Poor Communication Contribution**

* Developer has good idea for project
* Bashes away and writes 600 lines of code
* Submits Pull Request
* Core contributor looks at large PR
  * They don't fully understand purpose of request / the problem it solves
  * They don't like that the PR author hasn't followed the existing coding standards
  * They make a push back comment

:::

::: bad
Figure: Bad example - Poor early communication can lead to mis-directed work and pull requests not being accepted  
:::

::: greybox

**Good Communication Contribution**

* Developer (PR Author) has good idea for project
* Reviews the list of outstanding issues for the project and confirms that someone hasn't already had the same idea and started a discussion on it
* Author creates an issue on GitHub and outlines the problem they are trying to solve, and outlines their suggested solution
* The core contributors and other interested parties can help refine both the idea for the feature and the suggested implementation
* The author can then start working on the feature knowing that their idea for the project complies with the maintainers vision for the project and know it is likely to be merged into the core codebase

:::

::: good
Figure: Good example - Good communication leads to collaboration and better outcomes for the author and the project  
:::
 
::: info

**Projects with Internal Teams**

* Internal team members should only work on features during work hours that have been assigned to a release by the core contributors for a project
* Features will be assigned to a release during the Community Standup

:::
