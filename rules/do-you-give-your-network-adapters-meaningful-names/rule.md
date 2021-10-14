---
type: rule
archivedreason: 
title: Do you give your Network Adapters meaningful names?
guid: d9d32b43-aad0-458a-bf0c-20606d294af0
uri: do-you-give-your-network-adapters-meaningful-names
created: 2012-03-02T18:33:02.0000000Z
authors: 
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

When you configure Hyper-V Clustering, each node will have upwards of 4 network adapters, some virtual and some physical. It is important to give these adapters meaningful names so you know what network adapter does what. 

<!--endintro-->

::: bad
![Figure: Bad Example - It makes it hard to know what network adapter does what if you don't have meaningful names](naming-bad.jpg)
:::

::: good
![Figure: Good example - As an example naming convention for network adapters on each node](naming-good.jpg)
:::

::: good
![Figure: Good Example - It is easy to tell which network adapter does what when they have meaningful names](naming-good2.jpg)
:::
