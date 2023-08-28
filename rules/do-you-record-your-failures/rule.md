---
type: rule
archivedreason: 
title: Do you record your failures?
guid: 1de870f1-0278-4c11-8a25-8ec13bf8bdad
uri: do-you-record-your-failures
created: 2019-03-13T04:50:25.0000000Z
authors:
- title: Adam Cogan
  url: /people/adam-cogan
- title: Andreas Lengkeek
  url: /people/andreas-lengkeek
- title: Barry Sanders
  url: /people/barry-sanders
- title: Jernej Kavka
  url: /people/jernej-kavka
- title: Patricia Barros
  url: /people/patricia-barros
related: []
redirects: []

---

Australian R&D laws require you to show the separate attempts you make when developing a feature that counts towards R&D. For this reason, you should make sure to commit in between every attempt you make even if it does not have the desired affect to record the history of experimentation.





<!--endintro-->

The below example is for a scenario to improve load times for an MVC to Angular web app. The developer creates a new feature branch and works on their local machine.





Once they are done the developer commits all the changes they made and push it the remote repository. Using this method, the developer loses the history of experimentation and it will be difficult to prove for R&D.


![](single-commit-not-showing-experimentation-2.png)



::: bad
Bad Example: Only the final solution is committed. Experimentation history is not recorded  
:::




In this example for the same scenario the developer makes sure to commit every separate attempt to reduce load times for their web application. This way, everybody knows what kinds of experimentation was done to solve this problem.

![](commit-failed-experiments.png)




::: good
Good Example: Each attempt has a new commit and is not lost when retrieving history

:::
