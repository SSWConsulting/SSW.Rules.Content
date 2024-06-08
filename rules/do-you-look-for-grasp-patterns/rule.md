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

GRASP stands for General Responsibility Assignment Software Patterns and describes guidelines for working out what objects are responsible for what areas of the application.

<!--endintro-->

The fundamentals of GRASP are the building blocks of Object-Oriented design.  It is important that responsibilities in your application are assigned predictably and sensibly to achieve maximum extensibility and maintainability.

GRASP consists of a set of patterns and principles that describe different ways of constructing relationships between classes and objects.


| Creator | A specific class is responsible for creating instances of specific other classes (e.g. a Factory Pattern) |
| --- | --- |
| Information Expert | Responsibilities are delegated to the class that holds the information required to handle that responsibility |
| --- | --- |
| Controller | System events are handled by a single "controller" class that delegates to other objects the work that needs to be done |
| --- | --- |
| Low Coupling  | Classes should have a low dependency on each other, have low impact if changed, and have high potential for reuse |
| --- | --- |
| High Cohesion | Objects should be created for a single set of focused responsibilities |
| --- | --- |
| Polymorphism | The variation in behaviour of a type of object is the responsibility of that type's implementation |
| --- | --- |
| Pure Fabrication | Any class that does not represent a concept in the problem domain |
| --- | --- |
| Indirection | The responsibility of mediation between two classes is handled by an intermediate object (e.g. a Controller in the MVC pattern) |
| --- | --- |
| Protected Variations | Variations in the behaviour of other objects is abstracted away from the dependent object by means of an interface and polymorphism |
| --- | --- |


Tip: Visual Studio's Architecture tools can help you visualise your dependencies.  A good structure will show calls flowing in one direction.
![](architecture_responsibility_bad.png)Figure: Bad Example - Calls are going in both directions which hints at a poor architecture![](architecture_responsibility_good.png)Figure: Good Example - Calls are flowing in one direction hinting at a more sensible arrangement of responsibilities
