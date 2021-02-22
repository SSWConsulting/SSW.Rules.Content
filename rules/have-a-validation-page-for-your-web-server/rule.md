---
type: rule
archivedreason: 
title: Do you have a Validation page (the /zsValidate) for your web server?
guid: 73a982e8-dd89-4818-8fe1-e3d3d980d7e9
uri: have-a-validation-page-for-your-web-server
created: 2016-11-16T16:43:56.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-have-a-validation-page-the-zsvalidate-for-your-web-server
- do-you-have-a-validation-page-(the-zsvalidate)-for-your-web-server

---


<p>How can you know that all components are working correctly on your site? It is vitally important to have a 'Health Check' page to validate everything is working correctly. This page will check the server and make sure:</p><ul><li>all the DLLs are present (and registered for COM ones) <br></li><li>all the web services are working</li><li>all the databases are alive, etc. <br></li></ul><br>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt><img src="../../assets/la-footer.jpg" alt="Link Auditor footer" data-pin-nopin="true" style="width:700px;" /></dt><dd>Figure: <a href="https://sswlinkauditor.com/">Link Auditor</a> server info</dd></dl><p>You would be surprised how many dependencies a large web page can have.The advantage of this page is if you ever need to redeploy your application on another server or you have some pages that are just not working as planned you can load up this page and get a quick diagnostics of your website.</p><dl class="image"><dt><img src="../../assets/ValidateSetup.jpg" alt="Validate Setup" style="width:640px;" /></dt><dd>Figure: One of the components on this web site is down</dd></dl><dl class="image"><dt><img src="../../assets/ValidationTests.jpg" alt="Validation Tests" style="width:750px;" /></dt><dd>Figure: Automatically validating our website</dd><p>See <a href="https://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterUnitTests.aspx#zsValidatePage">SSW Rules - Do you have a zsValidate page to test your website dependencies?</a></p>
​​<br></dl>


