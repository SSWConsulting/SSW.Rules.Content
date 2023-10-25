---
type: rule
archivedreason: 
title: Done - Do you know how to make sure you deliver a build that’s tested every Sprint
guid: 8dc1ec73-f241-429f-8282-227a8fb39048
uri: done-do-you-know-how-to-make-sure-you-deliver-a-build-thats-tested-every-sprint
created: 2010-08-09T13:07:10.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
- title: Martin Hinshelwood
  url: https://ssw.com.au/people/martin-hinshelwood
related: []
redirects:
- done-do-you-know-how-to-make-sure-you-deliver-a-build-that’s-tested-every-sprint

---

What happens when you leave all the testing to the end of the Sprint? You find things that are not  ***done*** and you have no time before the  **Sprint Review** to fix them.

<!--endintro-->

![](RuleBuildEverySprintBad.png) 

::: bad
 **Figure: Bad example - if you don’t complete all the tasks the customer will not receive a build in the Sprint** 
:::
One way to mitigate this is to aim for a “ ***test please*** ” to occur a few days before the end of the  **Sprint** but you still run the risk of not having enough time to make sure everything is  ***done.*** 

![](RuleBuildEverySprintOK.png)


::: good
 **Figure: OK example – Send the “test please” before the end of the Sprint so you have time to finish everything** 
:::

It is preferable to conduct a  **Smoke Test** to make sure that you are comfortable demoing the unit of work you just finished to the customer. One way to do this is to create a Coded UI test for each of the Stories as part of your Definition of Done (DoD) that runs through the functionality you have built.

In this scenario the “ **test please** ” with the customer happens outside of the current Sprint. 

![](RuleBuildEverySprintGOOD.png)


::: good
 **Figure: Good example – Create a coded UI test for each story to prove that it is complete** 
:::

If you are doing  **Scrum** then you should have a  **User Story** fleshed out with a set of  **Acceptance Criteria** . These  **Acceptance Criteria** are agreed with the  **Product Owner** before  **The Team** committed to the story, and define what the  **Product Owner** will accept as complete. This makes it relatively easy to create some automated tests that test for these  **Acceptance Criteria** and help your  **Sprint Review** go as smoothly as possible.

Any changes found during  **the Sprint Review** get added to the  **Product Backlog** to be prioritised by the  **Product Owner** . 

![](RuleBuildEverySprintUltimate.png)
**Figure: Ultimate example – Create a Test (could be Coded UI) for each of the Acceptance Criteria agreed with the Product Owner**
