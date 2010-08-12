---
type: rule
title: Do you have a "Schema Master"?
uri: do-you-have-a-schema-master
created: 2009-10-05T05:51:48.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> You have a web site master right? This is the central point of contact if the site goes down.<br>
When developing an application, all members can code. However schema changes being done by many developers often can lead to trouble. <br>
<br>
Who&#160;is &quot;Schema Master&quot;? What does he do? 
 </span>


  <dl class="image">
    <dt><img alt="" src="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/Nick.png" /> </dt>
    <dd>Figure&#58; One person should be the 'Schema Master', on an average sized project (of 5-10 devs) </dd>
</dl>
<p style="margin&#58;0cm 0cm 0pt;">If your project has a database, you need to select a &quot;Schema Master&quot;. This is the one person who is allowed to make modifications to the database. These include&#58;</p>
<ul>
    <li>Creating, Modifying and Deleting tables and columns </li>
    <li>Relationships </li>
    <li>Modify <a href="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/Pages/DoYouDeployLookupData.aspx">Controlled Lookup Data</a> </li>
</ul>
The &quot;Schema Master&quot; in a development shop is often the lead programmer on the team. He is in charge of all database changes and scripting them out and checking them into source control.
<dl class="image">
    <dt><img alt="" src="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/zsVersionTable.png" /> </dt>
    <dd>Figure&#58; The Applications Database stores version info in a table called _zsVersion </dd>
</dl>
<dl class="image">
    <dt><img alt="" src="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/SQLScriptInTFS.png" /> </dt>
    <dd>Figure&#58; Only a &quot;Schema Master&quot; checks in the .sql files </dd>
</dl>



