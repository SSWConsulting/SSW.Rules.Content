---
type: rule
archivedreason: 
title: Do you know how to use named anchor links?
guid: 599548c1-a1ff-4f0a-aed8-5938acb6fe83
uri: do-you-know-how-to-use-named-anchor-links
created: 2012-07-17T20:11:55.0000000Z
authors:
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects: []

---


<p>The attribute &quot;name&quot; allow you to link to specific places within the page via {ltHTMLChar}a{gtHTMLChar} tag.</p>
<p>Suppose you have a long page with different sections. You can create a named anchor in each of these section headings to provide a &quot;jump-to&quot; functionality. In other words, you can have a different URL for each piece of content on the same page.</p>

<br><excerpt class='endintro'></excerpt><br>
<p>To do so you should create a empty link tag with the attribute name you prefer&#58;</p>
<span class="ms-rteCustom-CodeArea">
{ltHTMLChar}h2{gtHTMLChar}{ltHTMLChar}a name=&quot;get-started&quot;{gtHTMLChar}{ltHTMLChar}/a{gtHTMLChar}Get Started{ltHTMLChar}/h2{gtHTMLChar}
</span>
<span class="ms-rteCustom-FigureNormal">Figure&#58; Code for a named anchor link. Note it doesn't have the hash mark </span>
<p>To create a link to that section, simply add a hash mark to the end of the URL followed by the name you chose&#58;</p>
<span class="ms-rteCustom-CodeArea">
{ltHTMLChar}a href=&quot;#get-started&quot;{gtHTMLChar}Go to Get Started section{ltHTMLChar}/a{gtHTMLChar}
</span>
<span class="ms-rteCustom-FigureNormal">Figure&#58; Code to link to a named section of a page. Remember to add the hash mark</span>
<div class="ms-rteCustom-GreyBox">
<p><strong>Tip&#58;</strong> Use the hash mark only to go to the top of a page.&#160;<br>E.g. {ltHTMLChar}a href=&quot;#&quot;{gtHTMLChar}&amp;Go to top{ltHTMLChar}/a{gtHTMLChar}</p>
</div>
<div class="ms-rteCustom-GreyBox">
<p><strong>Tip 2&#58;</strong> Some browsers consider capitalization for anchor names. Always check you have your link and anchor name identical</p>
</div>



