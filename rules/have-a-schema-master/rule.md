---
type: rule
archivedreason: 
title: Do you have a "Schema Master"?
guid: c40124b5-f5e9-4f6c-8085-e3b91e645379
uri: have-a-schema-master
created: 2009-10-05T05:51:48.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-have-a-＂schema-master＂
- do-you-have-a-schema-master

---

You have a web site master right? This is the central point of contact if the site goes down.
 When developing an application, all members can code. However schema changes being done by many developers often can lead to trouble. 

 Who is "Schema Master"? What does he do?   
<!--endintro-->

![Figure: One person should be the 'Schema Master', on an average sized project (of 5-10 devs)](Nick.png)  

If your project has a database, you need to select a "Schema Master". This is the one person who should review all modifications to the database. These include:

* Creating, Modifying and Deleting tables and columns
* Relationships
* Modify [Controlled Lookup Data](/do-you-deploy-controlled-lookup-data)

 The "Schema Master" in a development shop is often the lead programmer on the team. They are in charge of all database changes and scripts. Team members should still feel free to make changes, just get them double checked by the Schema Master.     
![Figure: The Applications Database stores version info in a table called \_zsVersion](zsVersionTable.png)  

![Figure: Only a "Schema Master" checks in the .sql files](SQLScriptInTFS.png)
