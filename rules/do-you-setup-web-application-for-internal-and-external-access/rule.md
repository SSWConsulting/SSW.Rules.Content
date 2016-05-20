---
type: rule
title: Do you setup web application for internal and external access
uri: do-you-setup-web-application-for-internal-and-external-access
created: 2016-05-20T06:15:03.0000000Z
authors:
- id: 15
  title: Mark Liu

---



<span class='intro'> <blockquote style="margin&#58;0px 0px 0px 40px;border&#58;none;padding&#58;0px;"><p>- default zone should be over http, this is so search can access it over non-secure connection</p><p>- default zone should not be accessible outside of internal network</p><p>- extend the web application to an internet zone, this should be https to provide secure connection</p><p><span style="line-height&#58;1.6;">- this section should be extended with strategy to work with reverse proxy.</span></p></blockquote> </span>

<p>​&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; Reverse proxy handle https connection to client, and connects to SharePoint via http to reduce https overhead on SharePoint</p><p>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; SharePoint also needs to support https for internal traffic, if I click on a link to HTTPS it should work internally</p><p>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; For this scenario to work, web application needs to be extended 2 to 3 different zone</p><p>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;<strong>Default</strong>&#160;(http for internal and search)</p><p>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;<strong>Internet</strong>&#160;(http for reverse proxy)</p><p>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;<strong>Intranet</strong>&#160;(https for internal https link)​</p>


