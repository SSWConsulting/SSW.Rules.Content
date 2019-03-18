---
type: rule
title: Do you record your failures?
uri: do-you-record-your-failures
created: 2019-03-13T04:50:25.0000000Z
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



<span class='intro'> <div>Australian R&amp;D laws require you to show the seperate attempts you make when developing a feature that counts towards R&amp;D. For this reason, you should make sure to commit in between every attempt you make even if it does not have the desired affect to record the history of experimentation.<br></div><div><br></div> </span>

<div>The below example is for a scenario to improve load times for an MVC to Angular web app. The developer creates a new feature branch and works on their local machine.<br></div><div><br></div><div>Once they are done the developer commits all the changes they made and push it the remote repository. Using this method,&#160;the developer loses the history of experimentation and it will be difficult to prove for R&amp;D.<br></div><div><img src="/SiteAssets/do-you-record-you-failures/single-commit-not-showing-experimentation-2.png" alt="single-commit-not-showing-experimentation-2.png" style="margin&#58;5px;width&#58;508px;" /><br></div><dd class="ssw15-rteElement-FigureBad">​​Bad Example&#58; Only the final solution is commited. Experimentation history is not recorded​</dd><div><br></div><div>In this example for the same scenario the developer makes sure to commit every seperate&#160;attempt to reduce load times for their web application. This way, everybody knows what kinds of experimentation was done to solve this problem.<br><div><img src="/SiteAssets/do-you-record-you-failures/commit-failed-experiments.png" alt="commit-failed-experiments.png" style="margin&#58;5px;width&#58;508px;" />​<br></div><div><dd class="ssw15-rteElement-FigureGood">Good Example&#58; Each attempt has a new commit and is not lost when retrieving history​​<br></dd></div></div>


