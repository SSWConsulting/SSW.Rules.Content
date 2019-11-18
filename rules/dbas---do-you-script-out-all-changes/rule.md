---
type: rule
title: ​DBAs - Do you script out all changes?
uri: dbas---do-you-script-out-all-changes
created: 2019-11-18T19:21:18.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>Every time a change is made to your product's SQL Server Database, script out the change. You can use Enterprise Manager, VS.NET or Query Analyzer but every time you make changes you must save the change as a .sql script file so any alterations are scripted. Everything at SSW is usually done three times, once on Development, once on Staging and once on Production. Change control is one of the most important processes to ensuring a stable database system.<br></p><p>Keep the scripts in a separate directory to any other scripts or files. This way you can always go back to them and find out what alterations you have made to the database in version xxx to find errors. If you have all the scripts you are able to rebuild the database from scratch. At SSW we name this folder SQLChangeScripts so as to not confuse it with other script folders.​​<br></p> </span>

<dl class="image"><dt>
      <img src="/PublishingImages/SQLChangeScripts.jpg" alt="SQLChangeScripts.jpg" />
   </dt><dd>Figure&#58;&#160;A list of change SQL scripts, each file name is in the correct format</dd></dl><p>The script file format should be&#58; &lt;version&gt;_&lt;description&gt;.sql</p><p>The &lt;version&gt; should be a number which is padded with leading zeros (0) on the right to firm 3 or 4 digits (however long we need).​​​<br></p><h3 class="ssw15-rteElement-H3">What if you are using a code generator?​​<br></h3><p class="ssw15-rteElement-P">Every time we use&#160;Next Generation&#160;, it creates its own Generated Stored Procs in the Database Project of our Solution. The folder it is kept in is called &quot;Auto-Generated Stored Procedures&quot;.​​<br></p><p>The scripts found within this folder are as follows&#58;<br></p><ul><li>010_ViewsForStoredProcedures.sql</li><li>020_StoredProcedures_Select.sql</li><li>030_StoredProcedures_Insert.sql</li><li>040_StoredProcedures_Update.sql</li><li>050_StoredProcedures_Delete.sql</li></ul><p class="ssw15-rteElement-P">After re-generation of code in the solution, these scripts will be updated with the required stored procs for new Database Objects found in the application. The problem is, however, that every time a re-generation occurs these files must always be added to the large list of scripts in the &quot;SQLChangeScripts&quot; folder as shown above.​<br></p><p class="ssw15-rteElement-P">To solve the issue of continually piling up these scripts every time you use&#160;Next Generation&#160;, it is recommended that the scripts are copied over to the &quot;SQLChangeScripts&quot; folder, and the names should not be changed.​<br></p>By only modifying the first three numbers accordingly for the correct script sequence, you will be able to find all other Next Generation stored procs, as shown in the figure below.<br> 
<dl class="image">
   <dt>
      <img src="/PublishingImages/SQLScriptList.gif" alt="SQLScriptList.gif" />​</dt><dd>Figure&#58; Previous NextGen scripts can be removed except the last NextGen script file e.g 008_StoredProcedures_Delete.sql should not be deleted as it may be the last script in a previous version which SQL Deploy may need for reference<br></dd></dl><p class="ssw15-rteElement-P">Since the previous NextGen Scripts are considered outdated with the newly generated scripts; deleting the previous NextGen scripts will not affect the Database Objects found in the application.​​<br></p><p class="ssw15-rteElement-P">Deleting these scripts will in fact decrease the list of scripts significantly and save a very large amount of time when upgrading the database using SQL Deploy, especially when the generated scripts contain a lot of SQL commands.​​<br></p><p class="ssw15-rteElement-P">After the Upgrade, you should do a check on the database with the scripts just to make sure they Reconcile.​​<br></p>


