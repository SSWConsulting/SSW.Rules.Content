---
seoDescription: Well-formed HTML/XML tags are essential for proper document structure and rendering. Tags that open must be properly closed to ensure correct parsing and display
type: rule
archivedreason:
title: Do you make sure that all your tags are well formed ?
guid: 3673083a-7145-4441-918d-5d3d9419506c
uri: do-you-make-sure-that-all-your-tags-are-well-formed
created: 2011-04-28T09:29:10.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
---

Do you know how to form HTML/XML tags on webpages?
We need to make sure that all HTML/XML tags which open once, must be closed properly.

<!--endintro-->

::: greybox
&lt;div&gt;  
 &lt;p&gt;Hello HTML&lt;/p&gt;  
 &lt;/div&gt;

:::
Figure: Good Example

::: greybox
&lt;breakfast_menu&gt;

&lt;food&gt;

&lt;name&gt;Homestyle Breakfast&lt;/name&gt;

&lt;price&gt;$6.95&lt;/price&gt;

&lt;description&gt;two eggs&lt;/description&gt;

&lt;calories&gt;950&lt;/calories&gt;

&lt;/food&gt;

&lt;/breakfast_menu&gt;  
:::
Figure: Good Example

::: greybox
&lt;div&gt;

&lt;p&gt;Hello HTML

&lt;/div&gt;

:::
Figure: Bad Example

::: greybox
&lt;breakfast_menu&gt;

&lt;food&gt;

&lt;name&gt;Homestyle Breakfast

&lt;price&gt;$6.95

&lt;description&gt;two eggs

&lt;calories&gt;950

&lt;/food&gt;

&lt;/breakfast_menu&gt;  
:::
Figure: Bad Example
