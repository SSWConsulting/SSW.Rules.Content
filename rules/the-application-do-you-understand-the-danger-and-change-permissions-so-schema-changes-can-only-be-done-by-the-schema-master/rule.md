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

Having many people in a company that are able to make schema changes, can only lead to big problems. This gets worse if the application is powerful (eg. enabled with [SSW SQL Deploy](http://www.ssw.com.au/SSW/SQLDeploy/) that can make schema changes itself) can make schema changes. 

 Let's see how to fix the issue:   
<!--endintro-->
 To avoid this problem, only one person (the "Schema Master") should have permissions to upgrade the database.      ![](FullPermission.jpg)      Figure: The db\_owner role is granted for one person only – the "Schema Master"        
![Figure: And here is the "Schema Master" at SSW](Adam.jpg)
