---
type: rule
title: Figures - Do you use images to reduce the words?
uri: figures---do-you-use-images-to-reduce-the-words
created: 2014-12-04T20:21:31.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 16
  title: Tiago Araujo

---



<span class='intro'> <p>An image is worth a thousand words, it's true. So if you can remove text and replace with an image, do so.</p><p>So we need a better way to present an image on our website and it should be easy enough to create a decent look.</p> </span>

<dl class="badImage"><dt><p class="ssw15-rteElement-GreyBox">You then have this pretty white flower with a green stem standing on a water pond. It is beautiful.</p></dt><dd>Figure&#58; Bad example - Here we have text describing a flower</dd></dl><dl class="goodImage"><dt>
      <img src="/WebSites/RulesToBetterWebsitesLayout/PublishingImages/flower.jpg" alt="flower" />
   </dt><dd>Figure&#58; Good example - Here we have a picture (could be a screen capture) which avoids a thousand words</dd></dl><p>What else can you do?</p><ul><li>Use good captions - See 
      <a href="/WebSites/RulesToBetterWebsitesLayout/Pages/add-useful-caption.aspx">Do you add useful and bold figure text (aka a caption) to avoid a lot of text over images?</a></li><li>Use good HTML - See 
      <a href="#">Do you use the right HTML/CSS code to add the useful figure/caption?</a></li></ul><h3 class="ssw15-rteElement-H3">Technical note for the figure (aka Caption)</h3><p>Most developers (even WordPress) put the image and the caption in a DIV tag. The figure is just a paragraph.</p>
<font class="ms-rteCustom-CodeArea">
   <pre>&lt;div&gt;
&lt;img alt=&quot;&quot;/&gt;
&lt;p&gt;Figure&#58; Caption&lt;/p&gt;
&lt;/div&gt;
</pre> </font><span class="ms-rteCustom-FigureBad">Figure&#58; Bad Example</span><p>Instead, use a figure under the image, using a DL. A DL is a HTML tag that stands for ‘Definition List’. It contains a DT which is the item in the list – in our case an image. A DD (the description of the item). This structure gives the image and the figure, semantic meaning.</p>
<font class="ms-rteCustom-CodeArea">
   <pre>&lt;dl&gt;
&lt;dt&gt;&lt;img alt=&quot;&quot;/&gt;&lt;/dt&gt;
&lt;dd&gt;Figure&#58; Caption&lt;/dd&gt;
&lt;/dl&gt;
</pre> </font><span class="ms-rteCustom-FigureGood">Figure&#58; Good Example​</span> ​


