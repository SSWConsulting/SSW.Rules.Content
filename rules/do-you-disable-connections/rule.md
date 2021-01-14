---
type: rule
archivedreason: 
title: Do you disable connections?
guid: 1071b5f7-6efa-4e36-9987-39c04725a008
uri: do-you-disable-connections
created: 2015-08-12T15:42:01.0000000Z
authors: []
related: []
redirects:
- do-you-disable-connections1

---

It is important that while you're upgrading, nobody can check in.  Any check-ins after you backup your database will be lost.

To make sure that nobody can change anything during the upgrade, follow these steps.

<!--endintro-->

a.               Send out an email notifying everyone TFS will be unavailable for the upgrade period
 Follow [Rules to better Networks](http://www.ssw.com.au/SSW/Standards/Rules/RulesToBetterNetworks.aspx#rebootrestart)

b.              Make sure nobody can check in files:

c.                Open the TFS Administration Console on the server.

d.               Navigate to Application Tier / Team Project Collections.

e.              For each Team Project Collection, select it, and click "Stop Collection". Enter a useful message (this will be displayed to users trying to connect from Visual Studio) and click "Stop":

![](stop each term.png)

**Figure: Stop each Team Project Collection**



![](all team project.png)

**Figure: All Team Project Collections are stopped**



f.               In Visual Studio, confirm you can no longer connect to TFS

![](visual studio.png)

**Figure: Visual Studio shows the message that you entered when you stopped the Team Project Collection**
