---
type: rule
seoDescription: Are you leveraging dynamic viewport units? They ensure your website remains responsive across a range of screen sizes.
archivedreason:
title: Do you use dynamic viewport units?
guid: 50820f73-f1bc-4507-abb7-832df3ec8a04
uri: use-dynamic-viewport-units
created: 2024-07-16T04:28:49.0000000Z
authors: 
- title: Jord Gui
  url: https://ssw.com.au/people/jord-gui
related:
- progressive-web-app

---
In today's mobile-first era, ensuring your website looks great on all screen sizes is crucial. 

On mobile devices, viewport sizes fluctuate due to [dynamic toolbars](https://web.dev/blog/viewport-units#the-need-for-new-viewport-units) like address bars and tab bars, causing elements to potentially overflow beyond the viewport.

To address this issue, the CSS Working Group introduced [dynamic viewport units](https://developer.mozilla.org/en-US/docs/Web/CSS/length#dynamic) (like dvw, dvh, dvi, dvb, dvmin, dvmax).

Implementing these units into your website allows it to be responsive across desktop and mobile platforms.

<!--endintro-->

Dynamic viewport units are [compatible with every browser](https://developer.mozilla.org/en-US/docs/Web/CSS/length#browser_compatibility) and is even supported in popular CSS frameworks like [Tailwind CSS (as of v3.4)](https://tailwindcss.com/blog/tailwindcss-v3-4#dynamic-viewport-units)

::: img-medium
![Figure: Browser compatibility list for dynamic viewport units](dvu-browser-compatibility.png)
:::

::: bad  
![Figure: Bad example - TinaCMS media manager window overflowing when open on iPadOS Safari when using view height](dvu-bad-example.png)  
:::

::: good  
![Figure: Good example - TinaCMS media manager window responding properly when open on iPadOS Safari when using dynamic view height](dvu-good-example.png)  
:::
