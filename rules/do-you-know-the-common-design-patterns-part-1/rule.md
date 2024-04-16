---
type: rule
archivedreason: 
title: Do you know the common Design Patterns? (Part 1)
guid: 7c617edd-b576-4c1c-8771-d2a5edec7b1f
uri: do-you-know-the-common-design-patterns-part-1
created: 2012-04-02T04:44:06.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
- title: Dhruv Mathur
  url: https://ssw.com.au/people/dhruv-mathur
related: []
redirects:
- do-you-know-the-common-design-patterns-(part-1)

---

Design patterns are useful for ensuring [common design principles](/do-you-know-the-common-design-principles-part-1) are being followed.  They help make your code consistent, predictable, and easy to maintain.

<!--endintro-->

There are a very large number of Design Patterns, but here are a few important ones.

* **IOC** | [Inversion of Control](http&#58;//en.wikipedia.org/wiki/Inversion_of_control)  
In this pattern, control over the instantiation and management of objects is inverted, meaning that these responsibilities are handed over to an external framework like a DI container instead of being managed by the classes themselves. This separation enhances flexibility and decouples all the classes in the system.

* **DI** | [Dependency Injection](http&#58;//en.wikipedia.org/wiki/Dependency_injection)  
DI is a form of IoC where dependencies are provided to objects rather than created by them, one instance of the dependency can be used by many. This pattern also reduces dependency coupling between components since the instantiation is handled externally, making the system easier to manage and test.

* **Factory** | [Factory Pattern](http&#58;//en.wikipedia.org/wiki/Factory_pattern)  
It is a creational pattern that deals with the problem of creating objects without specifying the exact class of object that will be created. This is done by defining an interface or abstract class for creating an object, which subclasses decide how to implement. This pattern helps in managing and maintaining code by encapsulating how any object is created.

* **Singleton** | [Singleton Pattern](http&#58;//en.wikipedia.org/wiki/Singleton_pattern)  
This ensures that a class has only one instance and provides a global point of access to it. This pattern is used to control access to resources that are shared throughout an application, like a configuration file or connection to a database. This ensures that only a single shared instance of a class is consumed by the application.

* **Repository** | [Repository Pattern](http&#58;//msdn.microsoft.com/en-us/library/ff649690.aspx)  
A repository abstracts the data layer, providing a collection-like interface for accessing domain objects. It centralizes common data access functionalities and promotes a more organized data access architecture. By isolating the data layer, this pattern ensures that changes to the database access code are minimized when changes to the business logic or database specifics occur.

* **Unit of Work** | [Unit of Work Pattern](http&#58;//msdn.microsoft.com/en-us/magazine/dd882510.aspx)  
It is a way to keep track of everything you do during a transaction that can affect the database. When it's time to commit the transaction, it figures out everything that needs to be done to alter the database as a result of your work. This pattern is crucial for maintaining the consistency of data within the boundaries of a transaction.

* **MVC** | [Model View Controller](http&#58;//en.wikipedia.org/wiki/Model%e2%80%93view%e2%80%93controller)  
It is an architectural pattern that separates an application into three main logical components: the model, the view, and the controller. Each of these components handles different aspects of the application's data, user interface, and control logic, respectively. This separation helps manage complexity in large applications and have efficient code reuse.

* **MVP** | [Model View Presenter](http&#58;//en.wikipedia.org/wiki/Model_View_Presenter)
This pattern is a simpler version of MVC designed for modern applications where the user interface (the view) just displays information and responds to user inputs. In MVP, a middle-man called the presenter handles all the decision-making behind the scenes. It takes care of updating the view and reacting to user actions, making the view very simple and straightforward. This setup makes it easier to test the user interface because the view itself doesn't contain any complex logic—it just shows what the presenter tells it to.

By leveraging these design patterns, developers can solve complex problems more efficiently and ensure that their applications are robust, scalable, and easy to maintain. It is assumed knowledge that you know these design patterns. If you don't, read about them on the sites above or watch the [PluralSight videos on Design Patterns.](https://www.pluralsight.com/paths/design-patterns-in-c)
