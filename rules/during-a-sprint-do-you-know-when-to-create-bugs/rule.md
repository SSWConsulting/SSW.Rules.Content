---
type: rule
archivedreason: 
title: During a sprint - Do you know when to create bugs?
guid: 1685edfa-c7a7-41fe-965e-038a2d663f34
uri: during-a-sprint-do-you-know-when-to-create-bugs
created: 2010-09-16T16:13:21.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Martin Hinshelwood
  url: https://ssw.com.au/people/martin-hinshelwood
related: []
redirects: []

---

This is a very common question asked of teams using Scrum. The answer can depend on a lot of things, such as:

* How big is the bug?
* Can it be fixed right now?
* How important is quality to the product?
* Are there dedicated testers as part of the team?


Regardless of your answers, there are basically two types of bugs: those found in code currently being developed (in-Sprint) and those found in code previously thought done (out-of-Sprint).

<!--endintro-->

### In-Sprint bugs

For stories that are currently in progress, here are some guidelines:

Typically you want to fix all bugs discovered during the sprint or else they could impact the team’s ability to achieve its Sprint goal:

* If it’s a small bug (&lt; 1 hour to fix) and won’t impact the burndown, then just fix it
* If it’s a larger bug (&gt; 1 hour to fix) and won’t impact the ability to achieve the Sprint goal, then create a Bug work item, associate a Task and have a team member perform the fix during the Sprint
* If it’s a larger bug (&gt; 1 hour to fix) and will impact the ability to achieve the Sprint goal, then create a Bug work item to be prioritized (by the Product Owner) and to be fixed in a later Sprint; you may not be able to achieve your Sprint goal
* If another team member finds the bug, then they should create a Bug work item and then the team decides if it can be fixed in the current Sprint or needs to be prioritized (by the Product Owner) to be fixed in a later Sprint, in which case you may not be able to achieve your Sprint goal The team decides how many hours “n” equals


### Out-of-Sprint bugs

For stories that the team had previously considered done, here are some guidelines:

* If the bug is not critical (i.e. a hotfix), then create a Bug work item to be prioritized and fixed in a later Sprint
* For a critical hotfix, do whatever needs to be done to get the fix into production, knowing that your current Sprint commitments may be impacted Adjust the team’s capacity accordingly, especially if lots of hotfixes start occurring.
General tip: don’t create an associated task to fix a bug until the Sprint in which the team commits to fix it


See rule on [Do you know how to handle Bugs on the Product Backlog?](/Pages/BugsontheProductBacklog.aspx) for how to work with bugs on your backlog.

Extracted from        [Accentient’s](http&#58;//www.accentient.com/scrum/) Scrum Training by        [Richard Hundhausen](https&#58;//twitter.com/rhundhausen).
