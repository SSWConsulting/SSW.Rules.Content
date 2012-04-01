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



<span class='intro'> <div><span>“Only add complexity when you need flexibility” – Marcel de Vries</span></div>
​ </span>

​<span>Our controller is tightly coupled to the ExampleService and as a result, there is no way to unit test the controller.[This example is&#160;from the blog&#58;</span> <a href="http&#58;//www.devtrends.co.uk/blog/how-not-to-do-dependency-injection-the-static-or-singleton-container">http&#58;//www.devtrends.co.uk/blog/how-not-to-do-dependency-injection-the-static-or-singleton-container</a>&#160;<span>]</span> <table cellspacing="0" cellpadding="0" border="0" style="height&#58;auto;width&#58;714px;"><tbody><tr><td><div><div><code></code>&#160;</div>
<div class="ssw-rteStyle-CodeArea" style="height&#58;228px;width&#58;67.05%;"><code>public class HomeController<br>&#123;<br>&#160;&#160;&#160; private readonly IExampleService _service;<br>&#160;&#160;&#160; public HomeController()<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160; _service = new ExampleService();<br>&#160;&#160;&#160; &#125;&#160;&#160;&#160;&#160; <br>&#160;&#160;&#160; public ActionResult Index()<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; return View(_service.GetSomething());<br>&#160;&#160;&#160; &#125;<br>&#125;​</code></div>
<div class="ssw-rteStyle-FigureNormal"><code>Figure&#58;Controller coupled with ExampleService</code></div>
<div><code>we have known this,how do we fix it?use container badly - without dependecy injection</code></div>
<div class="ssw-rteStyle-CodeArea" style="height&#58;322px;width&#58;66.86%;"><code><table cellspacing="0" cellpadding="0" border="0" style="height&#58;auto;width&#58;714px;"><tbody><tr><td><div><div>public class HomeController<br>&#123;<br>&#160;&#160;&#160; private readonly IExampleService _service;<br>&#160;&#160;&#160;&#160; <br>&#160;&#160;&#160; public HomeController()<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160; _service = Container.Instance.Resolve&lt;IExampleService&gt;();<br>&#160;&#160;&#160; &#125;<br>&#160;&#160;&#160;&#160; <br>&#160;&#160;&#160; public ActionResult Index()<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; return View(_service.GetSomething());<br>&#160;&#160;&#160; &#125;<br>&#125;</div></div></td></tr></tbody></table></code></div></div></td></tr></tbody></table>
<div class="ssw-rteStyle-FigureBad"><span>&#160;Bad example - code showing NOT using dependency injection</span></div>
<div><span></span>&#160;</div>
<div><span>This is bad because</span></div>
<div><span>1.we removed one coupling and adding another one(the container).</span></div>
<div><span>2.it's not very clear what's going on.(</span><span>The beauty of dependency injection is that just by looking at the constructor of a class, you can tell exactly what it depends upon.</span>)<a href="http&#58;//codebetter.com/patricksmacchia/2009/02/01/understanding-code-static-vs-dynamic-dependencies/">Static IS THE　</a><span></span><span></span><span></span><span>KEY</span>&#58;<span>The</span><span></span><span></span><span></span><span> idea I would like to&#160;</span>defend now is that&#160;when it comes to</div>
understand and maintain a program, one need to focus mostly on thestatic&#160;dependencies, the ones found in<br>the source code<span>.</span> <div><br></div>
<div><span></span><div><div>use IoC correctly - with&#160;DI&#160;</div>
<div><span></span><table class="ssw-rteStyle-CodeArea" cellspacing="0" cellpadding="0" border="0" style="height&#58;auto;width&#58;714px;"><tbody><tr><td><div><div><code>public class HomeController<br>&#123;<br>&#160;&#160;&#160; private readonly IExampleService _service;<br>&#160;&#160;&#160;&#160;&#160;<br>&#160;&#160;&#160; public HomeController(IExampleService service)<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160; _service = service;<br>&#160;&#160;&#160; &#125;<br>&#160;&#160;&#160;&#160;&#160;<br>&#160;&#160;&#160; public ActionResult Index()<br>&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; return View(_service.GetSomething());<br>&#160;&#160;&#160; &#125;<br>&#125;​</code></div></div></td></tr></tbody></table>
<span class="ssw-rteStyle-FigureGood"><span>eg. Good example - code showing using dependency injection</span></span><div><span><br></span></div>
<div><span>about overuse of patterns​</span></div>
<div><span>pattern is an option,not must</span></div>
<div><span>1.principles v.s. design patterns</span></div>
<table cellspacing="0" border="1" style="font-size&#58;13px;border-top&#58;1px solid;font-family&#58;'lucida grande', 'bitstream vera sans', 'trebuchet ms', verdana, tahoma, arial, sans-serif;border-right&#58;0px solid;border-bottom&#58;0px solid;padding-bottom&#58;0px;padding-top&#58;0px;padding-left&#58;0px;margin&#58;0px;border-left&#58;1px solid;line-height&#58;normal;padding-right&#58;0px;"><tbody><tr><td style="border-top&#58;0px solid;border-right&#58;1px solid;border-bottom&#58;1px solid;padding-bottom&#58;5px;padding-top&#58;5px;padding-left&#58;5px;border-left&#58;0px solid;padding-right&#58;5px;"><b>SRP</b></td>
<td style="border-top&#58;0px solid;border-right&#58;1px solid;border-bottom&#58;1px solid;padding-bottom&#58;5px;padding-top&#58;5px;padding-left&#58;5px;border-left&#58;0px solid;padding-right&#58;5px;"><a href="http&#58;//www.objectmentor.com/resources/articles/srp.pdf" style="background-color&#58;transparent;">The Single Responsibility Principle</a></td>
<td style="border-top&#58;0px solid;border-right&#58;1px solid;border-bottom&#58;1px solid;padding-bottom&#58;5px;padding-top&#58;5px;padding-left&#58;5px;border-left&#58;0px solid;padding-right&#58;5px;"><i>A class should have one, and only one, reason to change.</i></td></tr>
<tr><td style="border-top&#58;0px solid;border-right&#58;1px solid;border-bottom&#58;1px solid;padding-bottom&#58;5px;padding-top&#58;5px;padding-left&#58;5px;border-left&#58;0px solid;padding-right&#58;5px;"><b>OCP</b></td>
<td style="border-top&#58;0px solid;border-right&#58;1px solid;border-bottom&#58;1px solid;padding-bottom&#58;5px;padding-top&#58;5px;padding-left&#58;5px;border-left&#58;0px solid;padding-right&#58;5px;"><a href="http&#58;//www.objectmentor.com/resources/articles/ocp.pdf" style="background-color&#58;transparent;">The Open Closed Principle</a></td>
<td style="border-top&#58;0px solid;border-right&#58;1px solid;border-bottom&#58;1px solid;padding-bottom&#58;5px;padding-top&#58;5px;padding-left&#58;5px;border-left&#58;0px solid;padding-right&#58;5px;"><i>You should be able to extend a classes behavior, without modifying it.</i></td></tr>
<tr><td style="border-top&#58;0px solid;border-right&#58;1px solid;border-bottom&#58;1px solid;padding-bottom&#58;5px;padding-top&#58;5px;padding-left&#58;5px;border-left&#58;0px solid;padding-right&#58;5px;"><b>LSP</b></td>
<td style="border-top&#58;0px solid;border-right&#58;1px solid;border-bottom&#58;1px solid;padding-bottom&#58;5px;padding-top&#58;5px;padding-left&#58;5px;border-left&#58;0px solid;padding-right&#58;5px;"><a href="http&#58;//www.objectmentor.com/resources/articles/lsp.pdf" style="background-color&#58;transparent;">The Liskov Substitution Principle</a></td>
<td style="border-top&#58;0px solid;border-right&#58;1px solid;border-bottom&#58;1px solid;padding-bottom&#58;5px;padding-top&#58;5px;padding-left&#58;5px;border-left&#58;0px solid;padding-right&#58;5px;"><i>Derived classes must be substitutable for their base classes.</i></td></tr>
<tr><td style="border-top&#58;0px solid;border-right&#58;1px solid;border-bottom&#58;1px solid;padding-bottom&#58;5px;padding-top&#58;5px;padding-left&#58;5px;border-left&#58;0px solid;padding-right&#58;5px;"><b>DIP</b></td>
<td style="border-top&#58;0px solid;border-right&#58;1px solid;border-bottom&#58;1px solid;padding-bottom&#58;5px;padding-top&#58;5px;padding-left&#58;5px;border-left&#58;0px solid;padding-right&#58;5px;"><a href="http&#58;//www.objectmentor.com/resources/articles/dip.pdf" style="background-color&#58;transparent;">The Dependency Inversion Principle</a></td>
<td style="border-top&#58;0px solid;border-right&#58;1px solid;border-bottom&#58;1px solid;padding-bottom&#58;5px;padding-top&#58;5px;padding-left&#58;5px;border-left&#58;0px solid;padding-right&#58;5px;"><i>Depend on abstractions, not on concretions.</i></td></tr>
<tr><td style="border-top&#58;0px solid;border-right&#58;1px solid;border-bottom&#58;1px solid;padding-bottom&#58;5px;padding-top&#58;5px;padding-left&#58;5px;border-left&#58;0px solid;padding-right&#58;5px;"><b>ISP</b></td>
<td style="border-top&#58;0px solid;border-right&#58;1px solid;border-bottom&#58;1px solid;padding-bottom&#58;5px;padding-top&#58;5px;padding-left&#58;5px;border-left&#58;0px solid;padding-right&#58;5px;"><a href="http&#58;//www.objectmentor.com/resources/articles/isp.pdf" style="background-color&#58;transparent;">The Interface Segregation Principle</a></td>
<td style="border-top&#58;0px solid;border-right&#58;1px solid;border-bottom&#58;1px solid;padding-bottom&#58;5px;padding-top&#58;5px;padding-left&#58;5px;border-left&#58;0px solid;padding-right&#58;5px;"><i>Make fine grained interfaces that are client specific.</i></td></tr></tbody></table>
<div><span>Figure&#58; 5 principles for class design</span></div>
<div>[<a href="http&#58;//butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod">http&#58;//butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod</a></div>
<div>&lt;&lt;<a href="http&#58;//codebetter.com/davidhayden/2005/05/20/agile-software-development-principles-patterns-and-practices/">Agile Software Development, Principles, Patterns, and Practices</a>​<span></span>&gt;&gt;Robert.C.Martin&#58;</div>
<div><a href="http&#58;//butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod"></a>]</div>
<span></span><div>&#160;</div></div></div></div>


