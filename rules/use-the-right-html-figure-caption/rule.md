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
<p class="ssw15-rteElement-CodeArea">&lt;div&gt;<br>&#160;&#160;&lt;img alt=&quot;&quot;/&gt;<br>&#160; &lt;p&gt;Figure&#58; Caption&lt;/p&gt;<br>&lt;/div&gt; </p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example​ </dd><p>Instead, you should use 
   <b>&lt;figure&gt;</b> and 
   <b>&lt;figcaption&gt; </b>as per&#160;<a href="https&#58;//www.w3schools.com/TAGS/tag_figcaption.asp">https&#58;//www.w3schools.com/TAGS/tag_figcaption.asp​</a>.&#160;This structure gives semantic&#160;meaning&#160;to&#160;the image and&#160;figure&#58;<br></p><p class="ssw15-rteElement-CodeArea">&lt;figure&gt;<br>&#160;&#160;&lt;img&#160;src=&quot;image.jpg&quot;&#160;alt=&quot;Image&quot; /&gt;<br>&#160;&#160;&lt;figcaption&gt;Figure&#58; Caption&lt;/figcaption&gt;<br>&lt;/figure&gt; </p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example​​​​​​<br></dd><h3 class="ssw15-rteElement-H3">​​The old way​<br></h3><p>For some internal sites, we still use the old way to place images&#58; Using&#160;<b>&lt;dl&gt;</b>,&#160;<b>&lt;dt&gt;</b> (which is the item in the list – in our case an image), and 
   <b>&lt;dd&gt;</b>for a caption. 
   <br></p><p class="ssw15-rteElement-CodeArea">&lt;dl class=&quot;image&quot;&gt; OR &lt;dl class=&quot;badImage&quot;&gt; OR &lt;dl class=&quot;goodImage&quot;&gt; 
   <br>&#160; &lt;dt&gt;&lt;img src=&quot;image.jpg&quot;​ alt=&quot;Image&quot;/&gt;&lt;/dt&gt;<br>&#160; &lt;dd&gt;Figure&#58; Caption&lt;/dd&gt; 
   <br>&lt;/dl&gt;<br></p><dd class="ssw15-rteElement-FigureNormal">​ Figure&#58; Old​ Example​</dd><div><p>
      <b>​Note&#58;</b>&#160;&lt;dl&gt; stands for &quot;<b>definition list</b>&quot;; &lt;dt&gt; for &quot;<b>definition term</b>&quot;; and &lt;dd&gt; for &quot;<b>definition description</b>&quot;.<br></p><h3 class="ssw15-rteElement-H3">​Relate Rule<br></h3><ul><li>
         <a href=/figures-do-you-add-useful-and-concise-figure-text-aka-a-caption-to-avoid-a-lot-of-text-over-images>Figures - Do you add useful and concise figure text?​​​</a><br></li></ul></div>


