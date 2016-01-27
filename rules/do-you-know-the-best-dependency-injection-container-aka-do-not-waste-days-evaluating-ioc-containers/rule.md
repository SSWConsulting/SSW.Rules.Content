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



<span class='intro'> <p>​​​You can waste days evaluating IOC containers. The top ones are quite similar. There is not much in this, but the best ones are StructureMap and AutoFac. At SSW we use Autofac&#160;on most projects.</p><p>Other excellent DI containers are StructureMap, Ninject and Castle Winsdor. They have weaknesses, some are listed below. </p> </span>

<p>Dependency Injection is an essential ingredient to having maintainable solutions. IOC containers make doing dependency injection easier.</p><p>When selecting a Dependency Injection container it is worth considering a number of factors such as&#58;</p><ul><li>Ease of use</li><li>Configurability&#58; Fluent API and/or XML Configuration</li><li>Performance (Unless you have a very high traffic application the difference should be minimal)</li><li>NuGet Support (only Ninject is doing a poor job of this) - see image</li></ul><p>The top tools all contain comparable functionality. In practice which one you use makes little difference, especially when you consider that your container choice should not leak into your domain model. </p><p> 
   <strong>Important&#58;</strong> Unless a specific shortfall is discovered with the container your team uses, you should continue to use the same container across all of your projects, become an expert with it and invest time on building features rather than learning new container implementations. </p><dl class="badImage"><dt> 
      <img src="/PublishingImages/ninject.jpg" alt="" /> 
   </dt><dd>Figure&#58; Bad Example - The Ninject extension packages are not up-to-date. The Ninject.MVC3 package needs to be used for MVC 4 and the Ninject.Web.WebAPI package does not work with the release version of WebApi, so developers must use the Ninject.Web.WebAPI-RC package instead. Also, Ninject doesn’t work in a medium trust environment.</dd></dl><dl class="goodImage"><dt> 
      ​​<img src="http&#58;//www.palmmedia.de/content/blogimages/67b056a5-9da8-40b4-9ae6-0c838cdac180.png" alt="IOC Container Performance" style="margin&#58;5px;width&#58;650px;" /> 
   </dt><dd>Figure&#58; Good Example - Autofac has a good combination of performance and features as per&#160;<a href="http&#58;//www.palmmedia.de/blog/2011/8/30/ioc-container-benchmark-performance-comparison">http&#58;//www.palmmedia.de/blog/2011/8/30/ioc-container-benchmark-performance-comparison​​​</a></dd></dl><p> 
   <strong>Note&#58;</strong> Autofac's support for child lifetime containers maybe significant for some&#58;​<br><a href="http&#58;//nblumhardt.com/2011/01/an-autofac-lifetime-primer/" target="_blank">​http&#58;//nblumhardt.com/2011/01/an-autofac-lifetime-primer</a></p><p>StructureMap does also support a kind of child container&#58;<br><a href="http&#58;//codebetter.com/jeremymiller/2010/02/10/nested-containers-in-structuremap-2-6-1/" target="_blank">http&#58;//codebetter.com/jeremymiller/2010/02/10/nested-containers-in-structuremap-2-6-1/</a> </p><p>​<img src="/PublishingImages/Autofac_web.png" alt="Autofac_web.png" style="margin&#58;5px;width&#58;650px;" /><br></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example - the web / mvc&#160;integration package&#160;layer for Autofac is developed by the same core Autofac team.&#160;Some containers (such as Structure Map) requre third-party integration layers​​&#160;​<br></dd><p><br></p><h4>Further Reading&#58;​</h4><ul><li><a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=0a5029a1-dd4f-46d7-9f22-8ab328e7c102">Do you use a dependency injection centric architecture?</a></li><li>
      <a href="/Pages/DoYouGenerateTheVSDependencyGraph.aspx">​Do you generate the VS dependency graph?</a>​</li></ul>


