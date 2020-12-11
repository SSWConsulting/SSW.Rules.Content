---
type: rule
archivedreason: 
title: Sample - Do you avoid dropping a user's database when you attempt to create a database?
guid: 5092e56e-d570-4efa-b148-8a9344cd61be
uri: sample---do-you-avoid-dropping-a-users-database-when-you-attempt-to-create-a-database
created: 2012-11-27T03:09:46.0000000Z
authors: []
related: []

---

If you have an SQL script that runs as part of your install you should always make sure that it does not drop the database first. When you typically auto-generate a script file from some of the SQL applications (such as Enterprise Manager) it will automatically attempt to drop a database if it already exists. This is bad practice as a company may already have a large investment in the data already in the database and dropping it may cause them to lose this investment.

<!--endintro-->

If you know which machine the database is going to be installed from within your application you should first check that it doesn't already exist and prompt the user accordingly to let them know that they should first manually delete the database. For example the install of the SQL Reporting Services setup handles this problem in an appropriate and simple manner (although some additional help could be provided).
<dl class="goodImage">&lt;dt&gt;<img width="630" height="127" src="../../assets/InterfacesDBAlreadyExists.gif" alt="Reporting Services Setup - Database Already Exists" style="width:600px;height:100px;">&lt;/dt&gt;
<dd>Good example – an application should never automatically delete a database, not even a sample database</dd></dl>
If you cannot be sure of the machine that the database is going to be installed on then you should make use of third party .sql script execution managers such as [SSW SQL Deploy](http://www.ssw.com.au/ssw/SQLDeploy) to ensure that when you attempt creation of databases where the database already exists then things will run smoothly.
