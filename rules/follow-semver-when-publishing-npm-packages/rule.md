---
type: rule
title: Do you follow semver when publishing npm packages?
seoDescription: When publishing npm packages, following Semantic Versioning (semver) is important for communicate changes clearly and maintain compatibility for your users. Learn how to manage versions responsibly and build trust with your user.  
uri: follow-semver-when-publishing-npm-packages
authors:
  - title: Ben Neoh
    url: https://www.ssw.com.au/people/ben-neoh
related:
  - different-symbols-mean-for-npm-version
  - packages-up-to-date
  - semantic-versioning
created: 2024-12-5T08:33:21.000Z
guid: 03d090d3-d813-43d9-998e-209c895050b3
---

When publishing an npm package, following **Semantic Versioning (semver)** is essential. It communicates changes clearly to your users and ensures smooth updates for their projects.

<!--endintro-->

## Why use semver in NPM Publishing

Semantic Versioning (semver) helps your users understand the impact of updates and manage their own dependencies more effectively. By adhering to semver, you make it clear whether an update introduces breaking changes, new features, or just bug fixes:

* **💥 MAJOR (Breaking Changes):** Signals to users that there are incompatible changes.
* **🚀 MINOR (New Features):** Informs users about new features that won’t break existing functionality.
* **🐛 PATCH (Bug Fixes):** Indicates that bug fixes or small improvements have been made without changing behavior.

Learn more about [semantic versioning](/semantic-versioning).

## Common Mistakes to Avoid ⚠️

### ❌ Incorrect Versioning

Ensure you understand the type of changes you’re making. For example, **if you introduce breaking changes but incorrectly release it as a patch update** (e.g., from `1.0.0` to `1.0.1`), it can cause significant issues for users relying on version ranges like `^1.0.0` or `~1.0.0` in their `package.json`.  

These ranges automatically pull in updates for compatible versions. By incorrectly marking a breaking change as a patch, you risk breaking their projects without warning. Always increment the **MAJOR** version for breaking changes to ensure users can consciously decide when to adopt them.

To better understand what the `^`, `~`, and other symbols mean in npm versioning, check out [What do the different symbols mean for npm version?](https://www.ssw.com.au/rules/different-symbols-mean-for-npm-version).  

### ❌ Forgetting to Communicate Breaking Changes

For major updates, clearly communicate the breaking changes in your release notes or changelog. This helps users prepare for or adapt to the changes.

::: good
![Figure: Good example - Tell public about the major release update and breaking changes](https://github.com/user-attachments/assets/ccb38aa4-f0cf-4886-8f8f-1410d9516e8b)
:::

## Tools to Help You Follow semver

* **[📝 changesets](https://www.npmjs.com/package/changeset)**
  A tool designed to manage versioning, changelogs, and release workflows in a more structured way. It helps you track changes in your codebase with "changeset" files that describe the changes made and their version impact, ensuring consistent versioning and changelog generation.
  
* **[🤖 Semantic Release](https://semantic-release.gitbook.io/)**  
  An automated tool that helps you manage versioning and changelogs based on your commit messages. It ensures that versions are incremented correctly according to your changes.

* **[🔄 Standard Version](https://github.com/conventional-changelog/standard-version)**  
  A tool for automating versioning and changelog generation based on conventional commit messages. It follows the rules of semver and can help reduce manual errors in version management.

* **[📚 Keep a Changelog](https://keepachangelog.com/)**  
  A standard for writing clear and consistent changelogs. Keeping a changelog is essential for communicating breaking changes and other updates clearly with users.

* **[🔢 semver](https://www.npmjs.com/package/semver)**  
  A library that helps parse and compare version numbers. It’s useful for checking if a version change follows the semver rules.

* **[📖 Semantic Versioning Specification](https://github.com/semver/semver/blob/master/semver.md)**  
  The official guide for Semantic Versioning. It outlines the full specification and provides more detailed rules that you should follow when working with semver.

## Important Semver Rules to Follow ✅

Here are some key rules from the [Semantic Versioning Specification](https://github.com/semver/semver/blob/master/semver.md) that you should keep in mind:

1. **Version Numbers Must Be Non-Decreasing**  
   Version numbers must always increase. If you publish a lower version than the previous one, it will cause issues for users.

2. **Pre-release Versions and Build Metadata**  
   Semver allows for the use of pre-release versions (e.g., `1.0.0-alpha.1`) and build metadata (e.g., `1.0.0+20130313144700`). These should be used to indicate versions that are not ready for production or specific builds that don’t affect the versioning rules.

3. **Incrementing Versions**  
   * **Patch**: Only increment for bug fixes and minor changes that do not affect the API.  
   * **Minor**: Increment for new features that do not break backward compatibility.  
   * **Major**: Increment for breaking changes to the API or backward incompatibilities.

4. **API Stability**  
   Always ensure that your API is backward compatible unless you are marking it as a breaking change. It’s essential to be mindful of how updates impact users' current implementations.

5. **Changelogs and Documentation**  
   Always document changes thoroughly, particularly breaking changes, in your changelog and version history. This documentation provides context and helps users understand what to expect from each version.  
