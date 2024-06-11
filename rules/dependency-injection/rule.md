---
seoDescription: Implementing Dependency Injection effectively separates object creation from usage, increasing flexibility and testability while reducing coupling.
type: rule
archivedreason:
title: Do you use the Dependency Injection design pattern?
guid: 076632c1-c3b3-4a59-8fa6-55d6fb9ceeae
uri: dependency-injection
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
  - common-design-patterns
redirects: []
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
