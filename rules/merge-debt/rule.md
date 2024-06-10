---
seoDescription: Learn how to avoid merge debt by ensuring PRs don't stay open for too long, conducting daily reviews, and facilitating "over-the-shoulder" reviews.
type: rule
title: Do you avoid Merge Debt?
uri: merge-debt
authors:
  - title: Brook Jeynes
    url: https://www.ssw.com.au/people/brook-jeynes
  - title: Gordon Beeming
    url: https://ssw.com.au/people/gordon-beeming
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related:
  - over-the-shoulder
redirects: []
created: 2023-08-14T00:00:00.000Z
archivedreason: null
guid: aa0d5e6d-f08a-43cd-9bee-4f72df367b78
---

If you are in a team (i.e. an internal contributor), it is the PR author's responsibility to get a PR reviewed and action feedback ASAP.  
As an internal contributor, it's a good idea to have a [call with the PR reviewers](/over-the-shoulder).

If you are **not** part of the team (i.e. an outside contributor), reviewing the PR is the responsibility of the repo maintainers. Actioning the feedback is still the responsibility of the PR author.
As an outside contributor, it's a good idea to chase the reviewers by reaching out with a comment on GitHub, or through the repo's community (e.g. Discord channels).

<!--endintro-->

::: info
**Note:** Remember that before declaring a task 'Done' with a link, your [changes should be live](/include-links-in-emails/#ensure-your-changes-are-live) for verification.
:::

When a PR is created but left open for a long time, it becomes stale. Stale PRs equate to merge debt because the longer the PR stays open, the more changes occur on the main branch and the harder it is to merge back in.

Merge debt refers to the amount of work a PR has to undergo before it can be merged into the main branch. If the PR is brand new, the amount of work required to merge is near to none, but as the PR stays open, the more work gets done on the main branch, leading to more work needing to be done to ensure the PR is up-to-date and able to be merged.

Merge debt can be avoided by:

* Ensuring PRs don't stay open for too long - you could use [SSW Dory](http://www.sswdory.com) to automatically inform you of any outstanding PR's.
* Conducting daily reviews on repos to ensure all PRs that can be merged are merged
* Ensuring that once a PR is ready to be merged, an "over-the-shoulder" review occurs

::: bad
![Figure: Bad example - Pressing commit and forgetting about it. PR has been left open for a over 2 weeks](https://github.com/SSWConsulting/SSW.Website-v3/assets/25432120/5a67d6ed-a301-4d72-af00-8da4277c1b75)
:::

::: good
![Figure: Good example - Devs reviewing a PR on a call - no merge debt!](over-the-shoulder-pr.png)
:::
