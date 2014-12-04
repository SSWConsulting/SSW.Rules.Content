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


<span style="line-height&#58;1.6;">Most developers (even WordPress) put the image and the caption in a DIV tag. The figure is just a paragraph.</span>
<br><excerpt class='endintro'></excerpt><br>
<font class="ms-rteCustom-CodeArea"> 
   <pre>{ltHTMLChar}div{gtHTMLChar}
{ltHTMLChar}img alt=&quot;&quot;/{gtHTMLChar}
{ltHTMLChar}p{gtHTMLChar}Figure&#58; Caption{ltHTMLChar}/p{gtHTMLChar}
{ltHTMLChar}/div{gtHTMLChar}
</pre> </font>
<span class="ms-rteCustom-FigureBad">Figure&#58; Bad Example</span>
<p>Instead, use a figure under the image, using a DL. A DL is a HTML tag that stands for ‘Definition List’. It contains a DT which is the item in the list – in our case an image. A DD (the description of the item). This structure gives the image and the figure, semantic meaning.</p> 
<font class="ms-rteCustom-CodeArea"> 
   <pre>{ltHTMLChar}dl{gtHTMLChar}
{ltHTMLChar}dt{gtHTMLChar}{ltHTMLChar}img alt=&quot;&quot;/{gtHTMLChar}{ltHTMLChar}/dt{gtHTMLChar}
{ltHTMLChar}dd{gtHTMLChar}Figure&#58; Caption{ltHTMLChar}/dd{gtHTMLChar}
{ltHTMLChar}/dl{gtHTMLChar}
</pre> </font>
<span class="ms-rteCustom-FigureGood">Figure&#58; Good Example​</span> ​​


