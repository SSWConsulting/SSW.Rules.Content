---
type: rule
title: Practices - Do you use client-side routing?
uri: practices---do-you-use-client-side-routing
created: 2016-04-22T22:39:45.0000000Z
authors:
- id: 55
  title: Steve Leigh
- id: 44
  title: Duncan Hunter

---



<span class='intro'> <p class="p1">Single page applications (SPAs) are getting more and more popular, and for good reason – a better and faster user experience, reduced server load and encourages good API separation.​</p><p class="p1">But have you ever visited a website, thought “I’ll refresh that” and then got taken back to the home screen? Or tried to copy or bookmark the URL, only to find it’s just “/Home”? This happens when client side routing hasn’t been implemented&#160;properly,&#160;and is a big hit to a site’s usability.</p> </span>

<p class="p1">This is easily fixed with Angular 2’s routing capabilities, and implementing it in your SPA will confer several advantages&#58;</p><ul class="ul1"><li class="li1">URLs can be copy-pasted and shared</li><li class="li1">Page refreshes work as expected</li><li class="li1">Less prone to errors</li></ul><ul class="ul1"><li class="li1">Better separation of concerns (navigation vs page state)&#160;</li></ul><p class="p2"><br></p><p class="p2"><img src="/PublishingImages/client-side-bad.png" alt="client-side-bad.png" style="margin&#58;5px;" /><br></p><p class="p1"><strong>Bad&#58; The blog post component is choosing components based on the state of the component</strong></p><p class="p2"><span style="line-height&#58;1.6;">A better way is to set up routes, and use a router (the first-party component router is great for this) to manage your components&#58;&#160;</span><br></p><p class="p2"><img src="/PublishingImages/client-side-good.png" alt="client-side-good.png" style="margin&#58;5px;" /><br></p><p class="p1"><strong>Good&#58; Setting up declarative routes and outlets gives a good user experience, persistent URLs and fewer moving parts </strong></p>


