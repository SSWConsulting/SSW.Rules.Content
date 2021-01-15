---
type: rule
archivedreason: 
title: Do you use DOCTYPE without any reference?
guid: fce75b30-c3a2-49b7-b80a-5dd74480325e
uri: do-you-use-doctype-without-any-reference
created: 2014-12-15T17:59:16.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects: []

---

Since HTML5, DOCTYPE no longer requires a reference to a DTD. Back in HTML 4.01, The DTD links were used in to specify the rules for the markup language (Transitional, Strict, Frameset etc) so that the browsers render the content correctly. It’s no longer necessary. 
<!--endintro-->

::: greybox
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "[http://www.w3.org/TR/html4/strict.dtd](http&#58;//www.w3.org/TR/html4/strict.dtd)"&gt;  
:::

::: bad
Figure: Bad Example – XXX  
:::

::: greybox
&lt;!DOCTYPE html&gt;  
:::

::: good
Figure: Good Example – XXX  
:::

For more information, go to 
      [HTML !DOCTYPE Declaration on w3schools.com](http&#58;//www.w3schools.com/tags/tag_doctype.asp)
