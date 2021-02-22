---
type: rule
archivedreason: 
title: Do you link your commits to a PBI?
guid: 0e206ce8-deed-4b09-902d-ecec0499586b
uri: do-you-link-your-commits-to-a-pbi
created: 2019-03-13T01:00:33.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Andreas Lengkeek
  url: https://ssw.com.au/people/andreas-lengkeek
- title: Barry Sanders
  url: https://ssw.com.au/people/barry-sanders
- title: Jernej Kavka
  url: https://ssw.com.au/people/jernej-kavka
- title: Patricia Barros
  url: https://ssw.com.au/people/patricia-barros
related: []
redirects: []

---


<p>​​​​​​​​​​​​​​In order to get better clarity on what work is done, it's a good idea to connect your PBI's and tasks to the commits, branches and pull requests that relate to the item. All commits, branches and pull requests should be linked to a PBI.​​<br></p><dl class="badImage"><dt><img src="no-linked-commit.png" alt="no-linked-commit.png" /></dt><dd>​Bad Example: No linked commit's, branches or pull requests<br></dd>​​</dl><dl class="goodImage"><dt><img src="link-branch-to-pbi.png" alt="linked-commit" /></dt><dd>Good Example: Git branch linked to PBI in TFS<br></dd>
</dl>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-Tip">Note: If you create your branches through Azure DevOps then you can link them during creation.​​​​​</p><dl class="goodImage"><dt>​<img src="link-pbi-during-creation.png" alt="link-pbi-during-creation.png" /></dt><dd>​Good Example: Using Azure DevOps to link PBI during creation</dd></dl><p>Here is a handy resource for linking work items:</p><p><a href="https://devblogs.microsoft.com/devops/linking-work-items-to-git-branches-commits-and-pull-requests/">https://devblogs.microsoft.com/devops/linking-work-items-to-git-branches-commits-and-pull-requests/​​​</a>​​</p><p class="ssw15-rteElement-Tip">Note: You can setup Branch Policies on your main branches to enforce this behaviour.</p><dl class="goodImage"><dt>​<img src="add-branch-policy-for-linked-items.png" alt="add-branch-policy-for-linked-items.png" /></dt><dd>​Good Example: Branch Policy on the master branch to enforce linked work items on pull requests<br></dd>
</dl>


