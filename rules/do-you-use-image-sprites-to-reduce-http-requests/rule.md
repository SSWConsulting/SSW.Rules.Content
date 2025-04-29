---
seoDescription: Reduce HTTP requests and speed up page load times by using CSS image sprites, a technique that combines multiple images into one, allowing browsers to display only the needed portion.
type: rule
archivedreason: Considered obsolete due to advancements in modern web technologies, like https://www.ssw.com.au/rules/use-a-cdn
title: Do you use image sprites to reduce HTTP requests?
guid: feb7f72b-d35c-4b46-a86b-92ae10916504
uri: do-you-use-image-sprites-to-reduce-http-requests
created: 2015-10-13T00:58:22.0000000Z
authors: 
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
---

A sprite is an image that has all of your other images inside of it, so if your sprite has 5 images, you’d be getting rid of 4 HTTP requests and speeding your site’s loading time up by the time for each of those 4 requests latency. You will use CSS selectors for each link to display only a portion of the image sprite - effectively showing just the image you need.

<!--endintro-->

The benefits to use CSS image sprites are:

* to save bandwidth
* to reduce HTTP server requests
* to speed up page load times

Ensure that the file size of your master image isn't greater than the sum of its pieces.

::: bad  
![Figure: Bad example - four images, one for each icon](ImageSprites_bad.gif)  
:::

::: good  
![Figure: Good Example - one image contains all the icons and CSS selectors make the browser display only the part you need](ImageSprites_good.gif)  
:::
