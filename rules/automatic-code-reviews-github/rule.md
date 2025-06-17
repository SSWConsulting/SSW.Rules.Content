---
type: rule
tips: ""
title: Do you request automatic reviews on GitHub?
uri: automatic-code-reviews-github
authors:
  - title: ""
guid: 95db3dbd-d5c2-4675-b64a-9e9238066770
---
Developers love writing PRs but often don't like reviewing them. In particular, when the sprint review starts to rear it's head on the horizon developers get tunnel vision and only focus on tasks they've been assigned. By leveraging AI agents, code reviews go from being lengthy, tedious, annoying distractions for senior developers, to a quick glance at the code followed by an "LGTM ✅".

`youtube: https://www.youtube.com/embed/cyPaAkRfEBQ`
**Video: GitHub Copilot code review**

<!--endintro-->

In a perfect world,  reviewing a PR would be nothing more than a last minute glance at a few commits to ensure there's nothing fishy going on. You've got [automated testing](https://www.ssw.com.au/rules/automated-ui-testing/) in your CI/CD pipeline are there to flag any regressions in existing functionality and you've got a Staging environment to preview how things are going to look. However in a world where a Stakeholders often ask for features yesterday that they wanted finished last week, automated testing often gets left by the wayside and Senior developers can find themselves in a crunch to get things across the line even without any distractions. 

Enter AI agents. AI Agents such as GitHub Copilot are now not only capable of structuring an MVP while you grab a cup of coffee, but they can also leverage their mountains of expertise to review PRs. This isn't a substitute for having a tech lead or a senior around to review your PRs, but it's an extra circle of hell rubbish code needs to crawl through before worming it's way into prod.


There's a few agents developers can choose for their PR reviewing needs.

### GitHub Copilot (Recommended)


GitHub Copilot Pro users may request code reviews from GitHub Copilot manually, or configure automatic code reviews by GitHub copilot whenever a pull request is made. GitHub Copilot reviews can automatically be triggered on your various code repos.





#### Repo level (⭐Recommended)

When configuring GitHub copilot to review at the repo level, any pull requests made to a target branch (ususally master) will trigger a review from GitHub copilot.

Code review rules can be fine tuned totrigger on specific branch patterns. 

#### Account

GitHub copilot pro users have the option of enabling GitHub copilot time.

#### Organization Level

GitHub Copilot may be configured to automatically review PRs and provide suggestions at the GitHub organization level. This is however only available for public repos, unless your organization is on the Team plan.


#### Limitations

* Can only be configured on a per repo level

::: img-medium
![Figure: Automatic code review on Tina.io using GitHub Copilot](auto-code-review-tina.png)
:::

::: img-medium
![Figure: Automatic code review for YakShaver using GitHub Copilot](yakshaver-code-review.png)
:::

### Cursor's BugBot

Cursor's BugBot allows you to configure automatic code reviews for a specific repo withing Cursor. If you're happy with the suggestions that Cursor has made you can click the "Fix in Cursor" button at the bottom of it's comments to apply the fix in your Cursor IDE. BugBot requires a subscription, but is available as part of a 7 day free trial.

::: img-medium
![Figure: Cursor's BugBot Leaving a comment on a PR](cursor-bugbot-example.png)
:::

### CodeRabbit

Code Rabbit works with VS Code as well as all of it's forks using an IDE Extension. Using the extension developers can request code reviews before creating a PR. Similar to Cursor and GitHub Copliot, CodeRabbit can review PRs on GitHub. It comes with a generous 14 day trial, with paid plans beginning at $12 per month.


::: img-medium
![Figure: CodeRabbit leaving a comment on a PR](coderabbit.webp)
:::
