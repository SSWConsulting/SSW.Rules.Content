---
type: rule
title: Do you keep a package audit log?
uri: package-audit-log
authors:
  - title: Piers Sinclar
    url: https://www.ssw.com.au/people/piers-sinclair
related:
  - awesome-documentation
  - installing-3rd-party-libraries
  - technical-debt
created: 2022-10-27T05:23:16.827Z
guid: 0a63d71e-66f0-4583-8a9c-6252df92ea34
---
Packages are the lifeblood of any software project. However, if the team is not careful, that lifeblood can turn into a heavy weight dragging the application down. It's too easy for 10 packages to turn into 1,000.

That's why it's crucial to maintain a package audit log.

<!--endintro-->

![](3rd-party-check-logos.png)

A package audit log helps developers track why packages are added, who added, and who approved them.

Generally, keep track of packages in a different file for each project in the solution e.g. \FrontendPackageAuditLog.md or \BackendPackageAuditLog.md

### What to track?

There are lots of things that can be tracked in a package audit log. Generally, you want to keep it as simple as possible and containing only information that isn't easy to find elsewhere. For example, bundle size and load time can easily be found on [Bundlephobia](bundlephobia.com), so there is no need to track that.

The 6 best attributes to keep track of are:

* Name
* Link to npm/NuGet
* Action (aka "added" or "removed")
* Actioned by
* Approved by
* Why (aka the reason)

That way it is easy to find out where the package is, who was involved in adding or removing it and why the change was made.

### Technical Debt - Ensure it gets updated

It's imperative that the package audit log is updated every time a package is added or removed. So, add it to the Sprint Review as an item to action every week. That way, the team is aware of all changes, and any missed changes are caught.

This process could be taken even further by having automated checks in PRs to add package details and then generating release notes based on those PRs.

### Template - What does it look like?

Markdown is an awesome way to structure and store the package audit log. Create a list following the below template:

```
# Project Northwind Frontend (REACT)

These are all the packages that have been added to the project (ordered by most recent). 
Note: Statistics like load time and bundle size can easily be found at [Bundlephobia](bundlephobia.com)

## [font-awesome](https://www.npmjs.com/package/font-awesome)
* Action: ✅Added
* Actioned by: William Liebenberg
* Approved by: No one available 😥
* Why: Get pre-made icons in our app!

## [date-fns](https://www.npmjs.com/package/date-fns)
* Action: ✅Added
* Actioned by: Piers Sinclair
* Approved by: Adam Cogan
* Why: It's faster than moment

## [moment](https://www.npmjs.com/package/moment)
* Action: ❌Removed
* Actioned by: Piers Sinclair
* Approved by: William Liebenberg
* Why: It's slower than date-fns

## [bootstrap](https://www.npmjs.com/package/bootstrap)
* Action: ✅Added
* Actioned by: Brady Stroud
* Approved by: Piers Sinclair
* Why: For pretty styling on the application
```
