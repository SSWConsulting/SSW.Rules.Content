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


<p>​​Most developers put the image and the caption in a DIV tag, where the figure is just a paragraph - this is not correct.<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">{ltHTMLChar}div{gtHTMLChar}<br>&#160;&#160;{ltHTMLChar}img alt=&quot;&quot;/{gtHTMLChar}<br>&#160; {ltHTMLChar}p{gtHTMLChar}Figure&#58; Caption{ltHTMLChar}/p{gtHTMLChar}<br>{ltHTMLChar}/div{gtHTMLChar} </p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example​ </dd><p>Instead, you should use 
   <b>{ltHTMLChar}figure{gtHTMLChar}</b> and 
   <b>{ltHTMLChar}figcaption{gtHTMLChar} </b>as per&#160;<a href="https&#58;//www.w3schools.com/TAGS/tag_figcaption.asp">https&#58;//www.w3schools.com/TAGS/tag_figcaption.asp​</a>.&#160;This structure gives semantic&#160;meaning&#160;to&#160;the image and&#160;figure&#58;<br></p><p class="ssw15-rteElement-CodeArea">{ltHTMLChar}figure{gtHTMLChar}<br>&#160;&#160;{ltHTMLChar}img&#160;src=&quot;image.jpg&quot;&#160;alt=&quot;Image&quot; /{gtHTMLChar}<br>&#160;&#160;{ltHTMLChar}figcaption{gtHTMLChar}Figure&#58; Caption{ltHTMLChar}/figcaption{gtHTMLChar}<br>{ltHTMLChar}/figure{gtHTMLChar} </p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example​​​​​​<br></dd><h3 class="ssw15-rteElement-H3">​​The old way​<br></h3><p>For some internal sites, we still use the old way to place images&#58; Using&#160;<b>{ltHTMLChar}dl{gtHTMLChar}</b>,&#160;<b>{ltHTMLChar}dt{gtHTMLChar}</b> (which is the item in the list – in our case an image), and 
   <b>{ltHTMLChar}dd{gtHTMLChar}</b>for a caption. 
   <br></p><p class="ssw15-rteElement-CodeArea">{ltHTMLChar}dl class=&quot;image&quot;{gtHTMLChar} OR {ltHTMLChar}dl class=&quot;badImage&quot;{gtHTMLChar} OR {ltHTMLChar}dl class=&quot;goodImage&quot;{gtHTMLChar} 
   <br>&#160; {ltHTMLChar}dt{gtHTMLChar}{ltHTMLChar}img src=&quot;image.jpg&quot;​ alt=&quot;Image&quot;/{gtHTMLChar}{ltHTMLChar}/dt{gtHTMLChar}<br>&#160; {ltHTMLChar}dd{gtHTMLChar}Figure&#58; Caption{ltHTMLChar}/dd{gtHTMLChar} 
   <br>{ltHTMLChar}/dl{gtHTMLChar}<br></p><dd class="ssw15-rteElement-FigureNormal">​ Figure&#58; Old​ Example​</dd><div><p>
      <b>​Note&#58;</b>&#160;{ltHTMLChar}dl{gtHTMLChar} stands for &quot;<b>definition list</b>&quot;; {ltHTMLChar}dt{gtHTMLChar} for &quot;<b>definition term</b>&quot;; and {ltHTMLChar}dd{gtHTMLChar} for &quot;<b>definition description</b>&quot;.<br></p><h3 class="ssw15-rteElement-H3">​Relate Rule<br></h3><ul><li>
         <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=810b7dab-f94c-4495-bf88-bb80c3bc9776">Figures - Do you add useful and concise figure text?​​​</a><br></li></ul></div>


