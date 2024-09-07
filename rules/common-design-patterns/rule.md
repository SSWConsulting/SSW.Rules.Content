---
seoDescription: Design patterns separate complexity into manageable components, improving application maintainability and scalability.
type: rule
archivedreason:
title: Do you know the common Design Patterns?
guid: 7c617edd-b576-4c1c-8771-d2a5edec7b1f
uri: common-design-patterns
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
related:
  - dependency-injection
  - code-against-interfaces
  - use-specification-pattern
redirects:
  - do-you-know-the-common-design-patterns-(part-1)
  - do-you-know-the-common-design-patterns-part-1
  - do-you-know-the-common-design-patterns-(part-2-example)
  - do-you-know-the-common-design-patterns-part-2-example
---

Design patterns are useful for ensuring [common design principles](/do-you-know-the-common-design-principles-part-1) are being followed.  They help make your code consistent, predictable, and easy to maintain.

`youtube: https://www.youtube.com/watch?v=tv-_1er1mWI`
**Video: 10 Design Patterns Explained in 10 Minutes (10 min)**

<!--endintro-->

## Important design patterns

* **IOC** | [Inversion of Control](http://en.wikipedia.org/wiki/Inversion_of_control)  
  In this pattern, control over the instantiation and management of objects is inverted, meaning that these responsibilities are handed over to an external framework like a DI container instead of being managed by the classes themselves. This separation enhances flexibility and decouples all the classes in the system.

* **DI** | [Dependency Injection](/dependency-injection)  
  DI is a form of IoC where dependencies are provided to objects rather than created by them, one instance of the dependency can be used by many. This pattern also reduces dependency coupling between components since the instantiation is handled externally, making the system easier to manage and test.

* **Factory** | [Factory Pattern](http://en.wikipedia.org/wiki/Factory_pattern)  
  It is a creational pattern that deals with the problem of creating objects without specifying the exact class of object that will be created. This is done by defining an interface or abstract class for creating an object, which subclasses decide how to implement. This pattern helps in managing and maintaining code by encapsulating how any object is created.

* **Singleton** | [Singleton Pattern](http://en.wikipedia.org/wiki/Singleton_pattern)  
  This ensures that a class has only one instance and provides a global point of access to it. This pattern is used to control access to resources that are shared throughout an application, like a configuration file or connection to a database. This ensures that only a single shared instance of a class is consumed by the application.

* **Repository** | [Repository Pattern](http://msdn.microsoft.com/en-us/library/ff649690.aspx)  
  A repository abstracts the data layer, providing a collection-like interface for accessing domain objects. It centralizes common data access functionalities and promotes a more organized data access architecture. By isolating the data layer, this pattern ensures that changes to the database access code are minimized when changes to the business logic or database specifics occur.

* **Unit of Work** | [Unit of Work Pattern](http://msdn.microsoft.com/en-us/magazine/dd882510.aspx)  
  It is a way to keep track of everything you do during a transaction that can affect the database. When it's time to commit the transaction, it figures out everything that needs to be done to alter the database as a result of your work. This pattern is crucial for maintaining the consistency of data within the boundaries of a transaction.

* **MVC** | [Model View Controller](http://en.wikipedia.org/wiki/Model%e2%80%93view%e2%80%93controller)  
  It is an architectural pattern that separates an application into three main logical components: the model, the view, and the controller. Each of these components handles different aspects of the application's data, user interface, and control logic, respectively. This separation helps manage complexity in large applications.

* **MVP** | [Model View Presenter](http://en.wikipedia.org/wiki/Model_View_Presenter)
  This pattern is a simpler version of MVC designed for modern applications where the user interface (the view) just displays information and responds to user inputs. In MVP, a middle-man called the presenter handles all the decision-making behind the scenes. It takes care of updating the view and reacting to user actions, making the view very simple and straightforward. This setup makes it easier to test the user interface because the view itself doesn't contain any complex logic—it just shows what the presenter tells it to.

* **Mediator** | [Mediator Pattern](http://en.wikipedia.org/wiki/Mediator_pattern)
  The mediator pattern uses a central object to handle communication between other objects in a system, promoting separation of concerns. This means each object doesn’t need to know about the details of how others operate, making the system easier to maintain and extend.

![Figure: Developers use design patterns to build quality solutions](design-patterns.png)

## Other design patterns

* **Decorator** | [Decorator Pattern](http://en.wikipedia.org/wiki/Decorator_pattern)
  The decorator pattern allows behavior to be added to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class. This pattern is useful for adding new features to objects without changing their structure, making it easier to extend the functionality of an object.

* **Command** | [Command Pattern](http://en.wikipedia.org/wiki/Command_pattern)
  The command pattern encapsulates a request as an object, allowing you to parameterize clients with queues, requests, and operations. This pattern helps in decoupling the sender and receiver of a request, making it easier to implement undo and redo functionalities.

* **Strategy** | [Strategy Pattern](http://en.wikipedia.org/wiki/Strategy_pattern)
  The strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. This pattern allows the algorithm to vary independently from the client that uses it, making it easier to switch between different algorithms at runtime.

* **Specification** | [Specification Pattern](http://en.wikipedia.org/wiki/Specification_pattern)
  The specification pattern is used to define business rules that can be combined to form complex rules. This pattern helps in separating the logic for checking business rules from the domain model, making it easier to maintain and reuse the rules.

* **Prototype** | [Prototype Pattern](http://en.wikipedia.org/wiki/Prototype_pattern)
  The prototype pattern is used to create new objects by copying a model instance. This method helps avoid the complexity of using subclasses and reduces the performance cost associated with creating new objects using the standard method (e.g., with the 'new' keyword), especially when it's too costly for the application.

* **Builder** | [Builder Pattern](http://en.wikipedia.org/wiki/Builder_pattern)
  The builder pattern is a flexible design pattern used to construct complex objects. It separates the process of building an object from the object's representation, making it easier to create different representations of an object using the same construction process.

* **Facade** | [Facade Pattern](http://en.wikipedia.org/wiki/Facade_pattern)
  The facade pattern simplifies interaction with complex subsystems by providing a single, straightforward interface. This makes the subsystem easier to use and maintain by hiding its complexities.

* **Proxy** | [Proxy Pattern](http://en.wikipedia.org/wiki/Proxy_pattern)
  The proxy pattern uses a placeholder or proxy object to control access to another object. It acts like a representative for the original object, managing interactions and access to it. This helps in controlling how and when the actual object is accessed.

* **Iterator** | [Iterator Pattern](http://en.wikipedia.org/wiki/Iterator_pattern)
  The iterator pattern lets you go through elements in a collection one by one without revealing how the collection is structured. It provides a standard way to loop through different types of collections, making it easier to access their elements.

* **Observer** | [Observer Pattern](http://en.wikipedia.org/wiki/Observer_pattern)
  The observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. This pattern is useful for building loosely coupled systems where objects can communicate with each other without knowing each other's details.

* **State** | [State Pattern](http://en.wikipedia.org/wiki/State_pattern)
  The state pattern allows an object to change its behavior when its internal state changes. It encapsulates the behavior of an object into separate classes, making it easier to add new states and transitions without changing the object's code.

By leveraging these design patterns, developers can solve complex problems more efficiently and ensure that their applications are robust, scalable, and easy to maintain. It is assumed knowledge that you know these design patterns. If you don't, read about them on the sites above or watch the [PluralSight videos on Design Patterns.](https://www.pluralsight.com/paths/design-patterns-in-c)

It is important to know when the use of a pattern is appropriate. Patterns can be useful, but they can also be harmful if used incorrectly.
