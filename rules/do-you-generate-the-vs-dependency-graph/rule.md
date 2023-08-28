---
type: rule
archivedreason: 
title: Do you generate the VS Dependency Graph?
guid: 726eadfd-fa6c-4549-acfd-bc9e30e378fe
uri: do-you-generate-the-vs-dependency-graph
created: 2012-03-16T08:04:49.0000000Z
authors:
- title: Adam Cogan
  url: /people/adam-cogan
- title: Adam Stephensen
  url: /people/adam-stephensen
- title: Igor Goldobin
  url: /people/igor-goldobin
related: []
redirects: []

---

Dependency graphs are important because they give you an indication of the coupling between the different components within your application.

A well architected application (ie. one that correctly follows the Onion Architecture) will be easy to maintain because it is loosely coupled.

<!--endintro-->


::: bad  
![Figure: Bad Example- The Visual Studio Dependency Graph is hard to read](TimePRODependence.png)  
:::


::: good  
![Figure: Good Example – The ReSharper Dependency graph groups dependencies based on Solution Folders. By having a        Consistent Solution Structure it is easy to see from your Dependency Graph if there is coupling between your UI and your Dependencies](TimePRODependence-good.png)  
:::

#### Further Reading:

* [Do you use a dependency injection centric architecture?](/do-you-use-a-dependency-injection-centric-architecture)
* [Do you know the best dependency injection container?](/the-best-dependency-injection-container)
