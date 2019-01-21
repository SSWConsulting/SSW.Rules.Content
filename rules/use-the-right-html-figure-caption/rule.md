---
type: rule
archivedreason: 
title: Figures - Do you use the right HTML/CSS code to add images and captions?
guid: f7fc077b-13cc-49e2-a487-06824d5d30af
uri: use-the-right-html-figure-caption
created: 2014-12-04T20:38:45.0000000Z
authors:
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- figures-do-you-use-the-right-html-css-code-to-add-the-useful-figure-caption
- figures-do-you-use-the-right-html-css-code-to-add-images-and-captions

---


<p>​​Most developers put the image and the caption in a DIV tag. The figure is just a paragraph.​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<font class="ms-rteCustom-CodeArea"> <pre>{ltHTMLChar}div{gtHTMLChar}
{ltHTMLChar}img alt=&quot;&quot;/{gtHTMLChar}
{ltHTMLChar}p{gtHTMLChar}Figure&#58; Caption{ltHTMLChar}/p{gtHTMLChar}
{ltHTMLChar}/div{gtHTMLChar}
</pre> </font> <span class="ms-rteCustom-FigureBad">Figure&#58; Bad Example</span> 
<p>Instead, you should use {ltHTMLChar}DL{gtHTMLChar},&#160;{ltHTMLChar}DT{gtHTMLChar} (which is the item in the list – in our case an image) and {ltHTMLChar}DD{gtHTMLChar}for a caption. This structure gives semantic<span style="line-height&#58;20.8px;"> meaning</span> to&#160;the image and&#160;figure. <br></p>
<font class="ms-rteCustom-CodeArea"> <pre>{ltHTMLChar}dl class=&quot;image&quot;{gtHTMLChar} OR {ltHTMLChar}dl class=&quot;badImage&quot;{gtHTMLChar} OR {ltHTMLChar}dl class=&quot;goodImage&quot;{gtHTMLChar}
{ltHTMLChar}dt{gtHTMLChar}{ltHTMLChar}img alt=&quot;&quot;/{gtHTMLChar}{ltHTMLChar}/dt{gtHTMLChar}
{ltHTMLChar}dd{gtHTMLChar}Figure&#58; Caption{ltHTMLChar}/dd{gtHTMLChar}
{ltHTMLChar}/dl{gtHTMLChar}
</pre> </font> <span class="ms-rteCustom-FigureGood">Figure&#58; Good Example </span> 
<p><b>Note&#58;</b>&#160;{ltHTMLChar}dl{gtHTMLChar} stands for &quot;<b>definition list</b>&quot;; {ltHTMLChar}dt{gtHTMLChar} for &quot;<b>definition term</b>&quot;; and {ltHTMLChar}dd{gtHTMLChar} for &quot;<b>definition description</b>&quot;.</p>​<br>


