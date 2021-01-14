---
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
&lt;breakfast\_menu&gt;<br>
<br>&lt;food&gt;<br>
<br>&lt;name&gt;Homestyle Breakfast&lt;/name&gt;<br>
<br>&lt;price&gt;$6.95&lt;/price&gt;<br>
<br>&lt;description&gt;two eggs&lt;/description&gt;<br>
<br>&lt;calories&gt;950&lt;/calories&gt;<br>
<br>&lt;/food&gt;
<br>&lt;/breakfast\_menu&gt;  
:::
Figure: Good Example

::: greybox
&lt;div&gt;   
<br>&lt;p&gt;Hello HTML  
<br>&lt;/div&gt;<br>

:::
Figure: Bad Example

::: greybox
&lt;breakfast\_menu&gt;<br>
<br>&lt;food&gt;<br>
<br>&lt;name&gt;Homestyle Breakfast<br>
<br>&lt;price&gt;$6.95<br>
<br>&lt;description&gt;two eggs<br>
<br>&lt;calories&gt;950<br>
<br>&lt;/food&gt;
<br>&lt;/breakfast\_menu&gt;  
:::
Figure: Bad Example
