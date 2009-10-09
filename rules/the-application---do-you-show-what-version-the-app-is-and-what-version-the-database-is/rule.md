---
type: rule
title: The application - Do you show what version the App is, and what version the Database is?
uri: the-application---do-you-show-what-version-the-app-is-and-what-version-the-database-is
created: 2009-10-05T05:26:57.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> 
  <dl class="image">
    <dt><img width="625" height="522" alt="" style="width&#58;576px;height&#58;475px;" src="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/LinkAuditor.png" /> </dt>
    <dd>Figure&#58; Everyone shows the version number somewhere on their app </dd>
</dl>
...but databases also need a version number.<br>
<br>
Let's see&#160;how to show the Database version&#58;&#160; 
 </span>


  <dl class="image">
    <dt><img alt="" src="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/zsVersionTable.png" /> </dt>
    <dd>Figure&#58; The applications database should have a table storing the version info (the table is called _zsVersion). See an example of this in <a href="http&#58;//www.ssw.com.au/SSW/LinkAuditor/">SSW Link Auditor</a> </dd>
</dl>
<dl class="image">
    <dt><img alt="" src="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/LinkAuditorVersion.png" /> </dt>
    <dd>Figure&#58; The user can clearly see the Database version is&#160;62&#160;after clicking &quot;Configure...&quot; button in wizard &quot;Storage Mechanism&quot;. See an example of this in <a href="http&#58;//www.ssw.com.au/SSW/LinkAuditor/">SSW Link Auditor</a> </dd>
</dl>
<dl class="image">
    <dt><img alt="" src="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/ChangeScripts.jpg" /> </dt>
    <dd>Figure&#58; The Application keeps all the scripts in a folder called SQLScripts (this allows the application to upgrade itself and give the Reconciliation functionality) </dd>
</dl>



