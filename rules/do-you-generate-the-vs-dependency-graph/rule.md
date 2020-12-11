---
type: rule
archivedreason: 
title: Do you generate the VS Dependency Graph?
guid: 726eadfd-fa6c-4549-acfd-bc9e30e378fe
uri: do-you-generate-the-vs-dependency-graph
created: 2012-03-16T08:04:49.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 24
  title: Adam Stephensen
- id: 40
  title: Igor Goldobin
related: []

---

Dependency graphs are important because they give you an indication of the coupling between the different components within your application.

A well architected application (ie. one that correctly follows the Onion Architecture) will be easy to maintain because it is loosely coupled.

<!--endintro-->
<dl class="badImage">&lt;dt&gt; 
      <img src="TimePRODependence.png" class="ssw-rteStyle-ImageArea" alt="" style="height:119px;width:620px;"> 
   &lt;/dt&gt;<dd>Figure: Bad Example- The Visual Studio Dependency Graph is hard to read</dd></dl><dl class="goodImage">&lt;dt&gt; 
      <img src="TimePRODependence-good.png" class="ssw-rteStyle-ImageArea" alt="TimePRODependence-good.png"> 
   &lt;/dt&gt;<dd>Figure: Good Example – The ReSharper Dependency graph groups dependencies based on Solution Folders. By having a 
      <a href="/do-you-have-a-consistent-net-solution-structure">Consistent Solution Structure</a> it is easy to see from your Dependency Graph if there is coupling between your UI and your Dependencies</dd></dl>
#### Further Reading:

* [Do you use a dependency injection centric architecture?](/do-you-use-a-dependency-injection-centric-architecture)
* [Do you know the best dependency injection container?](/Pages/Do-You-Know-the-Best-Dependency-Injection-Container.aspx)
