---
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


<p class="ssw15-rteElement-P">When you merge a branch you end up with messy merge commits.</p><p class="ssw15-rteElement-P">Rebasing might take a bit to get your head around, but you get a much cleaner project history.<span style="line-height:1.6;">​</span></p>
<br><excerpt class='endintro'></excerpt><br>
<ul><li>it eliminates the unnecessary merge commits required by git merge<br></li><li>rebasing also results in a perfectly linear project history - you can follow the tip of feature all the way to the beginning of the project without any forks.</li></ul><p>This makes it easier to navigate your project with commands like git log, git bisect, and gitk.</p><dl class="image"><dt><img src="rebase1.png" alt="rebase1.png" /></dt><dd>Figure: When merging: a messy merge commit is created any time you need to incorporate upstream changes from the master branch</dd></dl> <dl class="image"><dt><img src="rebase2.png" alt="rebase2.png" /></dt><dd>Figure: Git Rebase moves your new commits to the end of the master branch. This ensure that you don't end up with messy merge commits and you have a clean linear project history</dd></dl><p>
   <strong>Warning:</strong> If you don’t follow <a href=/the-golden-rule-of-rebasing>the Golden Rule of Rebasing</a>, you could end up in a ​world of pain.</p>​


