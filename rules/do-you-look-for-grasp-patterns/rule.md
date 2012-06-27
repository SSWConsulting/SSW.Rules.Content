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

<p>​The fundamentals of GRASP are the building blocks of Object Oriented design.&#160; It is important that responsibilities in your application are assigned predictably and sensibly to achieve maximum extensibility and maintainability.</p>
<p>GRASP consists of a set of&#160;patterns and principles that describe different ways of constructing relationships between classes and objects.</p>
<table cellpadding="4" border="1" style="border-collapse&#58;collapse;">
<tbody><tr><th>Creator</th>
<td>A specific class is responsible for creating instances of specific other classes (e.g. a Factory Pattern)</td></tr>
<tr><th>​Information Expert</th>
<td>Responsibilities are delegated to the class that holds the information required to handle that responsibility​</td></tr>
<tr><th>​Controller</th>
<td>​System events are handled by a single &quot;controller&quot; class that delegates to other objects the work that needs to be done</td></tr>
<tr><th>​Low Coupling </th>
<td>Classes should have a low dependency on each other, have low impact if changed, and ​have high potential for reuse</td></tr>
<tr><th>​High Cohesion</th>
<td>​Objects should be created for a single set of focused responsibilities</td></tr>
<tr><th>​Polymorphism</th>
<td>​The variation in behaviour of a type of object is the responsibility of that type's implementation</td></tr>
<tr><th>​Pure Fabrication</th>
<td>​Any class that does not represent a concept in the problem domain</td></tr>
<tr><th>​Indirection</th>
<td>​The responsibility of mediation between two classes is handled by an intermediate object (e.g. a Controller in the MVC pattern)</td></tr>
<tr><th style="padding-right&#58;10px;">​Protected Variations</th>
<td>​Variations in the behaviour of other objects is abstracted away from the dependent object by means of an interface and polymorphism</td></tr></tbody></table>
<p>Tip&#58; Visual Studio's Architecture tools can help you visualise your dependencies.&#160; A good structure will show calls flowing in one direction.</p>
<img alt="architecture_responsibility_bad.png" src="/PublishingImages/architecture_responsibility_bad.png" class="ms-rteCustom-ImageArea" />
<span class="ssw-rteStyle-FigureBad">Figure&#58; Bad Example - Calls are going in both directions which hints at a poor architecture</span>
<img class="ms-rteCustom-ImageArea" alt="architecture_responsibility_good.png" src="/PublishingImages/architecture_responsibility_good.png" />
<span class="ssw-rteStyle-FigureGood">Figure&#58; Good Example -&#160;Calls&#160;are flowing in one direction hinting at a more sensible&#160;arrangement of responsibilities</span>


