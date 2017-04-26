---
type: rule
title: Do you avoid using specific characters in friendly URL?
uri: do-you-avoid-using-specific-characters-in-friendly-url
created: 2017-04-26T20:15:26.0000000Z
authors:
- id: 9
  title: William Yin

---



<span class='intro'> When adding a friendly URL, please avoid using specific characters like “+, &#58;, #, &amp;, (, ), !, *, [, ], &#123;, &#125;, @, /, =, $” and so on due to multiple reasons&#58;<br> </span>

<ol><li>When adding a friendly URL, we meant to make it “<strong>friendly</strong>&quot; and “<strong>easy</strong>&quot; for the user to read and remember, so avoid using specific characters and try to make it short.</li><li>Some characters are unsafe characters, they will be encoded, which end up making the URL really messy and ugly, e.g 
      <strong>double quote</strong> (“) will be encoded to 
      <strong>%22</strong>.</li></ol><p>Some characters are reserved characters, which may not be supported by some features, based on our experience, “+&quot; is not supported in “canonical&quot; to redirect from 
   <b>http</b><strong></strong> to 
   <b>https</b>.​​<br></p><dl class="image"><dt><img src="/PublishingImages/sharepoint-characters-not-allowed.jpg" alt="sharepoint-characters-not-allowed.jpg" /></dt></dl><p>In the above source code, the URL 
   <a href="/do-you-know-when-to-use-+1">http&#58;//rules.ssw.com.au&#58;80/do-you-know-when-to-use-+1</a> 
   <em>[note&#58; don't include as a hyperlink as it's a broken URL]</em> will throw a 404 error rather than redirecting to 
   <b>https&#58;//rules.ssw.com.au&#58;80/do-you-know-when-to-use-+1</b>,but it works fine if the URL doesn't include “+&quot;, e.g. 
   <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=d1f2a285-1ca6-45d6-8142-30bccb09c528">https&#58;//rules.ssw.com.au/do-you-know-when-to-use-plus-one</a>.</p>


