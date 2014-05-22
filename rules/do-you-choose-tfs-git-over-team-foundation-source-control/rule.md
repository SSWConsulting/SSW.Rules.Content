---
type: rule
archivedreason: 
title: Do You Choose TFS-Git Over Team Foundation Source Control?
guid: 9a1642c8-3164-49b4-bd21-d81a014df14f
uri: do-you-choose-tfs-git-over-team-foundation-source-control
created: 2014-05-22T19:47:49.0000000Z
authors:
- id: 24
  title: Adam Stephensen
related: []

---


<p class="p1">Only a madman would write software today without using source control.</p><p class="p1">Apart from being the easiest way to back-up your code, and having the ability to go back to a previous state, source control provides a huge number of benefits, especially when integrated with Continuous Integration servers, and Continuous Deployment solutions.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>But which source control solution should I choose?​​</p><dl class="badImage"><dt>
      <img src="/TFS/RulesToBetterVersionControlWithGit/PublishingImages/git-1.jpg" alt="" /> 
   </dt><dd>Figure&#58; Bad Example - Unless you have time-travelled back to 1999, you should not be using Visual Source Safe</dd></dl><dl class="badImage"><dt>
      <img src="/TFS/RulesToBetterVersionControlWithGit/PublishingImages/git2.jpg" alt="" /> 
   </dt><dd>Figure&#58; Bad Example – Git is great, but learning to use ‘pure’ git from the command line can be intimidating for developers not used to working in a console</dd></dl><dl class="badImage"><dt>
      <img src="/TFS/RulesToBetterVersionControlWithGit/PublishingImages/git3.jpg" alt="" /> 
   </dt><dd>Figure&#58; Bad Example - Team Foundation Source Control – Server Workspaces. This is the source control that we have been using in TFS for years. It’s great, even on large code bases, except for when you are not connected to the TFS server. (Image from 
      <a href="http&#58;//bit.ly/why-tfs-git">http&#58;//bit.ly/why-tfs-git​</a>)</dd></dl><dl class="badImage"><dt>
      <img src="/TFS/RulesToBetterVersionControlWithGit/PublishingImages/git4.jpg" alt="" /> 
   </dt><dd>Figure&#58; Bad Example – Team Foundation Source Control – Local Workspaces. It’s great for when you are not connected to the TFS Server, except for when your code-base is very large. (Image from 
      <a href="http&#58;//bit.ly/why-tfs-git">http&#58;//bit.ly/why-tfs-git</a>)</dd></dl><dl class="goodImage"><dt>
      <img src="/TFS/RulesToBetterVersionControlWithGit/PublishingImages/git5.jpg" alt="" /> 
   </dt><dd>Good Example – TFS Git works fantastically offline and with large code-bases. Visual Studio has support for the basic operations so developers can ease their way into working with git. Once users become familiar with it, it also allows for far more control and flexibility. Note&#58; My Work and Code Review are not currently compatible with TFS Git, and you will need to fall back to the Git command line for more complex source control commands</dd></dl> 
<strong>Resources&#58;</strong> 
<a href="http&#58;//bit.ly/why-tfs-git">Taking your version control to a next level with TFS and Git </a>by Alexander Vanwynsberghe. 


