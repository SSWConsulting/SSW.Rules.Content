---
type: rule
archivedreason: 
title: Do you know the layers of the onion architecture?
guid: aa31cbec-f7bf-463c-ab4f-02c346fdc14b
uri: do-you-know-the-layers-of-the-onion-architecture
created: 2012-10-19T19:23:27.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ben Cull
  url: https://ssw.com.au/people/ben-cull
related: []
redirects: []

---

[![Onion Architecture](Onion-Architecture.jpg)](/Documents/Onion-Architecture.pdf)Figure: The layers of the onion architecture 
<!--endintro-->

### Application Core (the grey stuff)

This should be the big meaty part of the application where the domain logic resides.

### Domain Model

In the very centre, we see the Domain Model, which represents the state and behaviour combination that models truth for the organization and is only coupled to itself.

### Repository Interfaces

The first layer around the Domain Model is typically where we find interfaces that provide object saving and retrieving behaviour. 
The object saving behaviour is not in the application core, however, because it typically involves a database.  Only the interface is in the application core.  The actual implementation is a dependency which is injected.

### Business Logic Interfaces

Business logic is also exposed via interfaces to provide decoupling of business logic. 
Examples of where this is useful include substituting a FacebookNotificationService for an EmailNotificationService or a FedExShippingCalculator for a DHLShippingCalculator

### Clients (the red stuff)

The outer layer is reserved for things that change often.  E.g. UI and the other applications that consume the Application Core. 
This includes the MVC project.
Any interface dependencies in factories, services, repositories, etc, are injected into the domain by the controller.
This means any constructor-injected interfaces in domain classes are resolved automatically by the IoC container.

### Dependencies

Dependencies are implementations of interfaces defined in Repository and Business Logic Interfaces and Domain.
These classes are specific implementations and can be coupled to a particular method of data access, or specific service technology.
e.g. this is where the EF DbContext is implemented, as well as things like logging, email sending, etc.

These dependencies are injected into the application core.

Because the Application core only relies on abstractions of the dependencies, it is easy to update them.

The Onion Architecture relies heavily on the [Dependency Inversion](http://en.wikipedia.org/wiki/Dependency_inversion_principle) principle and other [SOLID principles](/do-you-know-the-common-design-principles-part-1).
(Note: Onion Architecture has been replaced by [Clean Architecture](/rules-to-better-clean-architecture))

#### References:

* http://blog.tonysneed.com/2011/10/08/peeling-back-the-onion-architecture/
* [http://stackoverflow.com/questions/9732747/what-type-of-architecture-is-this-called/9933371#9933371](http://stackoverflow.com/questions/9732747/what-type-of-architecture-is-this-called/9933371)


### Use SSW Data Onion to Generate your Code


To help make this process pain free, we've developed the [SSW Data Onion](http://www.sswdataonion.com/) to get you going and take away the boilerplate code you would normally need to write. Check out this cool video to see how it works:




`youtube: https://www.youtube.com/embed/FcuFya8vud8?rel=0&controls=0&showinfo=0`
 



**Further Reading:** [Do You Use a Dependency Injection Centric Architecture?](/Pages/Use-a-Dependency-Injection-Centric-Architecture.aspx)
