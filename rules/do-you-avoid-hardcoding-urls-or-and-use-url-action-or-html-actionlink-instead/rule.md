---
type: rule
archivedreason: 
title: Do you avoid hardcoding URLs (“../”, “~/”, or “/”) and use Url.Action or Html.ActionLink instead?
guid: 582c7a84-24ff-40ca-b1ff-332ec3a191a2
uri: do-you-avoid-hardcoding-urls-or-and-use-url-action-or-html-actionlink-instead
created: 2013-03-07T18:51:39.0000000Z
authors:
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related: []
redirects:
- do-you-avoid-hardcoding-urls-(-or-)-and-use-url-action-or-html-actionlink-instead

---


<p>Hardcoding URLs in your View can cause problems if your routes or page names need to change.  Instead, you should always use the Url and Html helpers to refer to different pages in your MVC application.</p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt><div class="greyBox"><pre>&lt;a href=&quot;/Rule/Create&quot;&gt;Create a Rule&lt;/a&gt;
</pre></div></dt><dd>Figure&#58; Bad Example – Hard-coded URLs may lead to broken links if routes change</dd></dl><dl class="goodImage"><dt><div class="greyBox"><pre>@Html.ActionLink(&quot;Create a Rule&quot;, &quot;Create&quot;, &quot;Rule&quot;)
</pre></div></dt><dd>Figure&#58; Good Example – Use the Url or Html helpers to provide links</dd></dl>


