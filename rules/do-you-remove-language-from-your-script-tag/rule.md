---
type: rule
archivedreason: 
title: Do you remove "Language" from your script tag?
guid: a5f42e3c-b24e-43de-8021-a85e9fed0656
uri: do-you-remove-language-from-your-script-tag
created: 2012-07-24T18:10:04.0000000Z
authors:
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects:
- do-you-remove-＂language＂-from-your-script-tag

---


<p>A few years ago, it was common to have the &quot;language&quot; attribute within the script tags. This attribute was used to specify the scripting language of the contents of this element.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>Since these identifiers are not standard, this attribute has been deprecated in favor of &quot;type&quot;.</p>

<div class="ms-rteCustom-CodeArea">
<p>&lt;script href=&quot;script.js&quot; language=&quot;javascript&quot;&gt;&lt;/script&gt;</p>
</div>
<span class="ms-rteCustom-FigureBad">Figure&#58; Language attribute has been deprecated</span>

<div class="ms-rteCustom-CodeArea">
<p>&lt;script href=&quot;script.js&quot; type=&quot;text/javascript&quot;&gt;&lt;/script&gt;</p>
</div>
<span class="ms-rteCustom-FigureGood">Figure&#58; The scripting language is specified as a content type</span>

<p>Read more on <a href="http&#58;//www.w3.org/TR/html4/interact/scripts.html#h-18.2.2" target="_blank">W3C website</a>.</p>


