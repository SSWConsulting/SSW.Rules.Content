---
seoDescription: Maintain a clear separation of concerns between design and code to ensure easy maintenance of your application.
type: rule
archivedreason:
title: Do you maintain separation of concerns?
guid: fab48b86-64c1-4686-8d8c-8b25b38bacd3
uri: maintain-separation-of-concerns
created: 2018-04-23T21:35:57.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-maintain-separation-of-concerns
---

One of the major issues people had back in the day with ASP (before ASP.NET) was the prevalence of "Spaghetti Code". This mixed **Reponse.Write()** with actual code.

<!--endintro-->

Ideally, you should keep design and code separate - otherwise, it will be difficult to maintain your application. Try to move all data access and business logic code into separate modules.

Bob Martin explains this best:

`youtube: https://www.youtube.com/embed/WpkDN78P884`
