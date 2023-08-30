---
type: rule
title: Do you make sure your images are hosted internally?
uri: images-should-be-hosted-internally
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related: []
redirects:
  - do-you-make-sure-your-images-are-hosted-internally
created: 2017-01-24T13:26:09.000Z
archivedreason: null
guid: 72bf9d1b-9ca5-4333-9e16-9adbc1dc6904
---

When want to show an image from the web on your website, the easiest way is to just copy the image's path and add it. This is not a good idea as the original host of the image can delete it, which will cause a broken image in your website.

<!--endintro-->

The right way to do this is to copy the image locally and upload to your own server, so you have total control over the image.

```html
<img src="https://some-external-url.com/images/open-extension.png" alt="Open extension"> 
<dd>Figure: Open extension</dd>
```
::: bad
Figure: Bad example - Using an external URL as image source. The image can be edited or deleted and there is nothing you can do about it
:::



```html
<img src="https://ssw.com.au/images/open-extension.png" alt="Open extension"> 
<dd>Figure: Open extension</dd>
```
::: good
Figure: Good example - Image is hosted internally. You have control over the image
:::

**Note:** For copyrighted images, you should **always** mention the source.
