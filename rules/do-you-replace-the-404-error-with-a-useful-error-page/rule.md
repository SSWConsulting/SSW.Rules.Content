---
type: rule
archivedreason: 
title: Do you replace the 404 error with a useful error page?
guid: a006213a-e97b-46a7-a66b-beb52b205533
uri: do-you-replace-the-404-error-with-a-useful-error-page
created: 2016-08-11T17:30:01.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 16
  title: Tiago Araujo
related: []

---


​​​​<p>Error page, you say? You worked hard to make sure my site has no errors!! Well, surfers don't always type URLs accurately. No website is immune to such errors.
</p><p>A well-designed custom error page encourages surfers to remain in your site and help them to the right page. Although it's possible to redirect error codes straight to your homepage, that doesn't tell visitors what's going on. It's more user-friendly to explain that there was a problem and provide some alternatives. Supply a link to your home page or other links, or offer your site's search function if you have one. ​<br></p>
​<br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea"><customErrors mode="Off"></customErrors> <br></p><dd class="ssw15-rteElement-FigureBad"> Figure: This is the default code on​ web.config <br></dd><p class="ssw15-rteElement-CodeArea"><customErrors mode="RemoteOnly" defaultRedirect="/ssw/ErrorPage.aspx"><br><error statusCode="404" redirect="/ssw/SSWCustomError404.aspx"><br></customErrors></p><dd class="ssw15-rteElement-FigureGood">Figure: this is the current code in the web.config of the SSW Site  </dd><p>For ASP.NET website, the detailed information would be presented to the remote machines when an unhandled error occurs if the customErrors mode is off.</p><p>This error information is useful for the developer to do debugging. However, it would leak out some confidential information which could be used to get into your system by the hackers. We can assume that if a SQL exception occurs by accident, which may expose database sensitive information (e.g. connection string; SQL script). So, to prevent these leaks, you should set the "mode" attribute of the tag <customerrors> to "RemoteOnly" or "On" in the web.config file and create a user-friendly customized error page to replace the detailed error information.<br></p><p class="ssw15-rteElement-CodeArea"><customErrors mode="RemoteOnly" defaultRedirect="GenericErrorPage.htm"></customErrors></p><dd class="ssw15-rteElement-FigureGood"> Figure: Turning on "customErrors" protects sensitive information against Hacker  </dd><dl class="badImage"><dt> <img src="404-bad.jpg" alt="404-bad.jpg" /> </dt><dd>Figure: Bad example - Unhandled error</dd></dl><dl class="goodImage"><dt> <img src="404-good.jpg" alt="404-good.jpg" /> </dt><dd>Figure: Good example - Custom error page </dd></dl><h3>Related rule</h3><ul><li><a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=0c5ba2ba-eb40-4b9e-afdc-c2bccd589b54">Do you avoid changing the URL on a 404 error?</a>
</li></ul>


