---
type: rule
archivedreason: 
title: Do you avoid having height/width in an image tag?
guid: 7b56ba87-23be-47a8-a534-f86990c45d44
uri: avoid-height-width-in-img-tag
created: 2014-12-22T12:28:11.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects: 
- do-you-not-have-height-width-in-an-img-tag

---

Specifying the width and height properties for an **&lt;img&gt;** tag of HTML can sometimes turn out to be more trouble than it's worth, particularly if the image is later updated with different dimensions. If the height / width ratio doesn't match that of original image, the image might be stretched.

Adding fixed widths to your images may also disrupt the responsiveness of your content.

In other words, you should not have the image dimensions specified in HTML unless you have a very specific reason to do so. Use CSS if you need to specify images dimensions.

<!--endintro-->

``` html
<img src="images/codeauditor-logo.png" alt="Code Auditor logo" width="150" height="100" />
```
::: bad  
![Figure: Bad example - Stretched image caused by inline height/width ratio that doesn't match](streched-image.jpg)  
:::

``` html
<img src="images/codeauditor-logo.png" alt="Code Auditor logo"  />
```
::: good  
![Figure: Good example - Avoiding inline height/width ratio keeps the image as original](non-streched-image.jpg)  
:::
