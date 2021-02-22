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


You have a web site master right? This is the central point of contact if the site goes down.<br>
When developing an application, all members can code. However schema changes being done by many developers often can lead to trouble. <br>
<br>
Who is "Schema Master"? What does he do? 

<br><excerpt class='endintro'></excerpt><br>

  <dl class="image">
    <dt><img src="Nick.png" alt="" /> </dt>
    <dd>Figure: One person should be the 'Schema Master', on an average sized project (of 5-10 devs) </dd>
</dl>
<p style="margin:0cm 0cm 0pt;">If your project has a database, you need to select a "Schema Master". This is the one person who should review all modifications to the database. These include:</p>
<ul>
    <li>Creating, Modifying and Deleting tables and columns </li>
    <li>Relationships </li>
    <li>Modify <a href="/Pages/DoYouDeployLookupData.aspx">Controlled Lookup Data</a> </li>
</ul>
The "Schema Master" in a development shop is often the lead programmer on the team. They are in charge of all database changes and scripts. Team members should still feel free to make changes, just get them double checked by the Schema Master.<dl class="image">
    <dt><img src="zsVersionTable.png" alt="" /> </dt>
    <dd>Figure: The Applications Database stores version info in a table called _zsVersion </dd>
</dl>
<dl class="image">
    <dt><img src="SQLScriptInTFS.png" alt="" /> </dt>
    <dd>Figure: Only a "Schema Master" checks in the .sql files </dd>
</dl>



