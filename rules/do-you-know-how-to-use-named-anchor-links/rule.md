---
type: rule
title: Do you know how to use named anchor links?
uri: do-you-know-how-to-use-named-anchor-links
created: 2012-07-17T20:11:55.0000000Z
authors:
- id: 16
  title: Tiago Araujo

---



<span class='intro'> <p>The attribute &quot;name&quot; allow you to link to specific places within the page via &lt;a&gt; tag.</p>
<p>Suppose you have a long page with different sections. You can create a named anchor in each of these section headings to provide a &quot;jump-to&quot; functionality. In other words, you can have a different URL for each piece of content on the same page.</p>
 </span>

<p>To do so you should create a empty link tag with the attribute name you prefer&#58;</p>
<span class="ms-rteCustom-CodeArea">
&lt;h2&gt;&lt;a name=&quot;get-started&quot;&gt;&lt;/a&gt;Get Started&lt;/h2&gt;
</span>
<span class="ms-rteCustom-FigureNormal">Figure&#58; Code for a named anchor link. Note it doesn't have the hash mark </span>
<p>To create a link to that section, simply add a hash mark to the end of the URL followed by the name you chose&#58;</p>
<span class="ms-rteCustom-CodeArea">
&lt;a href=&quot;#get-started&quot;&gt;Go to Get Started section&lt;/a&gt;
</span>
<span class="ms-rteCustom-FigureNormal">Figure&#58; Code to link to a named section of a page. Remember to add the hash mark</span>
<div class="ms-rteCustom-GreyBox">
<p><strong>Tip&#58;</strong> Use the hash mark only to go to the top of a page.&#160;<br>E.g. &lt;a href=&quot;#&quot;&gt;&amp;Go to top&lt;/a&gt;</p>
</div>
<div class="ms-rteCustom-GreyBox">
<p><strong>Tip 2&#58;</strong> Some browsers consider capitalization for anchor names. Always check you have your link and anchor name identical</p>
</div>



