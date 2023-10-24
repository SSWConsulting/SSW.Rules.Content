---
type: rule
title: GitHub Repos - Do you write nice commit messages?
uri: use-emojis-in-your-commits
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related:
  - use-emojis
  - which-emojis-to-use-in-scrum
  - write-a-good-pull-request
redirects:
  - do-you-write-nice-commit-messages
created: 2020-09-17T02:54:43.000Z
archivedreason: null
guid: d32126a2-4d6d-4f06-a7ba-f80234e66079
---

Reading ugly commits is not very pleasant and makes it very confusing when you have to check the commit history.

::: bad  
![Bad Example: The commits have no meaning.](2020-09-17\_17-19-04.png)  
:::

<!--endintro-->

`youtube: https://www.youtube.com/embed/uBLWVxnPLP4`

Here are a few ways to improve your commit log.

### Tip #1: Have a nice, concise comment

Examples:

* Fixed bug with emoji engine
* Added new emoji filter
* Updated Architecture Diagram to have emojis

### Tip #2: Using prefixes

Even better is to add a helpful prefix to categorize your commits.

Examples:

* Fix: Fixed bug with emoji engine
* Feature: Added new emoji filter
* Doc: Updated Architecture Diagram to have emojis

### Tip #3: Using emojis 💄

In a text message, emojis helps to add emotion and context to plain text. Why not use them in commit messages too 😃?

Examples:

* 🐛 BUG - Fixed emoji engine in language component
* 🚀 Feature - Added emoji filter on Snapchat
* 📄 Doc - Added emoji’s to changelog

There are a bunch more options to choose from - [carloscuesta/gitmoji: An emoji guide for your commit messages. 😜 (github.com)](https://github.com/carloscuesta/gitmoji)

### Tip #4: Using gitmoji VSCode extension

[Gitmoji - Visual Studio Marketplace (visualstudio.com)](https://marketplace.visualstudio.com/items?itemName=seatonjiang.gitmoji-vscode).

You can even go 🤘 hardcore and use the  **gitmoji cli -** [carloscuesta/gitmoji-cli: A gitmoji interactive command line tool for using emojis on commits. 💻 (github.com)](https://github.com/carloscuesta/gitmoji-cli)


::: good  
![Good Example: Great use of emoji and concise message.](commits-with-emojis.jpg)  
:::

See what emojis work best with each topic here: [https://gitmoji.dev/](https://gitmoji.dev/)

![Figure: Emojis list.](emojis-list.jpg)
