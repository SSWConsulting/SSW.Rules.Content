---
type: rule
title: The application - Do you understand the danger, and change permissions so
  "Schema Changes" can only be done by the "Schema Master"?
uri: the-application-do-you-understand-the-danger-and-change-permissions-so-schema-changes-can-only-be-done-by-the-schema-master
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - the-application-do-you-understand-the-danger-and-change-permissions-so-＂schema-changes＂-can-only-be-done-by-the-＂schema-master＂
created: 2009-10-07T00:04:12.000Z
archivedreason: Superseded by the rule [https://www.ssw.com.au/rules/have-a-schema-master](/rules/have-a-schema-master)
guid: b2b57d68-851b-474c-865a-fcb66b6ee20a
---
Having many people in a company that are able to make schema changes, can only lead to big problems. This gets worse if the application is powerful (eg. enabled with [SSW SQL Deploy](https://sqldeploy.com/) that can make schema changes itself) can make schema changes.

Let's see how to fix the issue:

<!--endintro-->

To avoid this problem, only one person (the "Schema Master") or the release pipeline should have permissions to upgrade the database.

![Figure: The db_owner role is granted for one person only – the "Schema Master"](FullPermission.jpg)

![Figure: And here is the "Schema Master" at SSW](nick.png)
