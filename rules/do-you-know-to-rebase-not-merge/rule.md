---
type: rule
title: Do you know to Rebase not Merge?
uri: do-you-know-to-rebase-not-merge
created: 2016-02-15T19:58:36.0000000Z
authors:
- id: 24
  title: Adam Stephensen

---



<span class='intro'> <p class="ssw15-rteElement-P">When you merge a branch you end up with messy merge commits.</p><p class="ssw15-rteElement-P">Rebasing might take a bit to get your head around, but&#160;you get a much cleaner project history.<span style="line-height&#58;1.6;">​</span></p> </span>

<ul><li>it eliminates the unnecessary merge commits required by&#160;git merge<br></li><li>rebasing also results in a perfectly linear project history -&#160;you can follow the tip of&#160;feature&#160;all the way to the beginning of the project without any forks.</li></ul><p>This makes it easier to navigate your project with commands like&#160;git log,&#160;git bisect, and&#160;gitk.</p><dl class="image"><dt><img src="/PublishingImages/rebase1.png" alt="rebase1.png" /></dt><dd>Figure&#58; When merging&#58;&#160;a&#160;messy merge commit is created any time you need to incorporate upstream changes&#160;from the master branch</dd></dl> <dl class="image"><dt><img src="/PublishingImages/rebase2.png" alt="rebase2.png" /></dt><dd>Figure&#58; Git Rebase moves your new commits to the end of the master branch. This ensure that you don't end up with messy merge commits and you have a clean linear project history</dd></dl><p>
   <strong>Warning&#58;</strong>&#160;If you don’t follow <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=cb4fd562-6c0a-418c-88c5-9af1b9451469">the&#160;Golden Rule of Rebasing</a>,&#160;you could end up in a ​world of pain.</p>​


