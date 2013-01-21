---
type: rule
title: Do you know how to use named anchor links?
uri: do-you-know-how-to-use-named-anchor-links
created: 2012-07-17T20:11:55.0000000Z
authors:
- id: 16
  title: Tiago Araujo

---



<span class='intro'> <p>The attribute &quot;name&quot; allows you to link to specific places within the page, via the &lt;a&gt; tag.</p><p>This is especially useful in long pages that can be separated into sections. You can create a named anchor in each of these section headings to provide &quot;jump-to&quot; functionality. In other words, you can have a different URL for each piece of content on the same page.</p> </span>

<span class="ms-rteCustom-CodeArea"> &lt;h2&gt;&lt;a name=&quot;get-started&quot;&gt;&lt;/a&gt;Get Started&lt;/h2&gt; </span><span class="ms-rteCustom-FigureNormal">Figure&#58; This is how you add an anchor name to an specific section of your page. Note it doesn't have the hash mark and the anchor tag is empty</span>
<p>To create a link to that section, simply add a hash mark to the end of the URL followed by the name you chose&#58;</p>
<span class="ms-rteCustom-CodeArea"> &lt;a href=&quot;#get-started&quot;&gt;Go to Get Started section&lt;/a&gt; </span><span class="ms-rteCustom-FigureNormal">Figure&#58; This is how you add a *link* to that anchor name you created. Remember to add the hash mark</span>
<div class="ms-rteCustom-GreyBox"><p> 
      <strong>Tip #1&#58;</strong> Use the hash mark 
      <strong>only</strong> to go to the top of a page.&#160;<br>E.g. &lt;a href=&quot;#&quot;&gt;&amp;Go to top&lt;/a&gt;</p></div><div class="ms-rteCustom-GreyBox"><p> 
      <strong>Tip #2&#58;</strong> Some browsers consider capitalization for anchor names (E.g. Firefox). Always check your links and anchor names are identical, matching the capitalization.</p></div>


