---
type: rule
archivedreason: Outdated
title: Do you know how to use Windows Integrated Authentication in Firefox?
guid: bb5713f5-6832-4704-8676-af0cafb7d9f7
uri: how-to-use-windows-integrated-authentication-in-firefox
created: 2016-02-02T19:28:24.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Peter Gfader
  url: https://ssw.com.au/people/peter-gfader
related: []
redirects:
- do-you-know-how-to-use-windows-integrated-authentication-in-firefox

---


<p>Internet Explorer has a great feature that you hardly notice. The Authentication credentials of the current user will be used by default.</p><dl class="image"><dt> 
      <img src="ie-integrated.JPG" alt="ie-integrated.JPG" /> 
   </dt><dd>Figure: Internet Explorer has the Integrated Authentication feature built in</dd></dl>​​ 
<p>In Firefox, if you sign-in to an internal server like SharePoint or CRM, you will get an authentication dialog. Even though you are already authenticated to the local domain.</p><dl class="image"><dt><img src="ff-auth1.JPG" alt="ff-auth1.JPG" /></dt><dd>Figure: We want to avoid authenticating using Firefox (so it works like IE)</dd></dl>
<br><excerpt class='endintro'></excerpt><br>
<h3>The Solution</h3>​​​ 
<ol><li>Open Firefox</li><li>Go to "about:config"</li><li>Click "I'll be careful, I promise!"</li><li>Enter in the Filter box above: "network.automatic"</li><li>You see 2 records</li><li>Double-click the second one - It is the key called network.automatic-ntlm-auth.trusted-uris</li><li>Enter the servers delimited by ",", e.g. "aphrodite, mermaid"</li><li>Close browser and test</li></ol>​​​ 
<dl class="image"><dt> <img src="ff-auth2.JPG" alt="ff-auth2.JPG" /> </dt><dd>Figure: Showed how to find "network.automatic-ntlm-auth.trusted-uris" by using filter: "network.automatic"</dd></dl><p>More info on this blog: <a href="http://www.cauldwell.net/patrick/blog/PermaLink%2cguid%2cc7f1e799-c4ae-4758-9de7-5c3e7a16f3da.aspx" target="_blank">Firefox and Sharepoint</a>.</p><p>
   <span style="color:#000000;font-family:verdana, sans-serif;font-size:12px;line-height:16.8px;"><b>Tip:</b> </span><span style="color:#000000;font-family:verdana, sans-serif;font-size:12px;line-height:16.8px;">To test this without the Integrated Authentication enabled, you need to clear your session. You do this via: </span><span style="color:#000000;font-family:verdana, sans-serif;font-size:12px;line-height:16.8px;"><b>Tools</b> | <b>Clear private data</b> | <b>Authenticated Sessions</b></span>.<b></b> <br></p><dl class="image"><dt><img src="ff-auth3.JPG" alt="ff-auth3.JPG" style="width:377px;" /></dt><dd>Figure: To test you will need to clear your "Authenticated Sessions" to completely logout from a site (SharePoint, CRM)</dd></dl>


