---
type: rule
archivedreason: 
title: Do you know the best time to tackle performance testing?
guid: 3dc509c0-c346-4e4d-a1d4-750299490aee
uri: the-best-time-to-tackle-performance-testing
created: 2019-08-27T17:28:21.0000000Z
authors:
- title: Matt Wicks
  url: https://ssw.com.au/people/matt-wicks
related: []
redirects:
- do-you-know-the-best-time-to-tackle-performance-testing

---

Performance, load and stress testing should be tackled after you have confirmed that everything works functionally (usually after UX testing). Performance testing should only be after daily errors are down to zero (reported by Application Insights or Raygun). This way you can be sure that any functional issues that occur during performance tests are scaling issues.

<!--endintro-->
