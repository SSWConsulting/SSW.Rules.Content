---
type: rule
archivedreason: "Bugs are usually tracked using GitHub Issues (or similar) and Team Companion is dead. Superceded by related Rule"
title: Do you keep the best possible bug database?
guid: 6159eae3-6e8b-4999-8812-0907c53db7fd
uri: do-you-keep-the-best-possible-bug-database
created: 2009-02-28T09:44:02.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related:
- build-the-backlog
redirects: []

---

There are 101 bug databases on the market at the moment and of course many companies make up their own in-house systems.  

<!--endintro-->
![](bugs.jpg)
This is a common scenario: Your tester/client finds a bug, they log on to your on-line bug database, and enter the data, they save the error message as a gif and upload the image. As Project Manager, you get notified by email of the bug, you log on to the application, view the image, review the status, assign a priority, and assign it to a developer. The developer receives the email, logs on and sets about fixing the bug. When completed, they logs back on to the application, enters a completed date, and an email is sent to the tester/client. The tester/client logs on, and is told what to test, reviews the work, enters a checked by date, and the final email is sent to the manager who closes the bug.

Phew! That sounds like a lot of steps which is why most people resort to just sending an email. I believe most people send requests for tasks via email, if this is the case, why should developers have a separate "to-do" list, in the form of a bug-database in which they re-enter data?

MS TFS has an Outlook addin which can save you a lot of this work called Team Companion. This has a number of benefits including:

* Developers don't have to re-enter data
* TFS fully integrates your bug tracking with your source control.
* Managers can see important information like Tasks Completed and Tasks Assigned in TFS Reports
* Clients can see what developers are working on via TFS
