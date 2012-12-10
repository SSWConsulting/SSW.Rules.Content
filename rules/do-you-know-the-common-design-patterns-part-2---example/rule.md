---
type: rule
title: Do you know the common Design Patterns? (Part 2 - Example)
uri: do-you-know-the-common-design-patterns-part-2---example
created: 2012-03-20T02:29:38.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 23
  title: Damian Brady
- id: 24
  title: Adam Stephensen
- id: 3
  title: Eric Phan

---



<span class='intro'> <p>​Appropriate use of design patterns can ensure your code is maintainable.</p> </span>

<p>Always code against an interface rather than a concrete implementation. Use dependency injection to control which implementation the interface uses.</p>
<p>For example, we could implement Inversion of Control by using the Dependency Injection pattern to decrease the coupling of our classes.</p>
<p>In this code, our controller is tightly coupled to the ExampleService and as a result, there is no way to unit test the controller.</p>
<p>[This example is from the blog&#58; <a href="http&#58;//www.devtrends.co.uk/blog/how-not-to-do-dependency-injection-the-static-or-singleton-container">http&#58;//www.devtrends.co.uk/blog/how-not-to-do-dependency-injection-the-static-or-singleton-container</a>]</p>
<div class="ssw-rteStyle-CodeArea" style="height&#58;228px;width&#58;67.05%;"><code>public class HomeController<br>&#123;<br>&#160;&#160;&#160; private readonly IExampleService _service;<br>&#160;&#160;&#160; public HomeController()<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160; _service = <span style="background-color&#58;rgb(255,255,0);">new ExampleService();</span><br>&#160;&#160;&#160; &#125;&#160;&#160;&#160;&#160; <br>&#160;&#160;&#160; public ActionResult Index()<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; return View(_service.GetSomething());<br>&#160;&#160;&#160; &#125;<br>&#125;​</code></div>
<div class="ssw-rteStyle-FigureBad">Figure&#58; Bad example - Controller coupled with ExampleService</div>
<div class="ssw-rteStyle-CodeArea" style="height&#58;322px;width&#58;66.86%;"><code>public class HomeController<br>&#123;<br>&#160;&#160;&#160; private readonly IExampleService _service;<br>&#160;&#160;&#160;&#160;&#160;<br>&#160;&#160;&#160; public HomeController()<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160; _service = <span style="background-color&#58;rgb(255,255,0);">Container.Instance.Resolve&lt;IExampleService&gt;();</span><br>&#160;&#160;&#160; &#125;<br>&#160;&#160;&#160;&#160; <br>&#160;&#160;&#160; public ActionResult Index()<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; return View(_service.GetSomething());<br>&#160;&#160;&#160; &#125;<br>&#125; </code></div>
<div class="ssw-rteStyle-FigureBad"><span>Figure&#58;&#160;Bad example - 2nd attempt using an Inversion of Control container but *not*&#160;using dependency injection. A dependency now exists on the Container.</span></div>
<p>This is bad&#160;code because we removed one coupling but added another one (the container).</p>
<div class="ssw-rteStyle-CodeArea" style="width&#58;66.86%;"><code>public class HomeController<br>&#123;<br>&#160;&#160;&#160; private readonly IExampleService _service;<br>&#160;&#160;&#160;&#160;&#160;<br>&#160;&#160;&#160; public HomeController(<span style="background-color&#58;rgb(255,255,0);">IExampleService service</span>)<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160; _service = service;<br>&#160;&#160;&#160; &#125;<br>&#160;&#160;&#160;&#160;&#160;<br>&#160;&#160;&#160; public ActionResult Index()<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; return View(_service.GetSomething());<br>&#160;&#160;&#160; &#125;<br>&#125;​</code></div>
<span class="ssw-rteStyle-FigureGood">Figure&#58; Good example - code showing using dependency injection. No static dependencies.</span> <p>Even better, use Annotate so you can enlighten the developer.</p>
<span style="font-size&#58;11pt;font-family&#58;'calibri','sans-serif';color&#58;black;"></span><p><img alt="bad.png" src="/PublishingImages/Code%20against%20interfaces%20-%20bad.png" style="margin&#58;5px;" /><br><strong class="ssw-rteStyle-FigureBad">Figure&#58; Bad Example - Referencing the concrete EF context</strong></p>
<p><span><img src="/Documents/Code%20against%20interfaces%20-%20good.png" alt="" style="height&#58;328px;margin&#58;5px;width&#58;872px;" /><br><strong class="ssw-rteStyle-FigureGood">Figure&#58; Good Example - Programming against the interface</strong><br></span></p>
<p>It is important to know when the use of a pattern is appropriate.&#160; Patterns can be useful, but they can also be harmful if used incorrectly.</p>


