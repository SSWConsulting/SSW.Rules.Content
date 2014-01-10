---
type: rule
title: Do you generate the VS Dependency Graph?
uri: do-you-generate-the-vs-dependency-graph
created: 2012-03-16T08:04:49.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 24
  title: Adam Stephensen
- id: 40
  title: Igor Goldobin

---



<span class='intro'> <p>Dependency graphs are important because they give you an indication of the coupling between the different components within your application.</p><p>
A well architected application (ie. one that correctly follows the Onion Architecture) will be easy to maintain because it is loosely coupled.</p>
 </span>

​ 
<dl class="badImage"><dt> 
      <img src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/TimePRODependence.png" class="ssw-rteStyle-ImageArea" alt="" style="height&#58;119px;width&#58;620px;" /> 
   </dt><dd>Figure&#58; Bad Example- The Visual Studio Dependency Graph is hard to read</dd></dl> ​ 
<dl class="goodImage"><dt> 
      <img src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/TimePRODependence-good.png" class="ssw-rteStyle-ImageArea" alt="TimePRODependence-good.png" /> 
   </dt><dd>Figure&#58; Good Example – The ReSharper Dependency graph groups dependencies based on Solution Folders. By having a 
      <a href="/SoftwareDevelopment/RulesToBetterDotNETProjects/Pages/SolutionStructure.aspx">Consistent Solution Structure</a> it is easy to see from your Dependency Graph if there is coupling between your UI and your Dependencies</dd></dl>​


