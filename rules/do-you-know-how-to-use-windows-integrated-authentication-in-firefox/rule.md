---
type: rule
title: Do you know how to use Windows Integrated Authentication in Firefox?
uri: do-you-know-how-to-use-windows-integrated-authentication-in-firefox
created: 2016-02-02T19:28:24.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 12
  title: Peter Gfader

---



<span class='intro'> <p>Internet Explorer has a great feature that you hardly notice. The Authentication credentials of the current user will be used by default.</p><dl class="image"><dt> 
      <img src="/PublishingImages/ie-integrated.JPG" alt="ie-integrated.JPG" /> 
   </dt><dd>Figure&#58; Internet Explorer has the Integrated Authentication feature built in</dd></dl>​​ 
<p>In Firefox, if you sign-in to an internal server like SharePoint or CRM, you will get an authentication dialog. Even though you are already authenticated to the local domain.</p><dl class="image"><dt><img src="/PublishingImages/ff-auth1.JPG" alt="ff-auth1.JPG" /></dt><dd>Figure&#58; We want to avoid authenticating using Firefox (so it works like IE)</dd></dl> </span>

<h3>The Solution</h3>​​​ 
<ol><li>Open Firefox</li><li>Go to &quot;about&#58;config&quot;</li><li>Click &quot;I'll be careful, I promise!&quot;</li><li>Enter in the Filter box above&#58; &quot;network.automatic&quot;</li><li>You see 2 records</li><li>Double-click the second one - It is the key called network.automatic-ntlm-auth.trusted-uris</li><li>Enter the servers delimited by &quot;,&quot;, e.g. &quot;aphrodite, mermaid&quot;</li><li>Close browser and test</li></ol>​​​ 
<dl class="image"><dt> <img src="/PublishingImages/ff-auth2.JPG" alt="ff-auth2.JPG" /> </dt><dd>Figure&#58; Showed how to find &quot;network.automatic-ntlm-auth.trusted-uris&quot; by using filter&#58; &quot;network.automatic&quot;</dd></dl><p>More info on this blog&#58; <a href="http&#58;//www.cauldwell.net/patrick/blog/PermaLink%2cguid%2cc7f1e799-c4ae-4758-9de7-5c3e7a16f3da.aspx" target="_blank">Firefox and Sharepoint</a>.</p><p>
   <span style="color&#58;#000000;font-family&#58;verdana, sans-serif;font-size&#58;12px;line-height&#58;16.8px;"><b>Tip&#58;</b>&#160;</span><span style="color&#58;#000000;font-family&#58;verdana, sans-serif;font-size&#58;12px;line-height&#58;16.8px;">To test this without the Integrated Authentication enabled, you need to clear your session. You do this via&#58;&#160;</span><span style="color&#58;#000000;font-family&#58;verdana, sans-serif;font-size&#58;12px;line-height&#58;16.8px;"><b>Tools</b> | <b>Clear private data</b> | <b>Authenticated Sessions</b></span>.<b></b> <br></p><dl class="image"><dt><img src="/PublishingImages/ff-auth3.JPG" alt="ff-auth3.JPG" style="width&#58;377px;" /></dt><dd>Figure&#58; To test you will need to clear your &quot;Authenticated Sessions&quot; to completely logout from a site (SharePoint, CRM)</dd></dl>


