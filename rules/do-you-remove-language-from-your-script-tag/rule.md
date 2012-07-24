---
type: rule
title: Do you remove "Language" from your script tag?
uri: do-you-remove-language-from-your-script-tag
created: 2012-07-24T18:10:04.0000000Z
authors:
- id: 16
  title: Tiago Araujo

---



<span class='intro'> <p>A few years ago, it was common to have the &quot;language&quot; attribute within the script tags. This attribute was used to specify the scripting language of the contents of this element.</p> </span>

<p>Since these identifiers are not standard, this attribute has been deprecated in favor of &quot;type&quot;.</p>

<div class="ms-rteCustom-CodeArea">
<p>&lt;script href=&quot;script.js&quot; language=&quot;javascript&quot;&gt;&lt;/script&gt;</p>
</div>
<span class="ms-rteCustom-FigureBad">Figure&#58; Language attribute has been deprecated</span>

<div class="ms-rteCustom-CodeArea">
<p>&lt;script href=&quot;script.js&quot; type=&quot;text/javascript&quot;&gt;&lt;/script&gt;</p>
</div>
<span class="ms-rteCustom-FigureGood">Figure&#58; The scripting language is specified as a content type</span>

<p>Read more on <a target="_blank" href="http&#58;//www.w3.org/TR/html4/interact/scripts.html#h-18.2.2">W3C website</a>.</p>


