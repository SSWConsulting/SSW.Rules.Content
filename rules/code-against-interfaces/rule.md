---
seoDescription: Code effectively against interfaces to ensure maintainable and readable code, making it easier to swap out implementations without modifying using code.
type: rule
archivedreason:
title: Do you code against interfaces?
guid: d1088a85-0785-42ce-94f6-abb6290dfd61
uri: code-against-interfaces
created: 2024-04-18T02:29:38.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
  - title: Eric Phan
    url: https://ssw.com.au/people/eric-phan
  - title: Dhruv Mathur
    url: https://ssw.com.au/people/dhruv-mathur
related:
  - do-you-name-your-dependencies-to-avoid-problems-with-minification
  - common-design-patterns
  - dependency-injection
redirects: []
---

Appropriate use of design patterns can ensure your code is maintainable and easy to read.

<!--endintro-->

### Code against Interfaces

Always code against an interface rather than a concrete implementation. Use dependency injection to control which implementation the interface uses. By doing this you create a contract for that service which the rest of the codebase has to adhere to.

By creating an interface for each service and programming against the interface, you can easily swap out the implementation of the service without changing the code that uses the service.

It is important to also control the scope of the injection. For example, in ASP.NET 8 application you have the option to register the concrete implementation in the DI container either as a singleton, scoped, or transient service. Each of them will have a different lifetime in the application and should be set as per the requirement.

![](Code against interfaces - bad.png)
**❌ Figure: Bad Example - Referencing the concrete EF context**

This is bad code because now the controller is directly dependent on the implementation of the EF context. This also increase the effort for unit testing.

![](Code against interfaces - good.png)
**✅ Figure: Good Example - Programming against the interface**

This is good because now you can test the controller and the services independently. Also the controller only talks to the service through the functionality exposed by the interface, enforcing encapsulation.
