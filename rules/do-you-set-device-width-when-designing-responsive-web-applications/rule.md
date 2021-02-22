---
type: rule
archivedreason: 
title: Do you set device width when designing responsive web applications?
guid: 28fc4b70-6cd7-4106-947e-82f2452630a5
uri: do-you-set-device-width-when-designing-responsive-web-applications
created: 2014-06-21T03:26:58.0000000Z
authors:
- title: Ben Cull
  url: https://ssw.com.au/people/ben-cull
related: []
redirects: []

---

When designing a responsive website, you need to make sure that the browser understands how to correctly render your website. Device-Width informs the browser what the size of the viewport should be. 
<!--endintro-->

Since we want our website to render corectly for all screen sizes, we specify that it should set the viewport to the size of the device's screen.


```html
<meta name="viewport" content="width=device-width" />
```


This ensures the browser always renders at the correct resolution for the device.
