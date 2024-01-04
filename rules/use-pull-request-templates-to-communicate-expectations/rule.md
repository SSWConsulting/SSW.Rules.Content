---
type: rule
title: Do you use Pull Request templates to communicate expectations?
uri: use-pull-request-templates-to-communicate-expectations
authors:
  - title: Gordon Beeming
    url: https://www.ssw.com.au/people/gordon-beeming
  - title: Alex Rothwell
    url: https://www.ssw.com.au/people/alex-rothwell
  - title: Brady Stroud
    url: https://ssw.com.au/people/brady-stroud
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Seth Daily
    url: https://ssw.com.au/people/seth-daily
created: 2023-09-06T16:24:00.000Z
guid: 8e378b56-3161-4433-81c0-40119075d137

---

Pull Request templates are a great way to communicate expectations to developers. You should can create different PR templates for different types of PRs. For example, you can have a PR template for bug fixes, a PR template for new features, and a PR template for refactoring. You are also able to create specific PR templates for specific code paths.

You can read more about PR templates in the GitHub docs at [Creating a pull request template for your repository](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)

<!--endintro-->

When creating a PR template, think of how you can help developers create great PRs

::: bad  
![Figure: Bad example - There is no information to guide developers](no-pr-template.jpg)  
:::

::: ok  
![Figure: OK example - The PR template contains handy links to guidance for creating great PRs ⭐](pr-template-with-comments-to-guidance.jpg)  
:::

::: good  
![Figure: Good example - This PR template asks for **context needed to review**, along with links to guidance for creating great PRs ⭐](pr-template-asking-for-context.jpg)  
:::

**Tip:** You can use comments in the markdown as above. These comments will not show when the PR is created, and is only visible when editing the description.
 
For a great Pull Request template, take a look at [@SSWConsulting/SSW.GitHub.Template](https://github.com/SSWConsulting/SSW.GitHub.Template/blob/main/.github/pull_request_template.md)
