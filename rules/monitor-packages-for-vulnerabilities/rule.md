---
type: rule
title: Do you monitor your application for vulnerabilities?
uri: monitor-packages-for-vulnerabilities
authors:
  - title: Chris Clement
    url: https://www.ssw.com.au/people/chris-clement
  - title: William Liebenberg
    url: https://www.ssw.com.au/people/william-liebenberg
related:
  - packages-up-to-date
  - do-you-make-sure-you-get-brownie-points
created: 2022-05-20T01:38:10.095Z
guid: b39cb829-e1b3-4e1d-b3c5-124c2e61720f
redirects:
  - monitor-packages-for-vulnerability

---
Using libraries as a building block for your project is a standard in modern software development. It's fairly normal to have 10+ npm and NuGet libraries used in a full-stack project.

One of the big challenges for developers to address is when this project has been delivered to the client and then gone to maintenance mode. With no developer actively working on the project, if there is a serious vulnerability discovered in a library referenced in the project (eg. `northwind/azure-helper@1.2.3`), no one will be aware of it, and it might cause some damage.

On the other hand, if you monitor the packages you have installed, you can notify the client, and it could [score you extra brownie points](https://www.ssw.com.au/rules/do-you-make-sure-you-get-brownie-points) and we have a duty of care to inform our clients.

## Level 0 - Manual tracking

List all installed packages in a file and cross-check with the [advisory board](https://github.com/advisories) and Google it, and change each lines regularly. Not recommended because this consumes time.

::: bad
![Figure: Bad Example - Tracking list of packages manually](screen-shot-2022-05-20-at-12.11.25.png)
:::

## Level 1 - Using tools to scan for vulnerabilities

Modern package managers such as npm or NuGet offers a way to check for vulnerabilities in the installed libraries. See [Do you keep your npm and yarn packages up to date?](https://www.ssw.com.au/rules/packages-up-to-date)

* npm: `npm audit` 
* yarn: `yarn audit` 
* dotnet cli: `dotnet list package --vulnerable`

Regularly running this command can give a summarised report on known vulnerabilities in the referenced libraries.

This is an improvement over manual tracking but still requires a developer to check out the latest code and then run the command.

::: ok
![Figure: OK Example - this npm audit command informs that there is 1 package with a high severity vulnerability](npm-audit-report.png)
:::

::: ok
![Figure: OK Example - this dotnet command informs that there is 1 package with a high severity vulnerability](dotnet-audit-report.png)
:::

## Level 2 - Automate vulnerability scanning (recommended)

Using 3rd party tools can help you to automate vulnerability scanning.

These tools will alert you whenever there's a security vulnerability detected in the project and optionally raise a PR for it.

Some of the available tools in the market:
- [Dependabot](https://github.com/dependabot) - free for all repositories under GitHub, easy to set up in the repository settings **(recommended)**. Used in [SSW Rules](https://www.ssw.com.au/rules/)
- [GitHub Enterprise Advanced Security](https://github.com/enterprise) - $ includes Dependabot plus additional features [like code scanning](https://docs.github.com/en/code-security/getting-started/github-security-features#available-with-github-advanced-security). See [here](https://docs.github.com/en/enterprise-cloud@latest/get-started/learning-about-github/about-github-advanced-security) for more details.
- [Snyk](https://snyk.io/) - $
- [Sonatype](https://www.sonatype.com/) - $

::: good
![Figure: Good Example - Dependabot produces a vulnerability report periodically (and can raise a PR for you)](screen-shot-2022-05-20-at-12.48.33.png)
:::

::: good
![Figure: Good Example - Snyk produces a vulnerability detection alert email](screen-shot-2022-05-20-at-12.38.26.png)
:::
