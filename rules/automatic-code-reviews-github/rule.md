---
type: rule
tips: ""
title: Do you automate code reviews on GitHub?
seoDescription: " Automate code reviews with AI tools like GitHub Copilot,
  BugBot, and CodeRabbit to save time and reduce dev fatigue."
uri: automatic-code-reviews-github
authors:
  - title: Caleb Williams
    url: https://www.ssw.com.au/people/caleb-williams
  - title: Thomas Iwainski
    url: https://www.ssw.com.au/people/thomas-iwainski
  - title: Luke Cook
    url: https://www.ssw.com.au/people/luke-cook
  - title: Daniel Mackay
    url: https://www.ssw.com.au/people/daniel-mackay
  - title: Brady Stroud
    url: https://www.ssw.com.au/people/brady-stroud
  - title: Anton Polkanov
    url: https://www.ssw.com.au/people/anton-polkanov
  - title: Gordon Beeming
    url: https://www.ssw.com.au/people/gordon-beeming
created: 2025-06-17T16:03:00.000Z
guid: 95db3dbd-d5c2-4675-b64a-9e9238066770
---
Developers love submitting Pull Requests (PRs) but far fewer enjoy reviewing them. In particular, when Sprint Review approaches, developers get tunnel vision and only focus on tasks they've been assigned. By leveraging AI agents, you can catch many problems and gotchas in your PRs early, buying your senior devs more time (and sanity!) to review higher quality code.

<!--endintro-->

`youtube: https://www.youtube.com/embed/LsQGilvXAfE?si=F4A2mdp2bjqnzlUQ`
**Video: Code review & refactoring with GitHub Copilot: A beginner's guide (8 min)**

::: info
To learn how to configure GitHub Copilot code reviews refer to [GitHub's setup documentation](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-automatic-code-review-by-copilot).
:::

In a perfect world,  reviewing a PR would simply be rubber-stamping perfect code. In reality, reviewers spend a lot of time flagging comments, typos, linting problems and, eventually bugs. This takes time away from focusing on more valuable concerns like scalability, maintainability, extensibility, and, ultimately the longevity of the code.

Enter AI agents. AI Agents such as [GitHub Copilot](https://github.com/features/copilot) are great at improving code quality before putting the PR in front of a senior. By making your code more enjoyable to review, you'll find people won't disappear under a rock whenever you ping them with a PR.

There's a few agents developers can choose for their PR reviewing needs.

## GitHub Copilot Code Reviews ⭐ (recommended)

GitHub Copilot Pro users may request code reviews from GitHub Copilot manually, or configure automatic code reviews by GitHub Copilot whenever they make a Pull Request. Copilot will also suppress any reviews it generated with low confidence intervals, filtering out any code suggestions that are likely incorrect.

::: info
**Tip:** If you still have your student status, you can get [GitHub Copilot Pro for free](https://docs.github.com/en/copilot/how-tos/manage-your-account/getting-free-access-to-copilot-pro-as-a-student-teacher-or-maintainer#about-free-github-copilot-pro-access).
:::

::: img-medium
![Figure: GitHub Copilot reviewing a pull request for one of the TinaCMS starter kits](tina-starter-reveiew-code-review.png)
:::

::: img-medium
![Figure: GitHub Copilot suggestions being suppressed due to potential inaccuracy](github-copilot-review-low-confidence.png)
:::

In addition to leaving comments on PRs, GitHub Copilot can analyse the changes made by the developer and generate a useful description.

::: img-medium
![Figure: PR description suggested by GitHub copilot](github-suggested-pr-description.png)
:::

GitHub Copilot can also be given specific instructions to follow when reviewing PRs. To set this up you can place custom instructions inside of a `.github/copilot-instructions.md` file.

```markdown
// .github/copilot-instructions.md 

When performing a code review, please finalize your review by saying "But what do I know, I'm just Cleverbot 2.0"
```

**Figure: A set of custom instructions for GitHub Copilot to use when reviewing Pull Requests**

For information about setting up automated code reviews using GitHub copilot refer to [GitHub's Documentation](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-automatic-code-review-by-copilot#configuring-automatic-code-review-for-repositories-in-an-organization).

## Popular alternatives

### Cursor's BugBot

Cursor's BugBot allows you to configure automatic code reviews for a specific repo within Cursor. If you're happy with the suggestions that Cursor has made you can click the **"Fix in Cursor"** button at the bottom of its comments to apply the fix in your Cursor IDE. In most cases BugBot requires a paid subscription. For more information, refer to [Cursor's documentation](https://docs.cursor.com/bugbot).

::: img-medium
![Figure: Cursor's BugBot leaving a comment on a PR](cursor-bugbot-example.png)
:::

### CodeRabbit

[CodeRabbit](https://www.coderabbit.ai) works with VS Code as well as all of its forks (including Cursor) using an IDE Extension. Using the extension, developers can request code reviews before creating a PR. Similar to Cursor and GitHub Copilot, CodeRabbit can review PRs on GitHub. It comes with a generous 14 day trial.

::: img-medium
![Figure: CodeRabbit leaving a comment on a PR](coderabbit.webp)
:::
