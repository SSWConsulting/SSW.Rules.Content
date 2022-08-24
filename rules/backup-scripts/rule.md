---
type: rule
archivedreason: 
title: Backup - Do you back up scripts?
guid: c0cbf1fa-785a-4f36-b6bf-d7e239a3286e
uri: backup-scripts
created: 2019-11-20T18:42:30.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- backup-do-you-back-up-scripts

---

Scripts are an important component in the operation of any database. This is why you should back up all your scripts and historical schema snapshots - so you can track the scripts that have been run and those that need to be deployed to test and production databases. We typically store these in source control such as VSS or Team Foundation Server as a Visual Studio Database project.

<!--endintro-->

You should regularly generate full scripts of all objects changed, keeping the following points in mind:

* Don't encrypt your database objects if you can avoid it - otherwise, they can't be scripted.

Use:

* Enterprise Manager Generate Scripts Wizard OR
* SQL DMO object model to script out the objects
