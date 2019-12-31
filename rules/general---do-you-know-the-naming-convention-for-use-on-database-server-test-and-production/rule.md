---
type: rule
title: General - Do you know the naming convention for use on database server test and production?
uri: general---do-you-know-the-naming-convention-for-use-on-database-server-test-and-production
created: 2019-11-14T21:59:12.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p class="ssw15-rteElement-P">Generally, every client should have a dev and a test database, so the dev database needs to have the postfix &quot;Dev&quot; and the test database need to have the postfix &quot;Test&quot;(E.g. SSWCRMDev, SSWCRMTest). However, you don't need any postfix for the&#160;production database.​​​<br><br></p> </span>

<dl class="badImage"><dt><img src="/PublishingImages/BadDBName.gif" alt="BadDBName.gif" />​</dt><dd>Figure&#58; Bad Example -&#160;Database with bad names<br></dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/GoodDBName.gif" alt="GoodDBName.gif" /></dt><dd>Figure&#58; Good Example -&#160;​Database with standard names</dd></dl>​<br>


