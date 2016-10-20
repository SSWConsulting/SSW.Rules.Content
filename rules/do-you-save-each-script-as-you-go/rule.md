---
type: rule
title: Do you save each script as you go?
uri: do-you-save-each-script-as-you-go
created: 2009-10-06T23:42:21.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 40
  title: Igor Goldobin

---



<span class='intro'> Every time a change is made to your product's SQL Server Database, script out the change. You can use SQL Management Studio or VS.NET (you can find old guys that still use Enterprise Manager or Query Analyzer), but every time you make changes you must save the change as a .sql script file so any alterations are scripted. <br>
<br>
Everything you do on your database will be done at least three times (<a shape="rect" href="/do-you-have-separate-development-testing-and-production-environments">once on development, once test and once on production</a>). Change control is one of the most important processes to ensuring a stable database system.&#160;<br>
<br>
Keep the scripts in a separate directory with only .sql files <br>
eg.&#160;&#160;C&#58;\Program Files\SSW Time PRO.NET\SQLScripts&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160; (32 bit)<br>
&#160;or&#160;&#160;C&#58;\Program Files (x86)\SSW Time PRO.NET\SQLScripts&#160; (64 bit)<br>
<br>
Later on you will get these&#160;7 benefits&#58; 
 </span>

<ol><li>​When you have an error you can see exactly which script introduced it </li><li>You don't have to use a compare tool like Red-Gate SQL Compare at the end of your development cycle </li><li>Your application can automatically make schema changes </li><li>The application can have a &quot;Create&quot; database button when installed for the first time </li><li>The application can have an &quot;Upgrade&quot; button and work out itself if this new version needs scripts to be run </li><li>The application can tell if it is an old version (as a newer version may have upgraded the schema), so you only use the latest clients </li><li>The application can have a &quot;Reconcile&quot; feature that compares the current schema to what it should be </li></ol>
<br>
<dl class="image"><dt> 
      <img src="/PublishingImages/ChangeScripts.jpg" alt="" />&#160;</dt><dd>Figure&#58; A list of change SQL scripts, each file name is in the correct format </dd></dl>
<br>
<strong>Is there a file naming convention to follow?</strong><br> The script file naming convention should be XXXXX_ObjectType_ObjectName_ColumnName_Description_SchemaMasterInitials.sql 
<br><br> eg.&#160; 00089_Table_Employee_Gender_ChangeFromBitToChar_AC.sql
<div>
   <br>
</div><div>
   <strong>What are the rules for Entity Framework Code Fi​​rst?</strong><br></div><div>Similar principles apply when using Entity Framework Code First. Every change you do to the schema must be either&#160;saved in code or scripted out as per above. We recommend using Migrations feature of Entity Framework 6. It allows you to keep track of all the changes in the similar fashion as SQL Deploy. Watch <a href="http&#58;//tv.ssw.com/4902/use-code-first-entity-framework-brendan-richards">this video</a> to learn more. We also recommend using SSW SQL Validate tool to make sure your schema hasn't been manually&#160;modified.​</div>


