---
type: rule
archivedreason: 
title: Do you present the user with a nice error screen? (Web Only)
guid: 4ee8ca41-78bb-40c1-94cc-cf44a3b47622
uri: do-you-present-the-user-with-a-nice-error-screen-web-only
created: 2013-09-11T21:08:47.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Drew Robson
  url: https://ssw.com.au/people/drew-robson
related: []
redirects:
- do-you-present-the-user-with-a-nice-error-screen-(web-only)

---


<p>​​​Your users should never see the “yellow screen of death” in ASP.NET. Errors should be caught, logged and a user-friendly screen displayed to the user.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>This last part is done by specifying the customErrors element in the web.config file.</p><p>This will activate ASP.NET’s built in error page (e.g. MVC’s HandleErrorAttribute filter) which can then be customized to suit your application.</p><p><br></p><blockquote style="margin:0px 0px 0px 40px;border:none;padding:0px;">​<img src="error-screen-bad.jpg" alt="" style="line-height:20px;" /><p></p></blockquote><dl class="badImage"><dd>Figure: Bad Example – Yellow Screen of Death</dd></dl><dl class="goodImage"><dt><img src="error-screen-good.jpg" alt="" /></dt><dd>Figure: Good Example - Default ASP.NET MVC custom error page</dd><p class="ssw15-rteElement-P">​<br></p><p>​However, as a developer you still want to be able to view the detail of the exception in your local development environment. Use the below setting in your Web Application's web.config file to view the yellow screen locally but present a nice error screen to the user.<br></p><p></p><p><img src="14-08-2014-2-47-50-PM-compressor.png" alt="14-08-2014-2-47-50-PM-compressor.png" style="margin:5px;width:650px;" />​<span style="color:#555555;font-size:11px;font-weight:bold;line-height:16px;background-color:transparent;">​​​</span></p><dd class="ssw15-rteElement-FigureGood">​​​Figure: Good Example - Don't hide the yellow screen of death in the local environment</dd><p class="ssw15-rteElement-P"><br></p></dl>


