---
type: rule
archivedreason: 
title: Do you know The Golden Rule of Rebasing?
guid: 9302157e-0ca6-48d3-9f59-46af0c035b9c
uri: do-you-know-the-golden-rule-of-rebasing
created: 2016-02-15T20:11:38.0000000Z
authors:
- id: 24
  title: Adam Stephensen
related: []

---

Rebasing is great for ensuring a clean project history... but it can be dangerous in inexperienced hands.

<!--endintro-->

**The golden rule of git rebase is to never use it on public branches.** (ie. never rebase master).

You should never rebase master onto a feature branch. This would move all of the commits in master onto the tip of  the feature branch (not the other way around).

Since rebasing results in brand new commits, Git will think that your master branch’s history has diverged from everybody else’s. If you were to Push this to the server... [expect lots of pain to fix it up](https://www.atlassian.com/git/tutorials/merging-vs-rebasing/the-golden-rule-of-rebasing)!
<dl class="badImage">&lt;dt&gt; <img src="rebase3.png" alt="rebase3.png"> &lt;/dt&gt;<dd>Figure: Bad Example: Rebasing master onto a feature branch can cause project history to become confused.    </dd></dl><dl class="image">&lt;dt&gt; <img src="rebase4.png" alt="rebase4.png"> &lt;/dt&gt;<dd>Figure: To get it wrong in Visual Studio you would need to change the current branch to master and then choose rebase. While this is possible, the VS team have done a good job making it hard to do the wrong thing</dd></dl><dl class="goodImage">&lt;dt&gt; <img src="rebase5.png" alt="rebase5.png"> &lt;/dt&gt;<dd>Figure: Good Example - Rebase your Feature branch onto Master</dd></dl>
