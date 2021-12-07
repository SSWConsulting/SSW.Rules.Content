---
type: rule
archivedreason: 
title: Do you disable connections for TFS 2015 migration?
guid: 1071b5f7-6efa-4e36-9987-39c04725a008
uri: disable-connections-tfs2015-migration
created: 2015-08-12T15:42:01.0000000Z
authors: 
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-disable-connections1

---

It is important that while you're upgrading, nobody can check in. Any check-ins after you backup your database will be lost.

To make sure that nobody can change anything during the upgrade, follow these steps.

<!--endintro-->

a. Send out an email notifying everyone TFS will be unavailable for the upgrade period

b. Make sure nobody can check in files:

c. Open the TFS Administration Console on the server.

d. Navigate to Application Tier / Team Project Collections.

e. For each Team Project Collection, select it, and click "Stop Collection". Enter a useful message (this will be displayed to users trying to connect from Visual Studio) and click "Stop":

![Figure: Stop each Team Project Collection](stop each term.png)

![Figure: All Team Project Collections are stopped](all team project.png)

f. In Visual Studio, confirm you can no longer connect to TFS

![Figure: Visual Studio shows the message that you entered when you stopped the Team Project Collection](visual studio.png)

