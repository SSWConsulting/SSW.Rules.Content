---
type: rule
title: Do you make sure your images are hosted internally?
uri: do-you-make-sure-your-images-are-hosted-internally
created: 2017-01-24T13:26:09.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 16
  title: Tiago Araujo

---



<span class='intro'> When want to show an image from the web on your website, the easiest way is to just copy the image's path and add it. This is not a good idea as the original host of the image can delete it, which will cause a broken image in your website.<br> </span>

<p>The right way to do this is to copy the image locally and upload to your own server, so you have total control over the image.<br></p><p class="ssw15-rteElement-CodeArea">&lt;dl class=&quot;image&quot;&gt;<br>&lt;dt&gt;&lt;img src=&quot;<span class="ssw15-rteStyle-Highlight">https&#58;//some-external-​url.com</span>/images/open-extension.png&quot; alt=&quot;Open extension&quot; /&gt;&lt;/dt&gt;&#160;<br>&lt;dd&gt;Figure&#58; Open extension&lt;/dd&gt;<br>&lt;/dl&gt;<br></p><dd class="ssw15-rteElement-FigureBad">​Figure&#58; Bad example - using an external URL as image source. The image can be edited or deleted and there is nothing you can do about it<br></dd><p class="ssw15-rteElement-CodeArea">​&lt;dl class=&quot;image&quot;&gt;<br>&lt;dt&gt;&lt;img src=&quot;<span class="ssw15-rteStyle-Highlight">https&#58;//ssw.com.au​</span>/images/open-extension.png&quot; alt=&quot;Open extension&quot; /&gt;&lt;/dt&gt;&#160;<br>&lt;dd&gt;Figure&#58; Open extension&lt;/dd&gt;<br>&lt;/dl&gt;​<br></p><dd class="ssw15-rteElement-FigureGood">​Figure&#58; Good example - Image is hosted internally. You have control over the image<br></dd><p class="ssw15-rteElement-P"><b>Note&#58;</b>&#160;For copyrighted images, it is important to always ​​mention the source.​​<br></p>


