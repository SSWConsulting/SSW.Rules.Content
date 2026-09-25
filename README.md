<img alt="SSW banner" src="https://raw.githubusercontent.com/SSWConsulting/SSW.Rules.Content/main/_docs/images/ssw-banner.png">

# The SSW Rules content 📜

Welcome to SSW.Rules.Content (The Data in markdown). Thank you for contributing best practices into SSW Rules!

<img alt="YouTube icon" align="left" width="32" height="22" src="https://raw.githubusercontent.com/SSWConsulting/SSW.Rules.Content/main/_docs/images/youtube_social_icon_red.png">

[SSW.Rules YouTube Channel](https://www.youtube.com/channel/UCKqEo5bl8ODqYZCKsq2xK5w)

## Pull Requests, Builds and Releases

Builds are done in GitHub Actions. After a rule is edited, a Pull Request is needed to be merged into the `main` branch and deployed to Production.  

PRs can be approved by [anyone at SSW](https://www.ssw.com.au/people/). Try these people first:

1. Tiago Araujo
2. Brady Stroud
3. Adam Cogan
4. Luke Cook
5. Brook Jeynes

[See the outstanding Pull Requests](https://github.com/SSWConsulting/SSW.Rules.Content/pulls).  
Most edits show on the site soon after merge. New redirects (from renaming a rule) only start working after the next [production deploy](https://github.com/SSWConsulting/SSW.Rules/actions/workflows/scheduled-production-deploy.yml), which runs daily at 06:00 UTC.

📘 How-to guides and GitHub Actions documentation are in the [Wiki](https://github.com/SSWConsulting/SSW.Rules.Content/wiki). To change a rule's URL or move it to a new folder, follow [How to Rename Rules](https://github.com/SSWConsulting/SSW.Rules.Content/wiki/How-to-Rename-Rules).

## Structure

* Rules live in `public/uploads/rules/[uri]/rule.mdx`
* Categories live in the categories folder
* Each rule has a folder containing rule.mdx and its images/assets
* Rules are organised into categories
* A rule can belong to multiple categories
* Category pages link to rules via frontmatter data

## The SSW Rules engine 🚗

This is built into a static site by the code at [SSW Rules](https://github.com/SSWConsulting/SSW.Rules).

## Agentic Workflows (ContentHawk 🦅)

This repository uses GitHub Agentic Workflows to assist in the ongoing maintenance of content. Using campaigns. For more information about these campaigns, and how to create them, refer to the [ContentHawk Documentation](.github/ContentHawk/README.md).
