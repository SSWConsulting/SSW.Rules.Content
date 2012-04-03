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



<span class='intro'> <p>Visual Studio has architecture tools that let you analyse the solution structure. While these can be useful, they're not as good as nDepend at highlighting areas that should be looked at.</p>
<p>nDepend is a great tool for analysing the dependencies between classes and assemblies in your projects.&#160; It can find issues and highlights them in red for easy discovery.</p> </span>

<p><img alt="architecturetools_vs11.png" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/ArchitectureToolsVS11.png" style="margin&#58;5px;" /><br><span class="ssw-rteStyle-FigureNormal">Figure&#58; VS11 lets you generate a dependency graph for your solution.</span><img alt="sqldeploy_dependencies.png" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/DependencyDiagramInVS11.png" style="margin&#58;5px;width&#58;600px;height&#58;243px;" /><br><span class="ssw-rteStyle-FigureNormal">Figure&#58; The dependency graph in VS11 shows you some interesting information, but it's not as good as nDepends at highlighting issues</span></p>
<div><span>nDepend is much better at showing you where your code architecture needs some work.</span></div>
<p><img alt="nDepend.png" src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/nDependDependencyGraph.png" style="margin&#58;5px;width&#58;600px;height&#58;370px;" /><br><span class="ssw-rteStyle-FigureNormal">Figure：ndepend Dependency Graph. Issues are highlighted in red for easy </span><span class="ssw-rteStyle-FigureNormal">discovery.</span><span>Read</span><span> more about nDepend&#58; <a href="http&#58;//www.ndepend.com/"><font color="#3a66cc">http&#58;//www.ndepend.com/</font></a></span></p>
<div class="ssw-rteStyle-Tip"><span></span><span>Warning&#58; nDepend doesn't yet support Visual Studio 2012 (AKA VS11) with a plugin.</span></div>


