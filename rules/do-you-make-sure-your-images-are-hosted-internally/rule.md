---
type: rule
archivedreason: 
title: Do you make sure your images are hosted internally?
guid: 72bf9d1b-9ca5-4333-9e16-9adbc1dc6904
uri: do-you-make-sure-your-images-are-hosted-internally
created: 2017-01-24T13:26:09.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 16
  title: Tiago Araujo
related: []

---

When want to show an image from the web on your website, the easiest way is to just copy the image's path and add it. This is not a good idea as the original host of the image can delete it, which will cause a broken image in your website.

<!--endintro-->

The right way to do this is to copy the image locally and upload to your own server, so you have total control over the image.

&lt;dl class="image"&gt;
&lt;dt&gt;&lt;img src="<mark>https&#58;//some-external-url.com</mark>/images/open-extension.png" alt="Open extension" /&gt;&lt;/dt&gt; 
&lt;dd&gt;Figure: Open extension&lt;/dd&gt;
&lt;/dl&gt;


::: bad
Figure: Bad example - using an external URL as image source. The image can be edited or deleted and there is nothing you can do about it

:::


&lt;dl class="image"&gt;
&lt;dt&gt;&lt;img src="<mark>https&#58;//ssw.com.au</mark>/images/open-extension.png" alt="Open extension" /&gt;&lt;/dt&gt; 
&lt;dd&gt;Figure: Open extension&lt;/dd&gt;
&lt;/dl&gt;


::: good
Figure: Good example - Image is hosted internally. You have control over the image

:::


**Note:**  For copyrighted images, it is important to always mention the source.
