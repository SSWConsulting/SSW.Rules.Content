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
{ltHTMLChar}div{gtHTMLChar}   <br>
{ltHTMLChar}p{gtHTMLChar}Hello HTML{ltHTMLChar}/p{gtHTMLChar}   <br>
{ltHTMLChar}/div{gtHTMLChar}
<br>
</font><span class="ms-rteCustom-FigureGood">Figure&#58; Good Example</span>
<div><br>
<font class="ms-rteCustom-GreyBox">
{ltHTMLChar}breakfast_menu{gtHTMLChar}
<br>
{ltHTMLChar}food{gtHTMLChar}
<br>
{ltHTMLChar}name{gtHTMLChar}Homestyle Breakfast{ltHTMLChar}/name{gtHTMLChar}
<br>
{ltHTMLChar}price{gtHTMLChar}$6.95{ltHTMLChar}/price{gtHTMLChar}
<br>
{ltHTMLChar}description{gtHTMLChar}two eggs{ltHTMLChar}/description{gtHTMLChar}
<br>
{ltHTMLChar}calories{gtHTMLChar}950{ltHTMLChar}/calories{gtHTMLChar}
<br>
{ltHTMLChar}/food{gtHTMLChar}<br>
{ltHTMLChar}/breakfast_menu{gtHTMLChar}
</font><span class="ms-rteCustom-FigureGood">Figure&#58; Good Example</span>
<br>
<font class="ms-rteCustom-GreyBox">
{ltHTMLChar}div{gtHTMLChar}   <br>
{ltHTMLChar}p{gtHTMLChar}Hello&#160;HTML&#160;&#160;<br>
{ltHTMLChar}/div{gtHTMLChar}
<br>
</font>
<span class="ms-rteCustom-FigureBad">Figure&#58; Bad Example</span><br>
<font class="ms-rteCustom-GreyBox">
{ltHTMLChar}breakfast_menu{gtHTMLChar}
<br>
{ltHTMLChar}food{gtHTMLChar}
<br>
{ltHTMLChar}name{gtHTMLChar}Homestyle Breakfast
<br>
{ltHTMLChar}price{gtHTMLChar}$6.95
<br>
{ltHTMLChar}description{gtHTMLChar}two eggs
<br>
{ltHTMLChar}calories{gtHTMLChar}950
<br>
{ltHTMLChar}/food{gtHTMLChar}<br>
{ltHTMLChar}/breakfast_menu{gtHTMLChar}
</font><span class="ms-rteCustom-FigureBad">Figure&#58; Bad Example</span>
<br>
</div>



