---
type: rule
archivedreason: 
title: Do you have a Validation page (the /zsValidate) for your web server?
guid: 73a982e8-dd89-4818-8fe1-e3d3d980d7e9
uri: do-you-have-a-validation-page-the-zsvalidate-for-your-web-server
created: 2016-11-16T16:43:56.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

How can you know that all components are working correctly on your site? It is vitally important to have a 'Health Check' page to validate everything is working correctly. This page will check the server and make sure:

* all the DLLs are present (and registered for COM ones)
* all the web services are working
* all the databases are alive, etc.



<!--endintro-->
<dl class="image">&lt;dt&gt;<img src="../../assets/la-footer.jpg" alt="Link Auditor footer" data-pin-nopin="true" style="width:700px;">&lt;/dt&gt;<dd>Figure: <a href="https://sswlinkauditor.com/">Link Auditor</a> server info</dd></dl>
You would be surprised how many dependencies a large web page can have.The advantage of this page is if you ever need to redeploy your application on another server or you have some pages that are just not working as planned you can load up this page and get a quick diagnostics of your website.
<dl class="image">&lt;dt&gt;<img src="../../assets/ValidateSetup.jpg" alt="Validate Setup" style="width:640px;">&lt;/dt&gt;<dd>Figure: One of the components on this web site is down</dd></dl><dl class="image">&lt;dt&gt;<img src="../../assets/ValidationTests.jpg" alt="Validation Tests" style="width:750px;">&lt;/dt&gt;<dd>Figure: Automatically validating our website</dd><p>See <a href="https://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterUnitTests.aspx#zsValidatePage">SSW Rules - Do you have a zsValidate page to test your website dependencies?</a></p>
<br></dl>
