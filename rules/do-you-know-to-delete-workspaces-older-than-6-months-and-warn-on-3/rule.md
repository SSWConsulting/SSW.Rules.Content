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


<p>The more workspaces you have the more load the TFS server is under when users check in and out. TFS has to check all of the workspaces for other checkouts of the same files which can be intensive if you have a lot of workspaces.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>If a developer had code checked out to a workspace that they have not even looked at in months, what is the likelihood that they even remember what changes they were making?</p>
<ul>Why do workspaces build up? <li>Developers use multiple computers </li>
<li>Developers use volatile virtual computers </li>
<li>Developers reinstall their workstation </li>
<li>Developers get new workstations </li>
<li>Developers leave </li></ul>
<ul>Developer checklist&#58; <li>Check workspaces often to see what you don't need </li>
<li>Delete any workspaces you no longer need </li></ul>
<ul>TFS Master Checklist&#58; <li>Delete all workspaces that have not been edited in 6 months </li>
<li>Warn developers for workspaces that have not been accessed in 3 months </li></ul>
<dl><dt><img alt="Longtime Workspaces" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/LongtimeWorkspaces.jpg" /></dt>
<dd>Figure&#58; Bad example - Rebecca has a workspace that has not been accessed in a while </dd></dl>
<dl><dt><img alt="Current Workspaces" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/CurrentWorkspaces.jpg" /></dt>
<dd>Figure&#58; Good example - All of Julian's workspaces are current </dd></dl>
<ol><li>Open VS 2010, File | Source Control | WorkSpaces, click the &quot;Show remote workspaces&quot;&#58; <dl><dt><img alt="Manage Workspaces " src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/ManageWorkspaces.jpg" /></dt>
<dd>Figure&#58; Manage Workspaces </dd></dl></li>
<li>Keep press &quot;Ctrl&quot;, select the workspaces which haven't been used for a long time. </li>
<li>Click &quot;Remove&quot; button.</li></ol>


