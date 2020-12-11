---
type: rule
archivedreason: 
title: Do you assume catastrophic failure before touching a server?
guid: 8b40cdcc-f358-4b1e-a102-9152e056e724
uri: do-you-assume-catastrophic-failure-before-touching-a-server
created: 2014-09-03T19:21:57.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 47
  title: Stanley Sidik
related: []

---

If you are going to install a service pack on a machine, moving a virtual server to another drive or doing any critical system level changes, make sure you back up your machine first. For virtualized machine, make sure you back up all related files, including vhd, avhd etc.

<!--endintro-->

You should already assume there could be catastrophic failure after these kind of operations and you should always be prepared for them by having a full backup somewhere. This is especially important when you are working your production or critical servers.
