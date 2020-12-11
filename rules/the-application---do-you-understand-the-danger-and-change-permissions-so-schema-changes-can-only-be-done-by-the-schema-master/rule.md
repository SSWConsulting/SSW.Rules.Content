---
type: rule
archivedreason: 
title: The application - Do you understand the danger, and change permissions so "Schema Changes" can only be done by the "Schema Master"?
guid: b2b57d68-851b-474c-865a-fcb66b6ee20a
uri: the-application---do-you-understand-the-danger-and-change-permissions-so-schema-changes-can-only-be-done-by-the-schema-master
created: 2009-10-07T00:04:12.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

Having many people in a company that are able to make schema changes, can only lead to big problems. This gets worse if the application is powerful (eg. enabled with [SSW SQL Deploy](http://www.ssw.com.au/SSW/SQLDeploy/) that can make schema changes itself) can make schema changes. 

 Let's see how to fix the issue:   
<!--endintro-->
 To avoid this problem, only one person (the "Schema Master") should have permissions to upgrade the database. <dl>    &lt;dt&gt;<img alt="" src="FullPermission.jpg"> &lt;/dt&gt;
    <dd>Figure: The db_owner role is granted for one person only – the "Schema Master" </dd></dl><dl class="image">    &lt;dt&gt;<img alt="" src="Adam.jpg"> &lt;/dt&gt;
    <dd>Figure: And here is the "Schema Master" at SSW </dd></dl>
