---
seoDescription: Avoid large PRs by choosing between creating a new repository or folder, and merging using small pull requests, allowing for clean snapshots of legacy applications and isolated backlogs.
type: rule
title: Git - Do you know how to avoid large PRs?
uri: avoid-large-prs
authors:
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
  - title: Jack Pettit
    url: https://www.ssw.com.au/people/jack-pettit
created: 2023-02-22T22:41:50.529Z
guid: d85ead8c-9a6b-4715-b798-e3db535604f8
---

Nobody wants to review a PR with 100s of files, nor is it nice to have a lot of work that is committed (a PR may even be waiting), but not approved. This is merge debt. Part of getting work complete is getting the PR approved by another developer so you don’t have it sitting around for a long time.

<!--endintro-->

The default option is to use a feature branch strategy which is awesome for small chunks of work. However, if you know that your work involves 2+ devs working on different tasks and they cannot work in isolation, then it can be tricky. For example, if you need to migrate from Gatsby to Next.js or if you have to upgrade from Xamarin to .NET MAUI then a feature branch strategy might not be appropriate. In that case choose from the below options:

### Option 1 - Create a new repository

This is a good option if you are concerned with legacy technical decisions impacting the future application.

### ✅ Pros

* Clean snapshot of legacy application
* No risk of the legacy application being used or referenced
* Isolated backlog – keep issues about the new project separated

### ❌ Cons

* Loss of history in one mono repo
* Isolated backlog – cannot see old feature or bug requests
* Have to migrate important issues later

![Figure: Good example – Developing the new application in a new repo ](avoid-large-prs-website.png)

### Option 2 – Create a new folder and keep merging using small PRs

In this scenario you will be replacing the old project (folder) at the end for a final rubber stamp PR

This is a good option if you are not worried about the legacy application influencing the new application.

### ✅ Pros

* Keeps history of previous iteration in one repo
* Sharing the same backlog – can see both old and new PBIs
* Can clearly see the difference after the final PR

### ❌ Cons

* Potential to reference or use old code/models
* Must implement bug fixes for the new + the old project
* Easier to be influenced by past legacy decisions
* Sharing the same backlog – can see both old and new PBIs

![Figure: Good example – Developing your new application in a new folder](avoid-large-prs-portal.png)
