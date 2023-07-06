---
type: rule
title: Do you know the 3 steps to completing a PBI?
uri: do-you-know-the-3-steps-to-a-pbi
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
  - title: Piers Sinclair
    url: https://ssw.com.au/people/piers-sinclair
related: []
redirects:
  - do-you-know-the-3-steps-to-completing-a-pbi
created: 2013-08-30T06:33:21.000Z
archivedreason: null
guid: 1de9df77-9b69-4242-b648-e08e5980e9a6
---
The lifecycle of a PBI can be broken down into 3 steps:

<!--endintro-->

### 0. Before it's ready

1. Received an email with some work to do? Get it into the backlog as a PBI ASAP (as per [Do you turn an email into a work item before starting work?](/turn-emails-into-pbis)).
2. Is the PBI ready? Check your PBI against your [Definition of Ready](/have-a-definition-of-ready).

### 1. Ready

1. Take the next PBI that was approved by the [Product Owner](/rules-to-better-product-owners)
2. Break down your PBI into tasks

::: good
![Figure: Testing Task added to PBI. This is the board the team will use for 90% of the Sprint, so testing is visible to everyone here](Testing-task.png)
:::

### 2. Code

1. From the PBI, create a new branch (so that your work is automatically tagged to the PBI)
2. On the Kanban Board, move your Task into "In Progress"
3. Checkout your new branch and code, code, code… (remember to [Red, Green, Refactor](/reply-done-plus-added-a-unit-test))
4. Open a Pull Request and get another engineer in your team to do an "over the shoulder" check of the code
5. Record a Done Video so you get your ducks in a row for the explanation to the Product Owner, and so they give you earlier feedback.
6. Make changes based on feedback (and then get more feedback)
7. Are you "Done"? Check your [Definition of Done](/definition-of-done) and complete the Pull Request!

### 3. Done

This should be easiest part!

1. Close off the PBI by replying done inside the PBI and also in the email thread

Congrats, your PBI is now ready to be demonstrated during your Sprint Review!

**Note:** This is the same process you'd follow for a Bug.

::: good
![Figure: This image includes all the important steps in a PBI lifecycle. Print this "SSW 3 Steps to a PBI pdf" and put it on your 'War Room' wall](3StepsToAPBI.jpg)
:::
