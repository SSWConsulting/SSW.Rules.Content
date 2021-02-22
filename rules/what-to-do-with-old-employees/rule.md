---
type: rule
archivedreason: 
title: What to do with old employees?
guid: 11d6567c-c718-4297-aad1-c1a463e0b7c4
uri: what-to-do-with-old-employees
created: 2017-01-17T11:02:26.0000000Z
authors:
- title: Danijel Malik
  url: https://ssw.com.au/people/danijel-malik
related: []
redirects: []

---


When migrating from TFS to the cloud you will find that a list of historical users may be quite long.<br>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt>​​<img src="old-employees-to-the-cloud.jpg" alt="old-employees-to-the-cloud.jpg" />​​<span style="color:#555555;font-size:0.9rem;font-weight:bold;">Figure: TFS Identity Mapping​</span>​</dt></dl><p>Many of these users are likely to be gone but they are preserved in TFS for historical purposes. What are you going to do with them? <br>       <b>A) </b>All account stays active (total 700 in AD) – this is a hard one because you need to bring all accounts in Azure AD and generally you don’t need those users<br>       
   <b>B)  </b>Old employees are carried over as phantom  (so only 40 are migrated) – Recommended because you will still see the history but not those accounts are not active anymore<br>       Eg. If Paul Stovell comes back he needs a new account (because you can't reuse the SID)<br></p>


