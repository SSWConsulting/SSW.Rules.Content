---
type: rule
archivedreason: 
title: Do you avoid using specific characters in friendly URL?
guid: c03c757d-86dc-4f31-9aa3-f1c6670c7d63
uri: avoid-using-specific-characters-in-friendly-url
created: 2017-04-26T20:15:26.0000000Z
authors:
- title: William Yin
  url: https://ssw.com.au/people/william-yin
related: []
redirects:
- do-you-avoid-using-specific-characters-in-friendly-url

---


When adding a friendly URL, please avoid using specific characters like “+, :, #, &, (, ), !, *, [, ], {, }, @, /, =, $” and so on due to multiple reasons:<br>
<br><excerpt class='endintro'></excerpt><br>
<ol><li>When adding a friendly URL, we meant to make it “<strong>friendly</strong>" and “<strong>easy</strong>" for the user to read and remember, so avoid using specific characters and try to make it short.</li><li>Some characters are unsafe characters, they will be encoded, which end up making the URL really messy and ugly, e.g 
      <strong>double quote</strong> (“) will be encoded to 
      <strong>%22</strong>.</li></ol><p>Some characters are reserved characters, which may not be supported by some features, based on our experience, “+" is not supported in “canonical" to redirect from 
   <b>http</b><strong></strong> to 
   <b>https</b>.​​<br></p><dl class="image"><dt><img src="sharepoint-characters-not-allowed.jpg" alt="sharepoint-characters-not-allowed.jpg" /></dt></dl><p>In the above source code, the URL 
   <a href="/do-you-know-when-to-use-+1">http://rules.ssw.com.au:80/do-you-know-when-to-use-+1</a> 
   <em>[note: don't include as a hyperlink as it's a broken URL]</em> will throw a 404 error rather than redirecting to 
   <b>https://rules.ssw.com.au:80/do-you-know-when-to-use-+1</b>,but it works fine if the URL doesn't include “+", e.g. 
   <a href=/do-you-know-when-to-use-plus-one>https://rules.ssw.com.au/do-you-know-when-to-use-plus-one</a>.</p>


