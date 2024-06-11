---
seoDescription: Understand the fundamentals of software design by learning the five SOLID principles - Single Responsibility Principle, Open-Closed Principle, Liskov Substitution Principle, Interface Segregation Principle, and Dependency Inversion Principle.
type: rule
archivedreason:
title: Do you know the common Design Principles? (Part 1)
guid: 7507df2f-e227-4ecf-931f-4864ad85eb02
uri: do-you-know-the-common-design-principles-part-1
created: 2012-04-02T00:29:11.0000000Z
authors:
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
related: []
redirects:
  - do-you-know-the-common-design-principles-(part-1)
---

::: greybox

**SRP The Single Responsibility Principle**
A class should have one, and only one reason to change.

**OCP The Open Closed Principle
** You should be able to extend a class's behavior without modifying it.

**LSP The Liskov Substitution Principle
** Derived classes must be substitutable for their base classes.

**ISP The Interface Segregation Principle
** Make fine-grained interfaces that are client specific.

**DIP The Dependency Inversion Principle
** Depend on abstractions, not on concretions.

:::

::: good
Figure: Your code should be using [SOLID principles](https://en.wikipedia.org/wiki/SOLID_%28object-oriented_design%29)

:::

<!--endintro-->

It is assumed knowledge that you know all 5 SOLID principles. If you don't, read about them on Uncle Bob's site above, or watch the [SOLID Pluralsight videos by Steve Smith.](https://www.youtube.com/watch?v=KN2svY2nabU)

### What order?

1. Look for Single Responsibility Principle violations. These are the most common and are the source of many other issues. Reducing the size and complexity of your classes and methods will often resolve other problems.
2. Liskov Substitution and Dependency Inversion are the next most common violations, so keep an eye out for them next
3. When teams first begin implementing Dependency Injection, it is common for them to generate bloated interfaces that violate the Interface Segregation Principle.

After you have identified and corrected the most obvious broad principle violations, you can start drilling into the code and looking for localized code breaches. [ReSharper](http://www.jetbrains.com/resharper/) from JetBrains or [JustCode](http://www.telerik.com/products/justcode.aspx) from Telerik are invaluable tools once you get to this level.

Once you understand common design principles, look at [common design patterns](/do-you-know-the-common-design-patterns-part-1) to help you follow them in your projects.
