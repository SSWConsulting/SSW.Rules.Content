---
type: rule
archivedreason: 
title: Do you know the common Design Patterns? (Part 2 - Example)
guid: 076632c1-c3b3-4a59-8fa6-55d6fb9ceeae
uri: do-you-know-the-common-design-patterns-part-2-example
created: 2012-03-20T02:29:38.0000000Z
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
redirects:
- do-you-know-the-common-design-patterns-(part-2-example)

---

Appropriate use of design patterns can ensure your code is maintainable and easy to read.

<!--endintro-->

### Dependency Injection

We should implement Inversion of Control by using the Dependency Injection pattern to decrease the direct coupling of our classes. Seprating the creation of objects or instances of services from thier usage allows for more flexibility and testability.

Lets look at an example, in this code, our controller is tightly coupled to the ExampleService and as a result, there is no way to unit test the controller.

[This example is from the blog: http://www.devtrends.co.uk/blog/how-not-to-do-dependency-injection-the-static-or-singleton-container]

```csharp
public class HomeController
{
    private readonly IExampleService _service;

    public HomeController()
    {
        _service = new ExampleService();
    }

    public ActionResult Index()
    {
        return View(_service.GetSomething());
    }
}
```

**❌ Figure: Bad example - Controller coupled with ExampleService.**

```csharp
public class HomeController
{
    private readonly IExampleService _service;

    public HomeController()
    {
        _service = Container.Instance.Resolve<IExampleService>();
    }

    public ActionResult Index()
    {
        return View(_service.GetSomething());
    }
}
```

**❌ Figure: Bad example - 2nd attempt using an Inversion of Control container but \*not\* using dependency injection. A dependency now exists on the Container.**

This is bad code because we removed one coupling but added another one (the container).

```csharp
public class HomeController
{
    private readonly IExampleService _service;

    public HomeController(IExampleService service)
    {
        _service = service;
    }

    public ActionResult Index()
    {
        return View(_service.GetSomething());
    }
}
```

**✅ Figure: Good example - code showing using dependency injection. No static dependencies.**

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

It is important to know when the use of a pattern is appropriate.  Patterns can be useful, but they can also be harmful if used incorrectly.
