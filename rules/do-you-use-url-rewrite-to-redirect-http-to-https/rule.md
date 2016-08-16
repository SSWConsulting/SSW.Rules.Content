---
type: rule
title: Do you use URL Rewrite to redirect HTTP to HTTPS?
uri: do-you-use-url-rewrite-to-redirect-http-to-https
created: 2016-08-16T08:47:17.0000000Z
authors:
- id: 47
  title: Stanley Sidik

---



<span class='intro'> Using IIS URL Rewrite Module, Web administrators can easily set up rules to define URL rewriting behavior based on HTTP headers, HTTP response or request headers, IIS server variables, and programmatic rules.​​​ HTTP to HTTPS redirect helps boost&#160;your Google site ranking as well as adding enforcing SSL&#160;security.<div><div>
         <br>
         <br>
      </div><div><div>
            <br>
         </div><div>
            <br>
         </div></div></div> </span>

<p>​<br></p><div>First you must download the IIS URL Rewrite module from Web Platform Component Installer. Ensure that a valid&#160;SSL Certificate is installed in IIS&#160;Server​.&#160;</div><div><br></div><div>1. Open URL Rewrite and begin with Add Rule(s) | Blank rule (Inbound rules)<br></div><div>2. Name the rule &quot;HTTP to HTTPS redirect&quot;<br></div><div>3. Add Pattern&#160;<strong>​(.*)</strong><br></div><div>​4. Add Conditions</div><blockquote style="margin-left&#58;40px;border&#58;none;"><div>​- Condition input&#58;&#160;<strong>​&#123;HTTPS&#125;</strong><br></div><div><strong>-&#160;</strong>Pattern&#58;&#160;<strong>off</strong></div></blockquote>​5.&#160;Add Action<div><blockquote style="margin-left&#58;40px;border&#58;none;"><div>- Action type&#58; Redirect<br></div><div>- Action Properties&#58;&#160;<strong>https&#58;//&#123;HTTP_HOST&#125;/&#123;R&#58;1&#125;</strong><br></div></blockquote></div><blockquote style="margin-left&#58;40px;border&#58;none;">- Redirect type&#58; Found (302)</blockquote>​6. Apply | Back to Rules<div><div><br></div><div></div><div><dt style="border&#58;none;"><img alt="Designing border protection." src="/SiteAssets/do-you-use-url-rewrite-to-redirect-http-to-https/IISURLRewrite.jpg" class="ms-rte-paste-setimagesize" style="margin&#58;5px;padding&#58;15px;border&#58;1px solid #cccccc;width&#58;750px;background&#58;#eeeeee;" />&#160;<br></dt><dd style="padding-left&#58;20px;border&#58;none;line-height&#58;16px;background-attachment&#58;initial;background-size&#58;initial;background-origin&#58;initial;background-clip&#58;initial;background-position&#58;initial;background-repeat&#58;no-repeat;">Figure&#58; HTTP to HTTPS redirect using IIS URL Rewrite module<br>​<br></dd></div></div><p><br></p>


