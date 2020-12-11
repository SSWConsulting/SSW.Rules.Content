---
type: rule
archivedreason: 
title: Do you know to delete workspaces older than 6 months and warn on 3?
guid: d202fa40-dbec-4392-9eac-7fc878d8e81c
uri: do-you-know-to-delete-workspaces-older-than-6-months-and-warn-on-3
created: 2011-11-18T03:52:39.0000000Z
authors:
- id: 22
  title: David Klein
- id: 5
  title: Justin King
- id: 17
  title: Ryan Tee
- id: 6
  title: Tristan Kurniawan
related: []

---

The more workspaces you have the more load the TFS server is under when users check in and out. TFS has to check all of the workspaces for other checkouts of the same files which can be intensive if you have a lot of workspaces.

<!--endintro-->

If a developer had code checked out to a workspace that they have not even looked at in months, what is the likelihood that they even remember what changes they were making?

Why do workspaces build up?* Developers use multiple computers
* Developers use volatile virtual computers
* Developers reinstall their workstation
* Developers get new workstations
* Developers leave


Developer checklist:* Check workspaces often to see what you don't need
* Delete any workspaces you no longer need


TFS Master Checklist:* Delete all workspaces that have not been edited in 6 months
* Warn developers for workspaces that have not been accessed in 3 months

<dl>&lt;dt&gt;<img alt="Longtime Workspaces" src="LongtimeWorkspaces.jpg">&lt;/dt&gt;
<dd>Figure: Bad example - Rebecca has a workspace that has not been accessed in a while </dd></dl><dl>&lt;dt&gt;<img alt="Current Workspaces" src="CurrentWorkspaces.jpg">&lt;/dt&gt;
<dd>Figure: Good example - All of Julian's workspaces are current </dd></dl>
1. Open VS 2010, File | Source Control | WorkSpaces, click the "Show remote workspaces": <dl>&lt;dt&gt;<img alt="Manage Workspaces " src="ManageWorkspaces.jpg">&lt;/dt&gt;
<dd>Figure: Manage Workspaces </dd></dl>
2. Keep press "Ctrl", select the workspaces which haven't been used for a long time.
3. Click "Remove" button.
