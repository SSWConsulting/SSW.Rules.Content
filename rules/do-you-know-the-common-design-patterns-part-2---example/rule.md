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



<span class='intro'> <div>​Appropriate use of design patterns can ensure your code is maintainable.</div> </span>

<p>For example, we could implement Inversion of Control by using the Dependency Injection pattern to&#160;decrease the coupling of our classes.</p>
<p>In this code, our controller is tightly coupled to the ExampleService and as a result, there is no way to unit test the controller.</p>
<p>[This example is from the blog&#58; <a href="http&#58;//www.devtrends.co.uk/blog/how-not-to-do-dependency-injection-the-static-or-singleton-container">http&#58;//www.devtrends.co.uk/blog/how-not-to-do-dependency-injection-the-static-or-singleton-container</a>]</p>
<div class="ssw-rteStyle-CodeArea" style="width&#58;67.05%;height&#58;228px;"><code>public class HomeController<br>&#123;<br>&#160;&#160;&#160; private readonly IExampleService _service;<br>&#160;&#160;&#160; public HomeController()<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160; _service = <span style="background-color&#58;#ffff00;">new ExampleService();</span><br>&#160;&#160;&#160; &#125;&#160;&#160;&#160;&#160; <br>&#160;&#160;&#160; public ActionResult Index()<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; return View(_service.GetSomething());<br>&#160;&#160;&#160; &#125;<br>&#125;​</code></div>
<div class="ssw-rteStyle-FigureBad">Figure&#58; Bad example - Controller coupled with ExampleService</div>
<div class="ssw-rteStyle-CodeArea" style="width&#58;66.86%;height&#58;322px;"><code><table border="0" cellspacing="0" cellpadding="0" style="width&#58;714px;height&#58;auto;"><tbody><tr><td><div><div>public class HomeController<br>&#123;<br>&#160;&#160;&#160; private readonly IExampleService _service;<br>&#160;&#160;&#160;&#160;&#160;<br>&#160;&#160;&#160; public HomeController()<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160; _service = <span style="background-color&#58;#ffff00;">Container.Instance.Resolve&lt;IExampleService&gt;();</span><br>&#160;&#160;&#160; &#125;<br>&#160;&#160;&#160;&#160; <br>&#160;&#160;&#160; public ActionResult Index()<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; return View(_service.GetSomething());<br>&#160;&#160;&#160; &#125;<br>&#125;</div></div></td></tr></tbody></table></code></div>
<div class="ssw-rteStyle-FigureBad"><span>Figure&#58;&#160;Bad example - 2nd attempt using an Inversion of Control container but *not*&#160;using dependency injection. A dependency now exists on the Container.</span></div>
<div><div><div>This is bad&#160;code because <span>we removed one coupling but added another one (the container).</span></div>
<div><div><table class="ssw-rteStyle-CodeArea" border="0" cellspacing="0" cellpadding="0" style="width&#58;714px;height&#58;auto;"><tbody><tr><td><div><div><code>public class HomeController<br>&#123;<br>&#160;&#160;&#160; private readonly IExampleService _service;<br>&#160;&#160;&#160;&#160;&#160;<br>&#160;&#160;&#160; public HomeController(<span style="background-color&#58;#ffff00;">IExampleService service</span>)<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160; _service = service;<br>&#160;&#160;&#160; &#125;<br>&#160;&#160;&#160;&#160;&#160;<br>&#160;&#160;&#160; public ActionResult Index()<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; return View(_service.GetSomething());<br>&#160;&#160;&#160; &#125;<br>&#125;​</code></div></div></td></tr></tbody></table>
<span class="ssw-rteStyle-FigureGood"><span>Figure&#58; Good example - code showing using dependency injection. No static dependencies.</span></span> It is important to know when the use of a pattern is appropriate.&#160; Patterns can be useful, but they can also be harmful if used incorrectly.</div></div></div></div>


