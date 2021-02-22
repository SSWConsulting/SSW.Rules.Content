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


Do you know how to form HTML/XML tags on webpages?<br>
We need to make sure that all HTML/XML tags which open once, must be closed properly.

<br><excerpt class='endintro'></excerpt><br>
  <br>
<font class="ms-rteCustom-GreyBox">
&lt;div&gt;   <br>
&lt;p&gt;Hello HTML&lt;/p&gt;   <br>
&lt;/div&gt;
<br>
</font><span class="ms-rteCustom-FigureGood">Figure&#58; Good Example</span>
<div><br>
<font class="ms-rteCustom-GreyBox">
&lt;breakfast_menu&gt;
<br>
&lt;food&gt;
<br>
&lt;name&gt;Homestyle Breakfast&lt;/name&gt;
<br>
&lt;price&gt;$6.95&lt;/price&gt;
<br>
&lt;description&gt;two eggs&lt;/description&gt;
<br>
&lt;calories&gt;950&lt;/calories&gt;
<br>
&lt;/food&gt;<br>
&lt;/breakfast_menu&gt;
</font><span class="ms-rteCustom-FigureGood">Figure&#58; Good Example</span>
<br>
<font class="ms-rteCustom-GreyBox">
&lt;div&gt;   <br>
&lt;p&gt;Hello&#160;HTML&#160;&#160;<br>
&lt;/div&gt;
<br>
</font>
<span class="ms-rteCustom-FigureBad">Figure&#58; Bad Example</span><br>
<font class="ms-rteCustom-GreyBox">
&lt;breakfast_menu&gt;
<br>
&lt;food&gt;
<br>
&lt;name&gt;Homestyle Breakfast
<br>
&lt;price&gt;$6.95
<br>
&lt;description&gt;two eggs
<br>
&lt;calories&gt;950
<br>
&lt;/food&gt;<br>
&lt;/breakfast_menu&gt;
</font><span class="ms-rteCustom-FigureBad">Figure&#58; Bad Example</span>
<br>
</div>



