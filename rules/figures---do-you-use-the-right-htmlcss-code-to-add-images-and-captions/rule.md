---
type: rule
archivedreason: 
title: Figures - Do you use the right HTML/CSS code to add images and captions?
guid: f7fc077b-13cc-49e2-a487-06824d5d30af
uri: figures---do-you-use-the-right-htmlcss-code-to-add-images-and-captions
created: 2014-12-04T20:38:45.0000000Z
authors:
- id: 16
  title: Tiago Araujo
- id: 1
  title: Adam Cogan
related: []

---

Most developers put the image and the caption in a DIV tag, where the figure is just a paragraph - this is not correct.

<!--endintro-->

&lt;div&gt;
  &lt;img alt=""/&gt;
  &lt;p&gt;Figure: Caption&lt;/p&gt;
&lt;/div&gt;


::: bad
Figure: Bad Example
:::


Instead, you should use      **&lt;figure&gt;** and      **&lt;figcaption&gt;** as per [https://www.w3schools.com/TAGS/tag\_figcaption.asp](https&#58;//www.w3schools.com/TAGS/tag_figcaption.asp). This structure gives semantic meaning to the image and figure:

&lt;figure&gt;
  &lt;img src="image.jpg" alt="Image" /&gt;
  &lt;figcaption&gt;Figure: Caption&lt;/figcaption&gt;
&lt;/figure&gt;


::: good
Figure: Good Example

:::


### The old way


For some internal sites, we still use the old way to place images: Using  **&lt;dl&gt;** ,  **&lt;dt&gt;** (which is the item in the list – in our case an image), and      **&lt;dd&gt;** for a caption.

&lt;dl class="image"&gt; OR &lt;dl class="badImage"&gt; OR &lt;dl class="goodImage"&gt; 
  &lt;dt&gt;&lt;img src="image.jpg" alt="Image"/&gt;&lt;/dt&gt;
  &lt;dd&gt;Figure: Caption&lt;/dd&gt; 
&lt;/dl&gt;
 **Figure: Good Example
** 

**Note:**  &lt;dl&gt; stands for " **definition list** "; &lt;dt&gt; for " **definition term** "; and &lt;dd&gt; for " **definition description** ".

### Relate Rule


* [Figures - Do you add useful and concise figure text?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=810b7dab-f94c-4495-bf88-bb80c3bc9776)
