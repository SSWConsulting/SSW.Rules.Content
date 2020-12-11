---
type: rule
archivedreason: 
title: 'DevOps – Stage 4: Do you continually improve processes?'
guid: ca702756-d411-4bf3-90ee-1faaf98f2f1f
uri: devops--stage-4-do-you-continually-improve-processes
created: 2016-03-07T18:51:30.0000000Z
authors:
- id: 3
  title: Eric Phan
- id: 1
  title: Adam Cogan
related: []

---

Now that you’ve got the numbers, you can then make decisions on what needs improvement and go through the DevOps cycle again.

Here are some examples:

<!--endintro-->

* For exceptions, review your exception log (ELMAH, RayGun, HockeyApp)
    * Add the important ones onto your backlog for prioritization
    * Add an ignore to the exceptions you don't care about to reduce the noise (e.g. 404 errors)
    * You can do this as the exceptions appear, or prior to doing your Sprint Review as part of the backlog grooming
    * You don't have to get the exception log down to 0, just action the important ones and aim to reduce the noise so that the log is still useful
* For code quality, add getting Code Auditor and ReSharper to 0 on files you’ve changed to your Definition of Done
* * See [https://rules.ssw.com.au/done-do-you-go-beyond-done-and-follow-a-definition-of-done](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=6449ae79-ba88-447e-aa48-36173029a2af)
* For code quality, add SonarQube and identify your technical debt and track it<dl class="image">&lt;dt&gt;<img src="improve-processes.png" alt="improve-processes.png">&lt;/dt&gt;</dl>
* For application/server performance, add automated load tests, add code to auto scale up on Azure
* For application usage, concentrate on features that get used the most and improve and streamline those features
