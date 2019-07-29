---
type: rule
title: Do you look at the architecture?
uri: do-you-look-at-the-architecture
created: 2012-03-16T08:33:48.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 23
  title: Damian Brady
- id: 3
  title: Eric Phan

---



<span class='intro'> <p>To visualize the structure of all your code you need architecture tools that will analyse your whole solution.<br></p>
<p>They show the dependencies between classes and assemblies in your projects.&#160;You have 2 choices&#58;</p>
<ul>
<li>Visual Studio's Dependency Graph. This feature is only available in Visual Studio Ultimate. (recommended)</li>
<li>If you want architecture tools for Visual Studio, but don't have Visual Studio Ultimate, then the excellent 3rd party solution nDepend. A bonus is that it can also find issues and highlights them in red for easy discovery<br></li>
</ul>
 </span>

<dl class="image"><dt><img src="/PublishingImages/ArchitectureToolsVS11.png" alt="architecturetools_vs11.png" /></dt><dd>Figure&#58; Visual Studio lets you generate a dependency graph for your solution</dd></dl><dl class="image"><dt><img src="/PublishingImages/DependencyDiagramInVS11.png" alt="sqldeploy_dependencies.png" style="width&#58;600px;" /> </dt><dd>Figure&#58; The dependency graph in Visual Studio&#160;shows you some interesting information about how projects relate to each other​<br></dd></dl><p>nDepend has a similar diagram that is a little messier, but the latest version also includes a &quot;Queries + Rules Explorer&quot; which is another code analysis tool.<br></p><dl class="image"><dt><img class="ms-rteCustom-ImageArea" src="/PublishingImages/nDependDependencyGraph.png" alt="nDepend.png" style="width&#58;600px;" />​ </dt><dd>Figure&#58; nDepend Dependency Graph. Issues are highlighted in red for easy discovery</dd></dl><p>Read more about nDepend&#58; <a href="http&#58;//www.ndepend.com/">ndepend.com</a>.</p>


