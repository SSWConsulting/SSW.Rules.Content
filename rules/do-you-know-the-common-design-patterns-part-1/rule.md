---
type: rule
archivedreason: 
title: Do you know the common Design Patterns? (Part 1)
guid: 7c617edd-b576-4c1c-8771-d2a5edec7b1f
uri: do-you-know-the-common-design-patterns-part-1
created: 2012-04-02T04:44:06.0000000Z
authors:
- title: Adam Cogan
  url: /people/adam-cogan
- title: Adam Stephensen
  url: /people/adam-stephensen
- title: Damian Brady
  url: /people/damian-brady
related: []
redirects:
- do-you-know-the-common-design-patterns-(part-1)

---

Design patterns are useful for ensuring [common design principles](/do-you-know-the-common-design-principles-part-1)are being followed.  They help make your code consistent, predictable, and easy to maintain.

<!--endintro-->

There are a very large number of Design Patterns, but here are a few important ones.

- **IOC** | [Inversion of Control](http&#58;//en.wikipedia.org/wiki/Inversion_of_control)  
Control of the object coupling is the responsibility of the caller, not the class.

- **DI** | [Dependency Injection](http&#58;//en.wikipedia.org/wiki/Dependency_injection)  
Dependencies are "injected" into the dependent object rather than the object depending on concretions.

- **Factory** | [Factory Pattern](http&#58;//en.wikipedia.org/wiki/Factory_pattern)  
Object creation is handled by a "factory" that can provide different concretions based on an abstraction.

- **Singleton** | [Singleton Pattern](http&#58;//en.wikipedia.org/wiki/Singleton_pattern)  
Instantiation of an object is limited to one instance to be shared across the system.

- **Repository** | [Repository Pattern](http&#58;//msdn.microsoft.com/en-us/library/ff649690.aspx)  
A repository is used to handle the data mapping details of CRUD operations on domain objects. 

- **Unit of Work** | [Unit of Work Pattern](http&#58;//msdn.microsoft.com/en-us/magazine/dd882510.aspx)  
A way of handling multiple database operations that need to be done as part of a piece of work. 

- **MVC** | [Model View Controller](http&#58;//en.wikipedia.org/wiki/Model%e2%80%93view%e2%80%93controller)  
An architectural pattern separating domain logic (Controller) from how domain objects (Models) are presented (View).

- **MVP** | [Model View Presenter](http&#58;//en.wikipedia.org/wiki/Model_View_Presenter)   
An architectural pattern deriving from MVC where the View handles UI events instead of the Controller.

Choose patterns wisely to improve your solution architecture. It is assumed knowledge that you know these design patterns. If you don't, read about them on the sites above or watch the [PluralSight videos on Design Patterns.](https://www.pluralsight.com/paths/design-patterns-in-c)
