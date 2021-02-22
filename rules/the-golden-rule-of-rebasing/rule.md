---
type: rule
archivedreason: 
title: Do you know The Golden Rule of Rebasing?
guid: 9302157e-0ca6-48d3-9f59-46af0c035b9c
uri: the-golden-rule-of-rebasing
created: 2016-02-15T20:11:38.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
related: []
redirects:
- do-you-know-the-golden-rule-of-rebasing

---


<p>​Rebasing is great for ensuring a clean project history... but it can be dangerous in inexperienced hands.</p>
<br><excerpt class='endintro'></excerpt><br>
<p> 
   <strong>The golden rule of git rebase is to never use it on public branches. </strong>(ie. never rebase master).</p><p>You should never rebase master onto a feature branch. This would move all of the commits in master onto the tip of  the feature branch (not the other way around). </p><p>Since rebasing results in brand new commits, Git will think that your master branch’s history has diverged from everybody else’s. If you were to Push this to the server... <a href="https://www.atlassian.com/git/tutorials/merging-vs-rebasing/the-golden-rule-of-rebasing">expect lots of pain to fix it up</a>!</p><dl class="badImage"><dt> <img src="rebase3.png" alt="rebase3.png" /> </dt><dd>Figure: Bad Example: Rebasing master onto a feature branch can cause project history to become confused.    </dd></dl><dl class="image"><dt> ​<img src="rebase4.png" alt="rebase4.png" /> </dt><dd>Figure: To get it wrong in Visual Studio you would need to change the current branch to master and then choose rebase. While this is possible, the VS team have done a good job making it hard to do the wrong thing</dd></dl><dl class="goodImage"><dt> <img src="rebase5.png" alt="rebase5.png" /> </dt><dd>Figure: Good Example - Rebase your Feature branch onto Master</dd></dl>


