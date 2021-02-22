---
type: rule
archivedreason: 
title: The application - Do you understand the danger, and change permissions so "Schema Changes" can only be done by the "Schema Master"?
guid: b2b57d68-851b-474c-865a-fcb66b6ee20a
uri: the-application-do-you-understand-the-danger-and-change-permissions-so-schema-changes-can-only-be-done-by-the-schema-master
created: 2009-10-07T00:04:12.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- the-application-do-you-understand-the-danger-and-change-permissions-so-＂schema-changes＂-can-only-be-done-by-the-＂schema-master＂

---


Having many people in a company that are able to make schema changes, can only lead to big problems. This gets worse if the application is powerful (eg. enabled with <a href="http://www.ssw.com.au/SSW/SQLDeploy/">SSW SQL Deploy</a> that can make schema changes itself) can make schema changes. <br>
<br>
Let's see how to fix the issue: 

<br><excerpt class='endintro'></excerpt><br>
To avoid this problem, only one person (the "Schema Master") should have permissions to upgrade the database.
<dl>
    <dt><img alt="" src="FullPermission.jpg" /> </dt>
    <dd>Figure: The db_owner role is granted for one person only – the "Schema Master" </dd>
</dl>
<dl class="image">
    <dt><img alt="" src="Adam.jpg" /> </dt>
    <dd>Figure: And here is the "Schema Master" at SSW </dd>
</dl>



