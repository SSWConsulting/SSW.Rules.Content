---
type: rule
archivedreason: 
title: Do you get a developer to test the migration?
guid: 4f9b5655-299b-4c7d-b281-722e72a13d88
uri: do-you-get-a-developer-to-test-the-migration1
created: 2015-08-14T11:37:58.0000000Z
authors: []
related: []
redirects:
- do-you-get-a-developer-to-test-the-migration

---

It is important to get another developer to check the migration for issues.

<!--endintro-->
They should follow these steps:
a.      Start Visual Studio 2013

b.     Open Team Explorer and connect to the new TFS Server

c.      Confirm that they can:

.                Source Code - Browse the projects and code using the Source Code Explorer

a.               Source Code Operations - Get Latest on a file, make a change and check in

b.              Source Code History - View the history of a number of files in different projects

c.               Work Items - Browse and view recent work items

d.     Open Visual Studio 2015 and repeat steps 1 to 3.

e.      Test that your builds complete successfully on the upgraded build controller(s) and agent(s).

f.       Check that they can create a new Team Project in Visual Studio 2015

**Congratulations! You've completed a successful migration!**
