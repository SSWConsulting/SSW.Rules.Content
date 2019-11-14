---
type: rule
archivedreason: 
title: General - Do you know the naming convention for use on database server test and production?
guid: 34ceccd7-b18b-4b55-a49e-df311676238e
uri: naming-convention-for-use-on-database-server-test-and-production
created: 2019-11-14T21:59:12.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- general-do-you-know-the-naming-convention-for-use-on-database-server-test-and-production

---


<p class="ssw15-rteElement-P">Generally, every client should have a dev and a test database, so the dev database need to have the postfix &quot;Dev&quot; and the test database need to have the postfix &quot;Test&quot;(E.g. SSWCRMDev, SSWCRMTest). However, you don't need any postfix for production database.​​​<br><br></p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt><img src="/PublishingImages/BadDBName.gif" alt="BadDBName.gif" />​</dt><dd>Figure&#58; Database with bad names</dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/GoodDBName.gif" alt="GoodDBName.gif" /></dt><dd>Figure&#58; Database with standard names</dd></dl>​<br>


