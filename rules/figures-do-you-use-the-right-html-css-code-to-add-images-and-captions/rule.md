---
type: rule
archivedreason: 
title: Figures - Do you use the right HTML/CSS code to add images and captions?
guid: f7fc077b-13cc-49e2-a487-06824d5d30af
uri: figures-do-you-use-the-right-html-css-code-to-add-images-and-captions
created: 2014-12-04T20:38:45.0000000Z
authors:
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- use-the-right-html-figure-caption
- figures-do-you-use-the-right-html-css-code-to-add-the-useful-figure-caption

---

Most developers put the image and the caption in a DIV tag, where the figure is just a paragraph - this is not correct.

<!--endintro-->



```
<div>
  <img alt=""/>
  <p>Figure: Caption</p>
</div>
```



::: bad
Figure: Bad Example  
:::

Instead, you should use      **&lt;figure&gt;** and      **&lt;figcaption&gt;** as per [https://www.w3schools.com/TAGS/tag\_figcaption.asp](https&#58;//www.w3schools.com/TAGS/tag_figcaption.asp). This structure gives semantic meaning to the image and figure:



```
<figure>
  <img src="image.jpg" alt="Image" />
  <figcaption>Figure: Caption</figcaption>
</figure>
```



::: good
Figure: Good Example

:::

### The old way


For some internal sites, we still use the old way to place images: Using  **&lt;dl&gt;** ,  **&lt;dt&gt;** (which is the item in the list – in our case an image), and      **&lt;dd&gt;** for a caption.



```
<dl class="image"> OR <dl class="badImage"> OR <dl class="goodImage"> 
  <dt><img src="image.jpg" alt="Image"/></dt>
  <dd>Figure: Caption</dd> 
</dl>
```


 **Figure: Good Example
** 

**Note:**  &lt;dl&gt; stands for " **definition list** "; &lt;dt&gt; for " **definition term** "; and &lt;dd&gt; for " **definition description** ".

### Relate Rule


* [Figures - Do you add useful and concise figure text?](/figures-do-you-add-useful-and-concise-figure-text-aka-a-caption-to-avoid-a-lot-of-text-over-images)
