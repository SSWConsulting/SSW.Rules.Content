---
type: rule
title: "Method #1 - Using Project Reference Assemblies within VS.NET"
uri: method-1-using-project-reference-assemblies-within-vsnet
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T05:53:00.000Z
guid: 061c1865-2110-4f4a-bbac-37a5e0c361fd
---
The first attempt was the following method of adding project references to a large solution.

<!--endintro-->

![Figure: Adding a project reference](betterlargedotnet_projref.gif)

Each project within a solution references other product's assemblies by the project's GUID.

**Advantages**

The advantages of adding the project to the solution is that you can easily switch between debug and release versions, and the build time is quicker.

**Disadvantages**

The main disadvantage is that the project can only reference other projects within the same solution.
