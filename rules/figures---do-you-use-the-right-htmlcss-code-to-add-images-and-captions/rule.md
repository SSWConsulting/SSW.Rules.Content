---
type: rule
title: Figures - Do you use the right HTML/CSS code to add images and captions?
uri: figures---do-you-use-the-right-htmlcss-code-to-add-images-and-captions
created: 2014-12-04T20:38:45.0000000Z
authors:
- id: 16
  title: Tiago Araujo
- id: 1
  title: Adam Cogan

---



<span class='intro'> <span style="line-height&#58;1.6;">Most developers (even WordPress) put the image and the caption in a DIV tag. The figure is just a paragraph.</span> </span>

<font class="ms-rteCustom-CodeArea"> 
   <pre>&lt;div&gt;
&lt;img alt=&quot;&quot;/&gt;
&lt;p&gt;Figure&#58; Caption&lt;/p&gt;
&lt;/div&gt;
</pre> </font>
<span class="ms-rteCustom-FigureBad">Figure&#58; Bad Example</span>
<p>Instead, use a figure under the image, using a DL. A DL is a HTML tag that stands for ‘Definition List’. It contains a DT which is the item in the list – in our case an image. A DD (the description of the item). This structure gives the image and the figure, semantic meaning.</p> 
<font class="ms-rteCustom-CodeArea"> 
   <pre>&lt;dl&gt;
&lt;dt&gt;&lt;img alt=&quot;&quot;/&gt;&lt;/dt&gt;
&lt;dd&gt;Figure&#58; Caption&lt;/dd&gt;
&lt;/dl&gt;
</pre> </font>
<span class="ms-rteCustom-FigureGood">Figure&#58; Good Example​</span> ​​


