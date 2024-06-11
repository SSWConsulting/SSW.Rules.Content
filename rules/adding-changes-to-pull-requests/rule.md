---
seoDescription: When to add changes to an existing pull request - Ensure correct, necessary, and beneficial updates to the project while considering expertise and project standards.
type: rule
title: Do you know when to add your changes to an existing PR?
uri: adding-changes-to-pull-requests
authors:
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
  - title: Tiago Araujo
    url: https://www.ssw.com.au/people/tiago-araujo
related:
  - github-content-changes
  - rubber-stamp-prs
created: 2023-03-22T14:08:29.478Z
guid: d43d618e-9c54-4cfc-899b-232fd5bccd36
---

Pull requests are a fundamental feature of collaborative software development, allowing contributors to propose changes to a project and receive feedback from other developers. When reviewing a pull request, it can be tempting to make additional changes beyond those requested by the PR creator.

Certain projects (E.g. SSW.Rules) [allow these additional edits](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/allowing-changes-to-a-pull-request-branch-created-from-a-fork), without the need for extra reviews by someone else. Knowing that, it's crucial to make sure the changes are **correct**, **necessary** and **beneficial** to the project before adding them.

<!--endintro-->

Most common scenarios where editing an existing PR is encouraged:

* Fixing typos
* Grammar improvements
* Formatting (Markdown) fixes/improvements

For the cases where your wanted change can serve as a learning opportunity to others, it is always best if you ask them to action by [requesting a change](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request). This way the extra change can be avoided in the future.

::: info
**Warning:** Only experts should include their own changes to an existing PR. \
Never add extra changes to a PR if you are less experienced or unfamiliar with the project. The additional changes may be unnecessary or even harmful!
:::

Ultimately, the decision to add additional changes to a pull request should be made based on the needs of the project and the expertise of the contributors involved. It's important to carefully consider the impact of any additional changes and ensure that they are aligned with the project standards.
