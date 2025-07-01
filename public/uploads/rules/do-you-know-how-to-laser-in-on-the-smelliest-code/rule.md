---
seoDescription: Identify and refactor "smelliest code" using Visual Studio's Code Metrics to pinpoint hotspots, then collaborate with responsible developers.
type: rule
archivedreason:
title: Do you know how to laser in on the smelliest code?
guid: c69ca2e5-0323-430e-ae26-62a753d4ace5
uri: do-you-know-how-to-laser-in-on-the-smelliest-code
created: 2012-03-16T08:36:31.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []
---

Rather than randomly browsing for dodgy code, use Visual Studio's Code Metrics feature to identify "Hot Spots" that require investigation.

::: bad  
![Figure: The bad was is to browse the code](lotto-balls.jpeg)  
:::

<!--endintro-->

![Figure: Run Code Metrics in Visual Studio](VS 11 Code Metrics.png)

![Figure: Red dots indicate the code that is hard to maintain. E.g. Save() and LoadCustomer()](CodeMetrics_3_1710232021935.png)

Identifying the problem areas is only the start of the process. From here, you should speak to the developers responsible for this dodgy code. There might be good reasons why they haven't invested time on this.

![Figure: Find out who the devs are by using CodeLens and start a conversation](codelens-start-conversation.png)

**Tip:** Learn [the benefits of Source Control](/do-you-know-the-benefits-of-using-source-control).

::: greybox
**Suggestion to Microsoft:** Allow us to visualize the developers responsible for the bad code (currently and historically) using CodeLens.
:::
