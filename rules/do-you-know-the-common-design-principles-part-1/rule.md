---
type: rule
title: Do you know the common Design Principles? (Part 1)
uri: do-you-know-the-common-design-principles-part-1
created: 2012-04-02T00:29:11.0000000Z
authors:
- id: 24
  title: Adam Stephensen
- id: 23
  title: Damian Brady

---



<span class='intro'> <div class="greyBox"><p>
      <b>SRP&#160;The Single Responsibility Principle</b><br>A class should have one, and only one&#160;reason&#160;to change.</p><p><b>OCP The Open&#160;Closed&#160;Principle&#160;<br></b>You should be able to extend a class's&#160;behavior&#160;without modifying it.</p><p><b>LSP The Liskov&#160;Substitution&#160;Principle&#160;<br></b>Derived classes must be substitutable for their base classes.</p><p><b>ISP The Interface&#160;Seg regation&#160;Principle&#160;<br></b>Make fine-grained interfaces that are client specific.</p><p><b>DIP The Dependency Inversion Principle&#160;<br></b>Depend on abstractions, not on concretions.<br></p></div><dd class="ssw15-rteElement-FigureGood"> Figure&#58; Your code should be using 
   <a href="https&#58;//en.wikipedia.org/wiki/SOLID_%28object-oriented_design%29">SOLID principles​​</a>​<br></dd> </span>

<p>It is assumed knowledge that you know all 5 SOLID principles. If you don't, read about them on Uncle Bob's site above, or watch the <a href="http&#58;//www.pluralsight-training.net/microsoft/courses/TableOfContents?courseName=principles-oo-design&amp;highlight=">SOLID Pluralsight videos by Steve Smith.</a></p>
<h3 class="ssw15-rteElement-H3">What order?</h3>
<ol>
<li>Look for Single Responsibility&#160;Principle violations. These are the most common and are the source of many other issues. Reducing the size and complexity of your classes and methods will often resolve other problems.</li>
<li>Liskov Substitution and Dependency Inversion are the next most common violations, so keep an eye out for them next.</li>
<li>When teams first begin implementing Dependency Injection, it is common for them to generate bloated interfaces that violate the Interface Segregation Principle.<br></li>
</ol>
<p>After you have identified and corrected the most obvious broad principle violations, you can start drilling into the code&#160;and looking for&#160;localized code breaches. <a href="http&#58;//www.jetbrains.com/resharper/">ReSharper</a> from JetBrains o​r&#160;<a href="http&#58;//www.telerik.com/products/justcode.aspx">JustCode</a> from Telerik&#160;are invaluable tools once you get to this level.</p>
<p>Once you understand common design principles, look at <a href="/Pages/DoYouKnowCommonDesignPatterns.aspx">common design patterns</a> to help you follow them in your projects.</p>


