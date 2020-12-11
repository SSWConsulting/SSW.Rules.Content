---
type: rule
archivedreason: 
title: Do You Use a Dependency Injection Centric Architecture ?
guid: df1a3eca-21bb-4734-9276-18c0e1869be3
uri: do-you-use-a-dependency-injection-centric-architecture-
created: 2012-10-19T19:11:41.0000000Z
authors:
- id: 24
  title: Adam Stephensen
- id: 40
  title: Igor Goldobin
related: []

---

[[badExample]]
| ![N-Tiered architectures do not inherently support dependency injection](dependency-injection-bad.jpg)
[[goodExample]]
| ![The Onion Architecture promotes layers built on interfaces, and then injecting dependencies into those layers. This keeps coupling low, and therefore maintainability high](dependency-injection-good.jpg)
<!--endintro-->

The classes in each layer can depend on layers toward the centre.

It emphasizes the use of interfaces for the business logic and repository layers. The repository layer corresponds to the Data Access layer in an n-Tier architecture.

An n-Tier architecture has at its base the database.
The core of the onion architecture is the Domain Model, and all dependencies are injected. This leads to more maintainable applications since it emphasizes separation of concerns.

####  Further Reading: 

* [Do you know the layers of the onion architecture?](/Pages/The-layers-of-the-onion-architecture.aspx)
* [Do you know the best dependency injection container?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=0aa194e1-2de9-4ed1-b430-444109d65a50)
