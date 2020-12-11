---
type: rule
archivedreason: 
title: Do you turn Edit and Continue OFF?
guid: 93a7027b-64d4-4873-b9ab-ab3d2417e772
uri: do-you-turn-edit-and-continue-off
created: 2013-08-30T20:30:54.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 3
  title: Eric Phan
related: []

---

With VS2013, you get the long awaited 64 bit edit and continue, and it is turned on by default. Edit and Continue is great when you need to make a quick change to executing code. However, it has its downsides too:

* Web Development - Kills IISExpress when you stop
* Can lead to bad development practices (trying to debug instead of doing RED, GREEN, REFACTOR)



<!--endintro-->

This is why we recommend that it is turned OFF by default.
