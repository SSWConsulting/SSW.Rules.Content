---
type: rule
archivedreason: 
title: Do you save failed experiments in abandoned pull requests?
guid: 749a0b35-2357-454e-b6d3-6e0b5a4804ba
uri: do-you-save-failed-experiments-in-abandoned-pull-requests
created: 2019-03-13T04:58:30.0000000Z
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


<div>​​​​Assume you are creating a cool new feature. First you will create a new branch, create some commits, check it works, and submit a pull request. However, if you are not happy with the feature then don’t just delete the branch as normal. Instead, create a pull request anyway and set the status to Abandoned. Now, you can continue to delete your branch as normal.<br></div><div><br></div><div>This makes sure that we have a historical log of work​ completed, and still keeps a clean repository.<br><div><br></div></div>
<br><excerpt class='endintro'></excerpt><br>
​<img src="create-pr-for-failed-branch.png" alt="create-pr-for-failed-branch.png" style="margin:5px;width:508px;" /><div><dd class="ssw15-rteElement-FigureGood">Good Example: Setup pull request for feature branch so that we have a history of the commits<br></dd><div><br></div></div><div><img src="abandoned-pr-for-branch.png" alt="abandoned-pr-for-branch.png" style="margin:0px 5px;width:508px;height:146px;" /><br></div><dd class="ssw15-rteElement-FigureGood">​Good Example: PR is abandoned with a deleted branch​<br></dd>


