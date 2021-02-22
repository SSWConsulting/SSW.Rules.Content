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
related:
- do-you-name-your-dependencies-to-avoid-problems-with-minification
redirects:
- do-you-know-the-common-design-patterns-(part-2-example)

---


<p>​Appropriate use of design patterns can ensure your code is maintainable.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>Always code against an interface rather than a concrete implementation. Use dependency injection to control which implementation the interface uses.</p>
<p>For example, we could implement Inversion of Control by using the Dependency Injection pattern to decrease the coupling of our classes.</p>
<p>In this code, our controller is tightly coupled to the ExampleService and as a result, there is no way to unit test the controller.</p>
<p>[This example is from the blog: <a href="http://www.devtrends.co.uk/blog/how-not-to-do-dependency-injection-the-static-or-singleton-container">http://www.devtrends.co.uk/blog/how-not-to-do-dependency-injection-the-static-or-singleton-container</a>]</p>
<div class="ssw-rteStyle-CodeArea" style="height:228px;width:67.05%;"><code>public class HomeController<br>{<br>    private readonly IExampleService _service;<br>    public HomeController()<br>    {<br>      _service = <span style="background-color:rgb(255,255,0);">new ExampleService();</span><br>    }     <br>    public ActionResult Index()<br>    {<br>        return View(_service.GetSomething());<br>    }<br>}​</code></div>
<div class="ssw-rteStyle-FigureBad">Figure: Bad example - Controller coupled with ExampleService</div>
<div class="ssw-rteStyle-CodeArea" style="height:322px;width:66.86%;"><code>public class HomeController<br>{<br>    private readonly IExampleService _service;<br>     <br>    public HomeController()<br>    {<br>      _service = <span style="background-color:rgb(255,255,0);">Container.Instance.Resolve&lt;IExampleService&gt;();</span><br>    }<br>     <br>    public ActionResult Index()<br>    {<br>        return View(_service.GetSomething());<br>    }<br>} </code></div>
<div class="ssw-rteStyle-FigureBad"><span>Figure: Bad example - 2nd attempt using an Inversion of Control container but *not* using dependency injection. A dependency now exists on the Container.</span></div>
<p>This is bad code because we removed one coupling but added another one (the container).</p>
<div class="ssw-rteStyle-CodeArea" style="width:66.86%;"><code>public class HomeController<br>{<br>    private readonly IExampleService _service;<br>     <br>    public HomeController(<span style="background-color:rgb(255,255,0);">IExampleService service</span>)<br>    {<br>      _service = service;<br>    }<br>     <br>    public ActionResult Index()<br>    {<br>        return View(_service.GetSomething());<br>    }<br>}​</code></div>
<span class="ssw-rteStyle-FigureGood">Figure: Good example - code showing using dependency injection. No static dependencies.</span> <p>Even better, use Annotate so you can enlighten the developer.</p>
<span style="font-size:11pt;font-family:'calibri','sans-serif';color:black;"></span><p><img alt="bad.png" src="Code against interfaces - bad.png" style="margin:5px;" /><br><strong class="ssw-rteStyle-FigureBad">Figure: Bad Example - Referencing the concrete EF context</strong></p>
<p><span><img src="Code against interfaces - good.png" alt="" style="height:328px;margin:5px;width:872px;" /><br><strong class="ssw-rteStyle-FigureGood">Figure: Good Example - Programming against the interface</strong><br></span></p>
<p>It is important to know when the use of a pattern is appropriate.  Patterns can be useful, but they can also be harmful if used incorrectly.</p>


