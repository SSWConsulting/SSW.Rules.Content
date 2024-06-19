---
seoDescription: Single-page applications (SPAs) offer a better user experience and reduced server load, but improper client-side routing can hinder usability. Implementing Angular's routing capabilities provides advantages like shareable URLs, accurate page refreshes, and improved separation of concerns.
type: rule
archivedreason:
title: Practices - Do you use client-side routing?
guid: 61245309-7d1c-4c21-9ba6-997f031e75e0
uri: use-client-side-routing
created: 2016-04-22T22:39:45.0000000Z
authors:
  - title: Steve Leigh
    url: https://ssw.com.au/people/steve-leigh
  - title: Duncan Hunter
    url: https://ssw.com.au/people/duncan-hunter
related: []
redirects:
  - practices-do-you-use-client-side-routing
---

Single page applications (SPAs) are getting more and more popular, and for good reason – a better and faster user experience, reduced server load and encourages good API separation.

But have you ever visited a website, thought “I’ll refresh that” and then got taken back to the home screen? Or tried to copy or bookmark the URL, only to find it’s just “/Home”? This happens when client-side routing hasn’t been implemented properly and is a big hit to a site’s usability.

<!--endintro-->

This is easily fixed with Angular ’s routing capabilities, and implementing it in your SPA will confer several advantages:

- URLs can be copy-pasted and shared
- Page refreshes work as expected
- Less prone to errors
- Better separation of concerns (navigation vs page state)

::: bad  
![Figure: Bad example - The blog post component is choosing components based on the state of the component](client-side-bad.png)  
:::

A better way is to set up routes, and use a router (the first-party component router is great for this) to manage your components:

::: good  
![Good: Setting up declarative routes and outlets gives a good user experience, persistent URLs, and fewer moving parts](client-side-good.png)  
:::
