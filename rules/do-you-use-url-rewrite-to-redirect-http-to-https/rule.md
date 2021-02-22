---
type: rule
archivedreason: 
title: Do you use URL Rewrite to redirect HTTP to HTTPS?
guid: 4abd7577-97ce-4466-8eb0-2a50ed108250
uri: do-you-use-url-rewrite-to-redirect-http-to-https
created: 2016-08-16T08:47:17.0000000Z
authors:
- title: Stanley Sidik
  url: https://ssw.com.au/people/stanley-sidik
related: []
redirects: []

---


​Using IIS URL Rewrite Module, Web administrators can easily set up rules to define URL rewriting behavior based on HTTP headers, HTTP response or request headers, IIS server variables, and programmatic rules.​​​ HTTP to HTTPS redirect helps boost your Google site ranking as well as adding enforcing SSL security.<br><div><br></div>
<br><excerpt class='endintro'></excerpt><br>
<div>​First you must download the IIS URL Rewrite module from Web Platform Component Installer. Ensure that a valid SSL Certificate is installed in IIS Server​. <br></div><div><br></div><div>1. Open URL Rewrite and begin with Add Rule(s) | Blank rule (Inbound rules)<br></div><div>2. Name the rule "HTTP to HTTPS redirect"<br></div><div>3. Add Pattern <strong>​(.*)</strong><br></div><div>​4. Add Conditions</div><blockquote style="margin-left:40px;border:none;"><div>​- Condition input: <strong>​{HTTPS}</strong><br></div><div><strong>- </strong>Pattern: <strong>off</strong></div></blockquote>​5. Add Action<div><blockquote style="margin-left:40px;border:none;"><div>- Action type: Redirect<br></div><div>- Action Properties: <strong>https://{HTTP_HOST}/{R:1}</strong><br></div></blockquote></div><blockquote style="margin-left:40px;border:none;">- Redirect type: Found (302)</blockquote>​6. Apply | Back to Rules<div><div><br></div><div></div><div><dt style="border:none;"><img alt="Designing border protection." src="IISURLRewrite.jpg" class="ms-rte-paste-setimagesize" style="margin:5px;padding:15px;border:1px solid #cccccc;width:750px;background:#eeeeee;" /> <br></dt><dd style="padding-left:20px;border:none;line-height:16px;background-attachment:initial;background-size:initial;background-origin:initial;background-clip:initial;background-position:initial;background-repeat:no-repeat;">Figure: HTTP to HTTPS redirect using IIS URL Rewrite module<br>​<br></dd></div></div><p><br></p>


