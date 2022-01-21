---
type: rule
archivedreason: 
title: Do you avoid having width and height properties in image tags?
guid: 3795e298-c889-49e5-b9b1-58dac3d8eaae
uri: do-you-exclude-width-and-height-properties-from-image-references-in-content
created: 2015-10-13T00:44:07.0000000Z
authors: 
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related: []
redirects: []

---

Specifying the width and height properties for images on your web pages can sometimes turn out to be more trouble than it's worth, particularly if the image is updated with different dimensions. Adding fixed widths to your images also disrupt your content on any responsive websites.

<!--endintro-->

In other words, you **should not** have the image dimensions specified in HTML unless you have a very specific reason to do so. Use CSS if you need to specify images dimensions.

```
<img src="MyPic.gif" width="93" height="25">
```
::: bad
Figure: Bad Example - Including the width and height properties for content images
:::

```
<img src="MyPic.gif">
```
::: good
Figure: Good Example - Exclude width and height properties for content images
:::
