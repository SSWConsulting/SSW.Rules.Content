---
type: rule
title: Do you know The Golden Rule of Rebasing?
uri: do-you-know-the-golden-rule-of-rebasing
created: 2016-02-15T20:11:38.0000000Z
authors:
- id: 24
  title: Adam Stephensen

---



<span class='intro'> <p>Rebasing is great for ensuring a clean project history... but it can be dangerous in inexperienced hands.</p> </span>

<p> 
   <strong>The golden rule of&#160;git rebase&#160;is to never use it on&#160;public&#160;branches.&#160;</strong>(ie. never rebase&#160;master).</p><p>You should never rebase master onto a feature branch. This would&#160;move&#160;all of the commits in&#160;master&#160;onto the tip&#160;of&#160; the feature branch (not the other way around).&#160;</p><p>The problem is that this only happened in&#160;your&#160;repository. All of the other developers are still working with the or iginal&#160;master. Since rebasing results in brand new commits, Git will think that your&#160;master&#160;branch’s history has diverged from everybody else’s.</p><dl class="badImage"><dt> <img src="/PublishingImages/rebase3.png" alt="rebase3.png" /> </dt><dd>Figure&#58; Bad Example&#58; Rebasing master onto a feature branch can cause project history to become confused. <a href="https&#58;//www.atlassian.com/git/tutorials/merging-vs-rebasing/the-golden-rule-of-rebasing">See this link to learn how to fix it up </a></dd></dl><dl class="image"><dt> ​<img src="/PublishingImages/rebase4.png" alt="rebase4.png" /> </dt><dd>Figure&#58; To get it wrong in Visual Studio you would need to change the current branch to master and then choose rebase. While this is possible, the VS team have done a good job making it hard to do the wrong thing</dd></dl><dl class="goodImage"><dt> <img src="/PublishingImages/rebase5.png" alt="rebase5.png" /> </dt><dd>Figure&#58; Good Example - Rebase your Feature branch onto Master</dd></dl>


