---
type: rule
title: The application - Do you understand the danger, and change permissions so "Schema Changes" can only be done by the "Schema Master"?
uri: the-application---do-you-understand-the-danger-and-change-permissions-so-schema-changes-can-only-be-done-by-the-schema-master
created: 2009-10-07T00:04:12.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>

To avoid this problem, only one person (the &quot;Schema Master&quot;) should have permissions to upgrade the database.
<dl>
    <dt><img alt="" src="/Standards/CodeAndApplicationDesign/RulesToBetterSQLServerSchemaDeployment/PublishingImages/FullPermission.jpg" /> </dt>
    <dd>Figure&#58; The db_owner role is granted for one person only – the &quot;Schema Master&quot; </dd>
</dl>
<dl>
    <dt><img alt="" src="/Standards/CodeAndApplicationDesign/RulesToBetterSQLServerSchemaDeployment/PublishingImages/Adam.jpg" /> </dt>
    <dd>Figure&#58; And here is the &quot;Schema Master&quot; at SSW </dd>
</dl>



