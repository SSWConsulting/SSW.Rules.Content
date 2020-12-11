---
type: rule
archivedreason: 
title: Do you know the best dependency injection container? (aka Do not waste days evaluating IOC containers)
guid: d4fc76e9-0802-48bd-83d7-4e068a19d33b
uri: do-you-know-the-best-dependency-injection-container-aka-do-not-waste-days-evaluating-ioc-containers
created: 2013-02-01T16:43:44.0000000Z
authors:
- id: 24
  title: Adam Stephensen
- id: 1
  title: Adam Cogan
- id: 34
  title: Brendan Richards
related: []

---


<p>​You can waste days evaluating IOC containers. The top ones are quite similar. There is not much in this, but the best ones are StructureMap and AutoFac. At SSW we use Autofac on most projects.<br></p><p>Other excellent DI containers are Ninject and Castle Winsdor. They have weaknesses, some are listed below.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>Dependency Injection is an essential ingredient to having maintainable solutions. IOC containers make doing dependency injection easier.</p><p>When selecting a Dependency Injection container it is worth considering a number of factors such as:</p><ul><li>Ease of use</li><li>Configurability: Fluent API and/or XML Configuration</li><li>Performance (Unless you have a very high traffic application the difference should be minimal)<br></li><li>NuGet Support (only Ninject is doing a poor job of this) - see image</li></ul><p>The top tools all contain comparable functionality. In practice which one you use makes little difference, especially when you consider that your container choice should not leak into your domain model.</p><p>
   <strong>Important:</strong> Unless a specific shortfall is discovered with the container your team uses, you should continue to use the same container across all of your projects, become an expert with it and invest time on building features rather than learning new container implementations.<br></p><dl class="badImage"><dt><img src="dic-bad.png" alt="dic-bad.png" /> <br></dt><dd>Figure: Bad Example - Ninject was a top container but is no longer developed as actively as Autofac and Structuremap. Both Autofac and Structuremap have active communities and contributors that ensure they stay up to date with the latest changes in .Net<br></dd></dl><dl class="goodImage"><dt> <img src="dic-good.png" alt="dic-good.png alt=" /> </dt><dd>Figure: Good Example - <strong>Autofac has a great combination of performance and features and is actively developed</strong> </dd></dl><p>
   <strong>Note:</strong> Autofac's support for child lifetime containers may be  significant for some: <br>
   <a href="http://nblumhardt.com/2011/01/an-autofac-lifetime-primer/" target="_blank"> http://nblumhardt.com/2011/01/an-autofac-lifetime-primer</a></p><p>StructureMap does also support a kind of child container:<br><a href="http://codebetter.com/jeremymiller/2010/02/10/nested-containers-in-structuremap-2-6-1/" target="_blank">http://codebetter.com/jeremymiller/2010/02/10/nested-containers-in-structuremap-2-6-1/</a> </p><p>​<img src="Autofac_web.png" alt="Autofac_web.png" style="margin:5px;width:650px;" /><br></p><dd class="ssw15-rteElement-FigureGood">Figure: Good Example - the web / mvc integration package layer for Autofac is developed by the same core Autofac team. Some containers (such as Structure Map) require third-party integration layers   <br>​</dd><h3 class="ssw15-rteElement-H3">Further Reading:​​<br></h3><ul><li>
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=0a5029a1-dd4f-46d7-9f22-8ab328e7c102">Do you use a dependency injection centric architecture?</a></li><li> 
      <a href="/Pages/DoYouGenerateTheVSDependencyGraph.aspx"> Do you generate the VS dependency graph?</a>  </li><li>
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=c9398fcf-0c43-4f22-8819-f324c4ecb1a8">Do you know what to do about ASP.NET Core default dependency injection? </a></li></ul>


