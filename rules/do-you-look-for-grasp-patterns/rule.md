---
type: rule
archivedreason: 
title: Do you look for GRASP Patterns?
guid: 206d32a0-1510-4f93-b4c5-9fc2ae6068c0
uri: do-you-look-for-grasp-patterns
created: 2012-04-01T09:35:53.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related:
- do-you-look-at-the-architecture
redirects: []

---


<p><span lang="EN-AU">GRASP stands for General Responsibility Assignment Software Patterns and describes guidelines for working out what objects are responsible for what areas of the application.</span></p>
<br><excerpt class='endintro'></excerpt><br>
<p>​The fundamentals of GRASP are the building blocks of Object-​Oriented design.  It is important that responsibilities in your application are assigned predictably and sensibly to achieve maximum extensibility and maintainability.</p>
<p>GRASP consists of a set of patterns and principles that describe different ways of constructing relationships between classes and objects.</p>
<table cellpadding="4" border="1" style="border-collapse:collapse;">
<tbody><tr><th>Creator</th>
<td>A specific class is responsible for creating instances of specific other classes (e.g. a Factory Pattern)</td></tr>
<tr><th>​Information Expert</th>
<td>Responsibilities are delegated to the class that holds the information required to handle that responsibility​</td></tr>
<tr><th>​Controller</th>
<td>​System events are handled by a single "controller" class that delegates to other objects the work that needs to be done</td></tr>
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
<tr><th style="padding-right:10px;">​Protected Variations</th>
<td>​Variations in the behaviour of other objects is abstracted away from the dependent object by means of an interface and polymorphism</td></tr></tbody></table>
<p>Tip: Visual Studio's Architecture tools can help you visualise your dependencies.  A good structure will show calls flowing in one direction.</p>
<img alt="architecture_responsibility_bad.png" src="architecture_responsibility_bad.png" class="ms-rteCustom-ImageArea" />
<span class="ssw-rteStyle-FigureBad">Figure: Bad Example - Calls are going in both directions which hints at a poor architecture</span>
<img class="ms-rteCustom-ImageArea" alt="architecture_responsibility_good.png" src="architecture_responsibility_good.png" />
<span class="ssw-rteStyle-FigureGood">Figure: Good Example - Calls are flowing in one direction hinting at a more sensible arrangement of responsibilities</span>


