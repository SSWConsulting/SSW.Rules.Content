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

To visualize the structure of all your code you need architecture tools that will analyze your whole solution.

They show the dependencies between classes and assemblies in your projects. You have 2 choices:

* Visual Studio's Dependency Graph. This feature is only available in Visual Studio Ultimate. (recommended)
* If you want architecture tools for Visual Studio, but don't have Visual Studio Ultimate, then the excellent 3rd party solution nDepend. A bonus is that it can also find issues and highlights them in red for easy discovery


<!--endintro-->
<dl class="image">&lt;dt&gt;<img src="ArchitectureToolsVS11.png" alt="architecturetools_vs11.png">&lt;/dt&gt;<dd>Figure: Visual Studio lets you generate a dependency graph for your solution</dd></dl><dl class="image">&lt;dt&gt;<img src="DependencyDiagramInVS11.png" alt="sqldeploy_dependencies.png" style="width:600px;"> &lt;/dt&gt;<dd>Figure: The dependency graph in Visual Studio shows you some interesting information about how projects relate to each other<br></dd></dl>
nDepend has a similar diagram that is a little messier, but the latest version also includes a "Queries + Rules Explorer" which is another code analysis tool.
<dl class="image">&lt;dt&gt;<img class="ms-rteCustom-ImageArea" src="nDependDependencyGraph.png" alt="nDepend.png" style="width:600px;"> &lt;/dt&gt;<dd>Figure: nDepend Dependency Graph. Issues are highlighted in red for easy discovery</dd></dl>
Read more about nDepend: [ndepend.com](http://www.ndepend.com/).

### Related Rule


* [Do you look at the architecture of JavaScript projects?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=5ecac864-c6b1-4187-8382-e2936ee3641f)
