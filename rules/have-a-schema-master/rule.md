---
type: rule
title: Do you have a "Schema Master"?
uri: have-a-schema-master
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-have-a-＂schema-master＂
  - do-you-have-a-schema-master
created: 2009-10-05T05:51:48.000Z
archivedreason: null
guid: c40124b5-f5e9-4f6c-8085-e3b91e645379
---
You have a website master right? This is the central point of contact if the site goes down.
When developing an application, all members can code. However schema changes being done by many developers often can lead to trouble...

<!--endintro-->

To avoid this problem, only one person (the "Schema Master") or the release pipeline should have permissions to upgrade the database.

![Figure: The db_owner role is granted for one person only – the "Schema Master"](fullpermission.jpg)

Who is the "Schema Master"? What do they do?   

![Figure: One person should be the 'Schema Master', on an average sized project (of 5-10 devs)](Nick.png)

If your project has a database, you need to select a "Schema Master". This is the one person who should review all modifications to the database. These include:

* Creating, Modifying and Deleting tables and columns
* Relationships
* Modify [Controlled Lookup Data](/do-you-deploy-controlled-lookup-data)

The "Schema Master" in a development shop is often the lead programmer on the team. They are in charge of all database changes and scripts. Team members should still feel free to make changes, just get them double checked by the Schema Master.
![Figure: The Applications Database stores version info in a table called _zsVersion](zsVersionTable.png)  

![Figure: Only a "Schema Master" checks in the .sql files](SQLScriptInTFS.png)