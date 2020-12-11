---
type: rule
archivedreason: 
title: General - Do you know the naming convention for use on database server test and production?
guid: 34ceccd7-b18b-4b55-a49e-df311676238e
uri: general---do-you-know-the-naming-convention-for-use-on-database-server-test-and-production
created: 2019-11-14T21:59:12.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

Generally, every client should have a dev and a test database, so the dev database needs to have the postfix "Dev" and the test database need to have the postfix "Test"(E.g. SSWCRMDev, SSWCRMTest). However, you don't need any postfix for the production database.

<!--endintro-->
<dl class="badImage">&lt;dt&gt;<img src="BadDBName.gif" alt="BadDBName.gif">&lt;/dt&gt;<dd>Figure: Bad Example - Database with bad names<br></dd></dl><dl class="goodImage">&lt;dt&gt;<img src="GoodDBName.gif" alt="GoodDBName.gif">&lt;/dt&gt;<dd>Figure: Good Example - Database with standard names</dd></dl>
