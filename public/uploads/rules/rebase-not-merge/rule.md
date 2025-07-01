---
seoDescription: Learn to rebase not merge and eliminate messy commits for a cleaner project history.
type: rule
archivedreason:
title: Do you know to Rebase not Merge?
guid: ed100451-91c0-4c38-8db8-b12d6b57b780
uri: rebase-not-merge
created: 2016-02-15T19:58:36.0000000Z
authors:
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
related: []
redirects:
  - do-you-know-to-rebase-not-merge
---

When you merge a branch you end up with messy merge commits.

Rebasing might take a bit to get your head around, but you get a much cleaner project history.

<!--endintro-->

- it eliminates the unnecessary merge commits required by git merge
- rebasing also results in a perfectly linear project history - you can follow the tip of feature all the way to the beginning of the project without any forks.

This makes it easier to navigate your project with commands like git log, git bisect, and gitk.

![Figure: When merging: a messy merge commit is created any time you need to incorporate upstream changes from the master branch](rebase1.png)

![Figure: Git Rebase moves your new commits to the end of the master branch. This ensure that you don't end up with messy merge commits and you have a clean linear project history](rebase2.png)

**Warning:** If you don’t follow [the Golden Rule of Rebasing](/the-golden-rule-of-rebasing), you could end up in a world of pain.
