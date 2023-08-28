---
type: rule
archivedreason: 
title: Do you know the common Design Patterns? (Part 2 - Example)
guid: 076632c1-c3b3-4a59-8fa6-55d6fb9ceeae
uri: do-you-know-the-common-design-patterns-part-2-example
created: 2012-03-20T02:29:38.0000000Z
authors:
- title: Adam Cogan
  url: /people/adam-cogan
- title: Damian Brady
  url: /people/damian-brady
- title: Adam Stephensen
  url: /people/adam-stephensen
- title: Eric Phan
  url: /people/eric-phan
related:
- do-you-name-your-dependencies-to-avoid-problems-with-minification
redirects:
- do-you-know-the-common-design-patterns-(part-2-example)

---

Appropriate use of design patterns can ensure your code is maintainable.

<!--endintro-->

Always code against an interface rather than a concrete implementation. Use dependency injection to control which implementation the interface uses.

For example, we could implement Inversion of Control by using the Dependency Injection pattern to decrease the coupling of our classes.

In this code, our controller is tightly coupled to the ExampleService and as a result, there is no way to unit test the controller.

[This example is from the blog: http://www.devtrends.co.uk/blog/how-not-to-do-dependency-injection-the-static-or-singleton-container]

`public class HomeController{    private readonly IExampleService _service;    public HomeController()    {      _service = new ExampleService();    }         public ActionResult Index()    {        return View(_service.GetSomething());    }}`

Figure: Bad example - Controller coupled with ExampleService

`public class HomeController{    private readonly IExampleService _service;         public HomeController()    {      _service = Container.Instance.Resolve<IExampleService>();    }         public ActionResult Index()    {        return View(_service.GetSomething());    }}`

Figure: Bad example - 2nd attempt using an Inversion of Control container but \*not\* using dependency injection. A dependency now exists on the Container.

This is bad code because we removed one coupling but added another one (the container).

`public class HomeController{    private readonly IExampleService _service;         public HomeController(IExampleService service)    {      _service = service;    }         public ActionResult Index()    {        return View(_service.GetSomething());    }}`
Figure: Good example - code showing using dependency injection. No static dependencies. 
Even better, use Annotate so you can enlighten the developer.

![bad.png](Code against interfaces - bad.png)
**Figure: Bad Example - Referencing the concrete EF context**

![](Code against interfaces - good.png)
**Figure: Good Example - Programming against the interface**

It is important to know when the use of a pattern is appropriate.  Patterns can be useful, but they can also be harmful if used incorrectly.
