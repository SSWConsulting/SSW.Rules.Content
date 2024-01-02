---
type: rule
title: Do you know when to branch in TFS (aka TFVC)?
uri: do-you-know-when-to-branch
authors:
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
related: []
redirects:
  - do-you-know-when-to-branch-in-tfs-aka-tfvc
  - do-you-know-when-to-branch-in-tfs-(aka-tfvc)
created: 2013-12-06T17:54:34.000Z
archivedreason: See the rule for how to branch in Git as a more modern tool
  choice than TFS [https://www.ssw.com.au/rules/do-you-know-when-to-branch-in-git](/rules/do-you-know-when-to-branch-in-git)
guid: aeeec9fa-6d78-4682-838d-091a3347ca28
---

One of the most controversial issues developers discuss is when to create branches and how many you should have.

Keep things simple:

1. Have the team develop on the one branch. It is fantastic as there is no more merging hell.
2. Have that branch called "**main**" (or " **trunk** " when using **TFS** or **SVN**

<!--endintro-->

::: greybox
**Note:** This rule only applies to TFVC. For git, see [Do you know when to branch in git?](/do-you-know-when-to-branch-in-git)
:::

Beware of smart bloggers giving the wrong advice 🙃 as many smart people like creating branches... E.g. [Guidance: A Branching strategy for Scrum Teams](https://nkdagility.com/blog/guidance-a-branching-strategy-for-scrum-teams/). Even Martin Fowler says there are a number of issues related to merging that lead us to try and minimise the number of branches that we work with in his article on [Feature Branches](https://martinfowler.com/bliki/FeatureBranch.html).

The quintessential scenario you need to support is that emergency _"Hey we have a security hole on the site and Hanselman has just tweeted it!"_

In that case you need to potentially update all of your branches and perform deployment, which can be quite tiresome.

The better way is to use OctopusDeploy which relieves developers from having multiple branches because you only have to worry about building on one branch and deployment can be done automatically to multiple environments. Octopus provides more secure, feature-rich environment which makes it very easy to deploy and promote builds between environments.

::: good  
![Figure: Good example - Manage deployments to multiple environments, view deployed versions.](2014-10-11\_18-54-00.png)  
:::

### Why you should avoid branching

1. Merging is painful, complex and is a time consuming task that does not add value
2. Often regressions are introduced as merges are missed and not merged back to trunk
3. The longer branches are, the more people that have worked on them... the more unpleasant the merge is going to be
  Amount of pain = size of the change \* the amount of work on the trunk in that period
4. The more you need to create a branch, the harder it is going to be to merge it back into the trunk!
5. Branching impedes refactoring

If a am working on a branch and perform sweeping renaming, and a developer working on another branch does the same – merging is nearly impossible.

This is **very** likely to happen on code bases that require tidying when you have developers who believe in improving code as they go (see the [Boy Scout rule](/follow-boy-scout-rule))

### When it's OK to branch

* For a disposable, investigatory spike
* To perform hotfixes to production environment

::: bad  
![Figure: Bad example – Creating a branch per feature leads to lots of merging (Image from paulhammant.com blog)](branch-bad.jpg)  
:::

::: bad  
![Figure: Bad example – Creating a branch per Sprint has everyone working on the same code but requires at least one merge every Sprint](branch-bad-2.jpg)
:::

::: good  
![Figure: Good example - Release Branching - always develop on the trunk, but create a new branch each time you release. This means that all developers are continually integrating all their code, branching is rare, but you always have access to your released version in case bug fixes or small mods are required. (Image from paulhammant.com)](branch-good.jpg)  
:::

#### Further reading

* [Make Large Scale Changes Incrementally with Branch By Abstraction](https://continuousdelivery.com/2011/05/make-large-scale-changes-incrementally-with-branch-by-abstraction/)
* [Introducing Branch By Abstraction](https://paulhammant.com/blog/branch_by_abstraction.html)
* [FeatureBranch by Martin Fowler](https://martinfowler.com/bliki/FeatureBranch.html)  
* [SemanticConflict by Martin Fowler](https://martinfowler.com/bliki/SemanticConflict.html)
