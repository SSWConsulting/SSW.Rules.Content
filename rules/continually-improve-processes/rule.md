---
type: rule
archivedreason: 
title: 'DevOps – Stage 4: Do you continually improve processes?'
guid: ca702756-d411-4bf3-90ee-1faaf98f2f1f
uri: continually-improve-processes
created: 2016-03-07T18:51:30.0000000Z
authors:
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- devops-stage-4-do-you-continually-improve-processes
- devops-–-stage-4-do-you-continually-improve-processes

---

Now that you’ve got the numbers, you can then make decisions on what needs improvement and go through the DevOps cycle again.

Here are some examples:

<!--endintro-->

* For exceptions, review your exception log (ELMAH, RayGun, HockeyApp)
    * Add the important ones onto your backlog for prioritization
    * Add an ignore to the exceptions you don't care about to reduce the noise (e.g. 404 errors)
    * You can do this as the exceptions appear, or prior to doing your Sprint Review as part of the backlog grooming
    * You don't have to get the exception log down to 0, just action the important ones and aim to reduce the noise so that the log is still useful

* For code quality, add getting Code Auditor and ReSharper to 0 on files you’ve changed to your [Definition of Done](/done-do-you-go-beyond-done-and-follow-a-definition-of-done)

* For code quality, add SonarQube and identify your technical debt and track it
  ![](improve-processes.png)  

* For application/server performance, add automated load tests, add code to auto scale up on Azure

* For application usage, concentrate on features that get used the most and improve and streamline those features
