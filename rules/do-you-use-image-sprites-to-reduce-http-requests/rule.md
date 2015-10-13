---
type: rule
archivedreason: 
title: Do you use image sprites to reduce HTTP requests?
guid: feb7f72b-d35c-4b46-a86b-92ae10916504
uri: do-you-use-image-sprites-to-reduce-http-requests
created: 2015-10-13T00:58:22.0000000Z
authors: []
related: []
redirects: []

---


<p>A sprite is an image that has all of your other images inside of it, so if your sprite 
             has 5 images, you’d be getting rid of 4 HTTP requests and speeding your site’s loading time 
             up by the time for each of those 4 requests latency. You will use CSS selectors for each 
             link to display only a portion of the image sprite - effectively showing just the 
             image you need.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>The benefits to use CSS image sprites are&#58;</p><ul><li>to save bandwidth</li><li>to reduce HTTP server requests</li><li>to speed up page load times</li></ul><p>Ensure that the file size of your master image isn't greater than the sum of its pieces.</p><dl class="badImage"><dt><img src="/PublishingImages/ImageSprites_bad.gif" alt="One image per Icon" /></dt><dd>Figure&#58; Bad Example - four images, one for each icon</dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/ImageSprites_good.gif" alt="One image contains all icons" /></dt><dd>Figure&#58; Good Example - one image contains all the icons and CSS selectors make the browser display only the part you need</dd></dl>


