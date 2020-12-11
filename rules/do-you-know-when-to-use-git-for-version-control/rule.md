---
type: rule
archivedreason: 
title: Do you know when to use Git for version control?
guid: f4f15feb-8c1e-4f5f-865a-f18009c8b9d5
uri: do-you-know-when-to-use-git-for-version-control
created: 2013-08-21T16:39:49.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 3
  title: Eric Phan
- id: 23
  title: Damian Brady
related: []

---

Team Foundation Server Update 2 and Team Foundation Server 2013 comes with built in support for Git as a version control system.

<!--endintro-->
<dl class="image">&lt;dt&gt;<img src="git-screen.jpg" alt="">&lt;/dt&gt;<dd>Figure: How you start using Git on TFS</dd></dl>
You should use Git if you:

* Are running an open source project
* Have lots of remote team members (as you get offline repo access with full history)
* Have an unstable/sporadic internet connection
* Develop in a non Microsoft environment (e.g. Linux, OSX)


There are also several disadvantages:

* No "My Work" view in Team Explorer
* No "Code Review" integration in Visual Studio
* No "Check in Policies"
* No SOX, FDA or CFD-11 compliance


At this point, SSW still recommends Team Foundation Version Control (TFVC) as the version control system of choice.
