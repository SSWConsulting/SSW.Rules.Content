---
type: rule
archivedreason: 
title: Do You Use a Dependency Injection Centric Architecture?
guid: df1a3eca-21bb-4734-9276-18c0e1869be3
uri: do-you-use-a-dependency-injection-centric-architecture
created: 2012-10-19T19:11:41.0000000Z
authors:
- title: Adam Stephensen
  url: /people/adam-stephensen
- title: Igor Goldobin
  url: /people/igor-goldobin
related: []
redirects: []

---

The classes in each layer can depend on layers toward the center.

It emphasizes the use of interfaces for the business logic and repository layers. The repository layer corresponds to the Data Access Layer in an n-Tier architecture.

An n-Tier architecture has at its base the database.

The core of the onion architecture is the Domain Model, and all dependencies are injected. This leads to more maintainable applications since it emphasizes the separation of concerns.


<!--endintro-->


::: bad  
![Figure: Bad Example – N-Tiered architectures do not inherently support dependency injection](dependency-injection-bad.jpg)  
:::


::: good  
![Figure: Good Example – The Onion Architecture promotes layers built on interfaces, and then injecting dependencies into those layers. This keeps coupling low, and therefore maintainability high](dependency-injection-good.jpg)  
:::

###  Related rules


* [Do you know the layers of the onion architecture?](/do-you-know-the-layers-of-the-onion-architecture)
* [Do you know the best dependency injection container?](/do-you-know-the-best-dependency-injection-container-aka-do-not-waste-days-evaluating-ioc-containers)
