---
type: rule
title: Do you have a consistent .NET Solution Structure?
uri: do-you-have-a-consistent-net-solution-structure
created: 2009-04-24T03:31:54.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 24
  title: Adam Stephensen

---



<span class='intro'> <p>When developing software, we follow a standard solution structure.</p> </span>

<dl class="goodImage"><dt>
      <img class="ms-rteCustom-ImageArea" alt="solutionlayout.png" src="/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/solution-structure.png" />
   </dt><dd>Figure&#58; Good Example - The Solution and Projects are named consistently and follow the Onion Architecture</dd></dl> ​​<span style="line-height&#58;1.6;">D</span><span style="line-height&#58;1.6;">ependencies and the application core are clearly separated as per the 
   </span><a href="/SoftwareDevelopment/RulesToBetterMVC/Pages/Use-a-Dependency-Injection-Centric-Architecture.aspx" style="line-height&#58;1.6;">Onion Architecture</a><span style="line-height&#58;1.6;">.</span><p>In the above example you can clearly see&#58;</p><ul><li>The different layers of the Onion Architecture&#58; see 
      <a href="/SoftwareDevelopment/RulesToBetterMVC/Pages/The-layers-of-the-onion-architecture.aspx">Layers of the Onion Architecture</a></li><li> 
      <a>Unit test and integration test projects&#58; see </a> 
      <a href="http&#58;//www.ssw.com.au/ssw/standards/rules/RulesToBetterUnitTests.aspx">Rules to Better Unit Tests</a></li><li>The Documentation solution folder&#58; see 
      <a href="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/Pages/DoYouReviewTheDocumentation.aspx">Do you review the documentation?</a>​</li><li>The References solution folder&#58; to hold any 3rd party assemblies that are not available via NuGet</li></ul><p>Common Library projects are named 
   <strong>[Company].[AssemblyName]</strong>. E.g. 
   <strong>BCE.Logging</strong> is a shared project between all solutions at company BCE.</p><p>Other projects are named 
   <strong>[Company].[Solution Name].[AssemblyName]</strong>. E.g. 
   <strong>BCE.Sparrow.Business</strong> is the Business layer assembly for company ‘BCE’, solution ‘Sparrow’.</p><p>We have separated the unit tests, one for each project, for several reasons&#58;</p><ul><li>It provides a clear separation of concerns and allows each component to be individually tested</li><li>The different libraries can be used on other projects with confidence as there are a set of tests around them</li></ul>


