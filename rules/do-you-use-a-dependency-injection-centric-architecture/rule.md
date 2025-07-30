---
seoDescription: Discover how to build maintainable applications using dependency injection centric architecture and master the Onion Architecture's layers.
type: rule
archivedreason:
title: Do you use a dependency injection centric architecture?
guid: df1a3eca-21bb-4734-9276-18c0e1869be3
uri: do-you-use-a-dependency-injection-centric-architecture
created: 2012-10-19T19:11:41.0000000Z
authors:
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
  - title: Igor Goldobin
    url: https://ssw.com.au/people/igor-goldobin
related:
  - do-you-know-the-layers-of-the-onion-architecture
  - the-best-dependency-injection-container
redirects: []
---

The classes in each layer can depend on layers toward the center. It emphasizes the use of interfaces for the business logic and repository layers.

The repository layer corresponds to the Data Access Layer in an n-Tier architecture. An n-Tier architecture has at its base the database.

The core of the onion architecture is the Domain Model, and all dependencies are injected. This leads to more maintainable applications since it emphasizes the separation of concerns.

<!--endintro-->

::: bad  
![Figure: Bad example – N-Tiered architectures do not inherently support dependency injection](dependency-injection-bad.jpg)  
:::

::: good  
![Figure: Good example – The Onion Architecture promotes layers built on interfaces, and then injecting dependencies into those layers. This keeps coupling low, and therefore maintainability high](dependency-injection-good.jpg)  
:::
