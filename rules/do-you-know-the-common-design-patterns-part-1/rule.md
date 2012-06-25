---
type: rule
title: Do you know the common Design Patterns? (Part 1)
uri: do-you-know-the-common-design-patterns-part-1
created: 2012-04-02T04:44:06.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 24
  title: Adam Stephensen
- id: 23
  title: Damian Brady

---



<span class='intro'> <p>Design patterns are useful for ensuring <a href="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/Pages/DoYouKnowCommonDesignPrinciples.aspx">common design principles </a>are being followed.&#160; They help make your code consistent, predictable,&#160;and easy to maintain.</p> </span>

<p>​There are a very large number of Design Patterns, but here are a few important ones.</p>
<table width="100%" cellpadding="4" border="1" class="ssw-rteTable-default" style="border-width&#58;1px;border-style&#58;solid;"><tbody><tr class="ssw-rteTableEvenRow-default">
<th class="ssw-rteTableFirstCol-default">​IOC</th>
<td class="ssw-rteTableOddCol-default"><a href="http&#58;//en.wikipedia.org/wiki/Inversion_of_control">​Inversion of Control</a></td>
<td class="ssw-rteTableEvenCol-default">Control of the object coupling is the responsibility of the caller, not the class.</td></tr>
<tr class="ssw-rteTableOddRow-default"><th class="ssw-rteTableFirstCol-default">​DI</th>
<td class="ssw-rteTableOddCol-default">​<a href="http&#58;//en.wikipedia.org/wiki/Dependency_injection">Dependency Injection</a></td>
<td class="ssw-rteTableEvenCol-default">Dependencies are &quot;injected&quot; into the dependent object rather than the object depending on concretions.</td></tr>
<tr class="ssw-rteTableEvenRow-default"><th class="ssw-rteTableFirstCol-default">​Factory</th>
<td class="ssw-rteTableOddCol-default"><a href="http&#58;//en.wikipedia.org/wiki/Factory_pattern">​Factory Pattern</a></td>
<td class="ssw-rteTableEvenCol-default">​Object creation is handled by a &quot;factory&quot; that can provide different concretions based on an abstraction.</td></tr>
<tr class="ssw-rteTableOddRow-default"><th class="ssw-rteTableFirstCol-default">​Singleton</th>
<td class="ssw-rteTableOddCol-default"><a href="http&#58;//en.wikipedia.org/wiki/Singleton_pattern">​Singleton Pattern</a></td>
<td class="ssw-rteTableEvenCol-default">​Instantiation of an object is limited to one instance to be shared across the system.</td></tr>
<tr class="ssw-rteTableEvenRow-default"><th class="ssw-rteTableFirstCol-default">​Repository</th>
<td class="ssw-rteTableOddCol-default"><a href="http&#58;//msdn.microsoft.com/en-us/library/ff649690.aspx">​Repository Pattern</a></td>
<td class="ssw-rteTableEvenCol-default">​A repository is used to handle the data mapping details of CRUD operations on domain objects.</td></tr>
<tr class="ssw-rteTableOddRow-default"><th class="ssw-rteTableFirstCol-default">​Unit of Work</th>
<td class="ssw-rteTableOddCol-default"><a href="http&#58;//msdn.microsoft.com/en-us/magazine/dd882510.aspx">​Unit of Work Pattern</a></td>
<td class="ssw-rteTableEvenCol-default">​A way of handling multiple database operations that need to be done as part of a piece of work.</td></tr>
<tr class="ssw-rteTableEvenRow-default"><th class="ssw-rteTableFirstCol-default">​MVC</th>
<td class="ssw-rteTableOddCol-default"><a href="http&#58;//en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller">​Model View Controller</a></td>
<td class="ssw-rteTableEvenCol-default">​An architectural pattern separating domain logic (Controller) from&#160;how domain objects (Models) are presented (View).</td></tr>
<tr class="ssw-rteTableOddRow-default"><th class="ssw-rteTableFirstCol-default">​MVP</th>
<td class="ssw-rteTableOddCol-default"><a href="http&#58;//en.wikipedia.org/wiki/Model_View_Presenter">​Model View Presenter</a></td>
<td class="ssw-rteTableEvenCol-default">​An architectural pattern deriving from MVC where the View handles UI events instead of the Controller.</td></tr></tbody></table>
<span class="ssw-rteStyle-FigureNormal">Figure&#58; Choose patterns wisely to improve your solution architecture</span>
<p>It is assumed knowledge that you know these design patterns. If you don't, read about them on the sites above or watch the <a href="http&#58;//www.pluralsight-training.net/microsoft/courses/TableOfContents?courseName=patterns-library">PluralSight videos on Software Patterns.</a></p>


