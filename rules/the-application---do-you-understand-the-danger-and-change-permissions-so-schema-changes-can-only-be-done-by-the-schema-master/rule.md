---
type: rule
title: The application - Do you understand the danger, and change permissions so "Schema Changes" can only be done by the "Schema Master"?
uri: the-application---do-you-understand-the-danger-and-change-permissions-so-schema-changes-can-only-be-done-by-the-schema-master
created: 2009-10-07T00:04:12.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> Having many people in a company&#160;that are able to make schema changes, can only lead to big problems. This gets worse if the application is powerful (eg. enabled with <a href="http&#58;//www.ssw.com.au/SSW/SQLDeploy/">SSW SQL Deploy</a> that can make schema changes itself) can make schema changes. <br>
<br>
Let's see&#160;how to fix&#160;the issue&#58; 
 </span>

To avoid this problem, only one person (the &quot;Schema Master&quot;) should have permissions to upgrade the database.
<dl>
    <dt><img alt="" src="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/FullPermission.jpg" /> </dt>
    <dd>Figure&#58; The db_owner role is granted for one person only – the &quot;Schema Master&quot; </dd>
</dl>
<dl class="image">
    <dt><img alt="" src="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/Adam.jpg" /> </dt>
    <dd>Figure&#58; And here is the &quot;Schema Master&quot; at SSW </dd>
</dl>



