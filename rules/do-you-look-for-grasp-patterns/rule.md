---
type: rule
title: Do you look for GRASP Patterns?
uri: do-you-look-for-grasp-patterns
created: 2012-04-01T09:35:53.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 23
  title: Damian Brady

---



<span class='intro'> <p><span lang="EN-AU">GRASP stands for General Responsibility Assignment Software Patterns and describes guidelines for working out what objects are responsible for what areas of the application.</span></p> </span>

<p>​The fundamentals of GRASP are the <span lang="EN-AU">building blocks of Object Oriented design.&#160; It is important that r<span lang="EN-AU">esponsibilities in your application are assigned predictably and sensibly to achieve maximum extensibility and maintainability.</span></span></p>
<p><span lang="EN-AU">GRASP consists of a set of&#160;patterns and principles that describe different ways of constructing relationships between classes and objects.</span></p>
<p><span lang="EN-AU"></span></p>
<table style="border-width&#58;1px;border-style&#58;solid;border-color&#58;rgb(68, 68, 68);"><tbody><tr><th style="padding-right&#58;10px;">Creator</th>
<td>A specific class is responsible for creating instances of specific other classes (e.g. a Factory Pattern)</td></tr>
<tr><th style="padding-right&#58;10px;">​Information Expert</th>
<td>Responsibilities are delegated to the class that holds the information required to handle that responsibility​</td></tr>
<tr><th style="padding-right&#58;10px;">​Controller</th>
<td>​System events are handled by a single &quot;controller&quot; class that delegates to other objects the work that needs to be done</td></tr>
<tr><th style="padding-right&#58;10px;">​Low Coupling </th>
<td>Classes should have a low dependency on each other, have low impact if changed, and ​have high potential for reuse</td></tr>
<tr><th style="padding-right&#58;10px;">​High Cohesion</th>
<td>​Objects should be created for a single set of focused responsibilities</td></tr>
<tr><th style="padding-right&#58;10px;">​Polymorphism</th>
<td>​The variation in behaviour of a type of object is the responsibility of that type's implementation</td></tr>
<tr><th style="padding-right&#58;10px;">​Pure Fabrication</th>
<td>​Any class that does not represent a concept in the problem domain</td></tr>
<tr><th>​Indirection</th>
<td>​The responsibility of mediation between two classes is handled by an intermediate object (e.g. a Controller in the MVC pattern)</td></tr>
<tr><th style="padding-right&#58;10px;">​Protected Variations</th>
<td>​Variations in the behaviour of other objects is abstracted away from the dependent object by means of an interface and polymorphism</td></tr></tbody></table>
<p></p>
<p>Tip&#58; Visual Studio's Architecture tools can help you visualise your dependencies.&#160; A good structure will show calls flowing in one direction.</p>
<p><img src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/architecture_responsibility_bad.png" alt="architecture_responsibility_bad.png" style="margin&#58;5px;" /><br><span class="ssw-rteStyle-FigureBad">Figure&#58; Bad Example - Calls are going in both directions which hints at a poor architecture</span><img src="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/PublishingImages/architecture_responsibility_good.png" alt="architecture_responsibility_good.png" style="margin&#58;5px;" /><br><span class="ssw-rteStyle-FigureGood">Figure&#58; Good Example -&#160;Calls&#160;are flowing in one direction hinting at a more sensible&#160;arrangement of responsibilities</span></p>


