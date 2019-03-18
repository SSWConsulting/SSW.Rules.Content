---
type: rule
title: Do you save failed experiments in abandoned pull requests?
uri: do-you-save-failed-experiments-in-abandoned-pull-requests
created: 2019-03-13T04:58:30.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 87
  title: Andreas Lengkeek
- id: 82
  title: Barry Sanders
- id: 58
  title: Jernej Kavka
- id: 84
  title: Patricia Barros

---



<span class='intro'> <div>​​​Assume you are creating a cool new feature. First you will create a new branch, create some commits, check it works, and submit a pull request. However, if you are not happy with the feature then don’t just delete the branch as normal. Instead, create a pull request anyway and set the status to Abandoned. Now, you can&#160;continue to delete your branch as normal.<br></div><div><br></div><div>This makes sure that we have a historical log of word completed, and still keeps a clean repository.<br><div><br></div></div> </span>

​<img src="/SiteAssets/do-you-save-failed-experiments-in-abandoned-pull-requests/create-pr-for-failed-branch.png" alt="create-pr-for-failed-branch.png" style="margin&#58;5px;width&#58;508px;" /><div><dd class="ssw15-rteElement-FigureGood">Good Example&#58;&#160;Setup pull request for feature branch so that we have a history of the commits<br></dd><div><br></div></div><div><img src="/SiteAssets/do-you-save-failed-experiments-in-abandoned-pull-requests/abandoned-pr-for-branch.png" alt="abandoned-pr-for-branch.png" style="margin&#58;0px 5px;width&#58;508px;height&#58;146px;" /><br></div><dd class="ssw15-rteElement-FigureGood">​Good Example&#58;&#160;PR is abandoned with a deleted branch​<br></dd>


