---
type: rule
title: Do you have a Validation page (the /zsValidate) for your web server?
uri: do-you-have-a-validation-page-the-zsvalidate-for-your-web-server
created: 2016-11-16T16:43:56.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>How can you know that all components are working correctly on your site? It is vitally important to have a 'Health Check' page to validate everything is working correctly. This page will check the server and make sure&#58;</p><ul><li>all the DLLs are present (and registered for COM ones) <br></li><li>all the web services are working</li><li>all the databases are alive, etc. <br></li></ul><br> </span>

<dl class="image"><dt><img src="https&#58;//www.ssw.com.au/ssw/standards/rules/Images/la-footer.jpg" alt="Link Auditor footer" data-pin-nopin="true" style="width&#58;700px;" /></dt><dd>Figure&#58;&#160;<a href="https&#58;//sswlinkauditor.com/">Link Auditor</a> server info</dd></dl><p>You would be surprised how many dependencies a large web page can have.The advantage of this page is if you ever need to redeploy your application on another server or you have some pages that are just not working as planned you can load up this page and get a quick diagnostics of your website.</p><dl class="image"><dt><img src="https&#58;//www.ssw.com.au/ssw/standards/rules/Images/ValidateSetup.jpg" alt="Validate Setup" style="width&#58;640px;" /></dt><dd>Figure&#58; One of the components on this web site is down</dd></dl><dl class="image"><dt><img src="https&#58;//www.ssw.com.au/ssw/standards/rules/Images/ValidationTests.jpg" alt="Validation Tests" style="width&#58;750px;" /></dt><dd>Figure&#58; Automatically validating our website</dd><p>See&#160;<a href="https&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterUnitTests.aspx#zsValidatePage">SSW Rules - Do you have a zsValidate page to test your website dependencies?</a></p>
​​<br></dl>


