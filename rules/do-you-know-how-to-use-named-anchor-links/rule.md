---
type: rule
archivedreason: 
title: Do you know how to use named anchor links?
guid: 599548c1-a1ff-4f0a-aed8-5938acb6fe83
uri: do-you-know-how-to-use-named-anchor-links
created: 2012-07-17T20:11:55.0000000Z
authors:
- title: Tiago Araujo
  url: /people/tiago-araujo
related: []
redirects: []

---

The attribute "name" allows you to link to specific places within the page, via the &lt;a&gt; tag.

This is especially useful in long pages that can be separated into sections. You can create a named anchor in each of these section headings to provide "jump-to" functionality. In other words, you can have a different URL for each piece of content on the same page.

<!--endintro-->
 &lt;h2&gt;&lt;a name="get-started"&gt;&lt;/a&gt;Get Started&lt;/h2&gt; **Figure: This is how you add an anchor name to an specific section of your page. Note it doesn't have the hash mark and the anchor tag is empty** 
You now have a custom URL that points to the specific section of the page. It is the page URL followed by the hash mark and the name you chose:
 http://www.yourpage.com#get-started **Figure: This is how your custom URL will look like** 
You can use this new URL to point users to that specific section of your page.

To create a link to your anchor named section inside the same page, simply add a new "href" anchor tag - now with a hash mark followed by the name you chose:
 &lt;a href="#get-started"&gt;Go to Get Started section&lt;/a&gt; **Figure: This is how you add a \*link\* to that anchor name you created inside the same page. Remember to add the hash mark** 

::: greybox

**Tip #1:** Use the hash mark         **only** to go to the top of a page. 
E.g. &lt;a href="#"&gt;&Go to top&lt;/a&gt;

:::


::: greybox

**Tip #2:** Some browsers consider capitalization for anchor names (E.g. Firefox). Always check your links and anchor names are identical, matching the capitalization.

:::
