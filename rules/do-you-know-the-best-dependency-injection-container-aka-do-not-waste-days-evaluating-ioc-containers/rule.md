---
type: rule
title: Do you know the best dependency injection container? (aka Do not waste days evaluating IOC containers)
uri: do-you-know-the-best-dependency-injection-container-aka-do-not-waste-days-evaluating-ioc-containers
created: 2013-02-01T16:43:44.0000000Z
authors:
- id: 24
  title: Adam Stephensen
- id: 1
  title: Adam Cogan
- id: 34
  title: Brendan Richards

---



<span class='intro'> <p>You can waste days evaluating IOC containers. The top ones are quite similar. The best one is StructureMap. </p> 
<p>Other excellent DI containers are AutoFac, Ninject and Castle Winsdor. They have weaknesses, some are listed below. </p> </span>

<p>Dependency Injection is an essential ingredient to having maintainable solutions. IOC containers make doing dependency injection easier.</p><p>When selecting a Dependency Injection container it is worth considering a number of factors such as&#58;</p><ul><li>Ease of use</li><li>Configurability&#58; Fluent API and/or XML Configuration</li><li>Performance (Unless you have a very high traffic application the difference should be minimal)</li></ul><p>The top tools all contain comparable functionality. In practice which one you use makes little difference, especially when you consider that your container choice should not leak into your domain model. </p><p>
   <strong>Important&#58;</strong> Unless a specific shortfall is discovered with the container your team uses, you should continue to use the same container across all of your projects, become an expert with it and invest time on building features rather than learning new container implementations. </p><dl class="badImage"><dt>
      <img src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/ninject.jpg" alt="" />
   </dt><dd>Figure&#58; Bad Example - The Ninject extension packages are not up-to-date. The Ninject.MVC3 package needs to be used for MVC 4 and the Ninject.Web.WebAPI package does not work with the release version of WebApi, so developers must use the Ninject.Web.WebAPI-RC package instead. Also, Ninject doesn’t work in a medium trust environment.</dd></dl><dl class="goodImage"><dt>
      <img src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/frameworks-graphic.jpg" alt="" />
   </dt><dd>Figure&#58; Good Example - StructureMap has better performance than the other top frameworks.<br>

   <ul><li>      <a href="http&#58;//weblogs.asp.net/gunnarpeipman/archive/2010/09/21/unity-castle-windsor-structuremap-ninject-who-has-best-performance.aspx">Unity, Castle Windsor, StructureMap, Ninject – who has best performance?</a> </li><li><a href="http&#58;//www.iocbattle.com/">IoC Battle - .Net Inversion Of Control (IoC) Container Performance Comparison</a> </li><li><a href="http&#58;//www.palmmedia.de/Blog/2011/8/30/ioc-container-benchmark-performance-comparison">IoC Container Benchmark - Performance comparison</a></li> </ul></dd></dl>


