---
type: rule
archivedreason: 
title: Do you look at the architecture of .NET projects?
guid: 94c385c2-98fd-46a0-acd1-b50070ee03ee
uri: do-you-look-at-the-architecture-of-net-projects
created: 2012-03-16T08:33:48.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 23
  title: Damian Brady
- id: 3
  title: Eric Phan
related:
- do-you-look-for-grasp-patterns

---


<p>​To visualize the structure of all your code you need architecture tools that will analyze your whole solution.<br></p>
<p>They show the dependencies between classes and assemblies in your projects. You have 2 choices:</p>
<ul>
<li>Visual Studio's Dependency Graph. This feature is only available in Visual Studio Ultimate. (recommended)</li>
<li>If you want architecture tools for Visual Studio, but don't have Visual Studio Ultimate, then the excellent 3rd party solution nDepend. A bonus is that it can also find issues and highlights them in red for easy discovery<br></li>
</ul>

<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt><img src="ArchitectureToolsVS11.png" alt="architecturetools_vs11.png" /></dt><dd>Figure: Visual Studio lets you generate a dependency graph for your solution</dd></dl><dl class="image"><dt><img src="DependencyDiagramInVS11.png" alt="sqldeploy_dependencies.png" style="width:600px;" /> </dt><dd>Figure: The dependency graph in Visual Studio shows you some interesting information about how projects relate to each other​<br></dd></dl><p>nDepend has a similar diagram that is a little messier, but the latest version also includes a "Queries + Rules Explorer" which is another code analysis tool.<br></p><dl class="image"><dt><img class="ms-rteCustom-ImageArea" src="nDependDependencyGraph.png" alt="nDepend.png" style="width:600px;" />​ </dt><dd>Figure: nDepend Dependency Graph. Issues are highlighted in red for easy discovery</dd></dl><p>Read more about nDepend: <a href="http://www.ndepend.com/">ndepend.com</a>.<br></p><h3 class="ssw15-rteElement-H3">Related Rule​​<br></h3><ul><li>​<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=5ecac864-c6b1-4187-8382-e2936ee3641f">Do you look at the architecture of JavaScript projects?</a>​<br></li></ul>


