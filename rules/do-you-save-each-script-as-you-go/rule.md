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



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>


  <ol>
    <li>When you have an error you can see exactly which script introduced it</li>
    <li>You don't have to use a compare tool like Red-Gate SQL Compare at the end of your development cycle</li>
    <li>Your application can automatically make schema changes</li>
    <li>The application can have a &quot;Create&quot; database button when installed for the first time</li>
    <li>The application can have an &quot;Upgrade&quot; button and work out itself if this new version needs scripts to be run</li>
    <li>The application can tell if it is an old version (as a newer version may have upgraded the schema), so you only use the latest clients</li>
    <li>The application can have a &quot;Reconcile&quot; feature that compares the current schema to what it should be</li>
</ol>
<br>
<dl class="image">
    <dt><img alt="" src="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/ChangeScripts.jpg" /> </dt>
    <dd>Figure&#58; A list of change SQL scripts, each file name is in the correct format </dd>
</dl>
<br>
<strong>Is there a file naming convention to follow?</strong><br>
The script file naming convention should be XXXXX_ObjectType_ObjectName_ColumnName_Description_SchemaMasterInitials.sql <br>
<br>
eg.&#160; 00089_Table_Employee_Gender_ChangeFromBitToChar_AC.sql<br>



