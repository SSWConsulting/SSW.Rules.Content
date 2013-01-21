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


<p>The attribute &quot;name&quot; allows you to link to specific places within the page, via the {ltHTMLChar}a{gtHTMLChar} tag.</p><p>This is especially useful in long pages that can be separated into sections. You can create a named anchor in each of these section headings to provide &quot;jump-to&quot; functionality. In other words, you can have a different URL for each piece of content on the same page.</p>
<br><excerpt class='endintro'></excerpt><br>
<span class="ms-rteCustom-CodeArea"> {ltHTMLChar}h2{gtHTMLChar}{ltHTMLChar}a name=&quot;get-started&quot;{gtHTMLChar}{ltHTMLChar}/a{gtHTMLChar}Get Started{ltHTMLChar}/h2{gtHTMLChar} </span> 
<span class="ms-rteCustom-FigureNormal">Figure&#58; Good example - This is how you add an anchor name to an specific section of your page. Note it doesn't have the hash mark</span> 
<p>To create a link to that section, simply add a hash mark to the end of the URL followed by the name you chose&#58;</p> 
<span class="ms-rteCustom-CodeArea"> {ltHTMLChar}a href=&quot;#get-started&quot;{gtHTMLChar}Go to Get Started section{ltHTMLChar}/a{gtHTMLChar} </span> 
<span class="ms-rteCustom-FigureNormal">Figure&#58; Good example - This is how you add a *link* to that anchor name you created. Remember to add the hash mark</span> 
<div class="ms-rteCustom-GreyBox"><p>
      <strong>Tip #1&#58;</strong> Use the hash mark <strong>only</strong> to go to the top of a page.&#160;<br>E.g. {ltHTMLChar}a href=&quot;#&quot;{gtHTMLChar}&amp;Go to top{ltHTMLChar}/a{gtHTMLChar}</p></div><div class="ms-rteCustom-GreyBox"><p>
      <strong>Tip #2&#58;</strong> Some browsers consider capitalization for anchor names (E.g. Firefox). Always check your links and anchor names are identical, matching the capitalization.</p></div> 


