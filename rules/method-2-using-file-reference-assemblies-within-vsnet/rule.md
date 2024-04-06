---
type: rule
title: "Method #2 - Using File Reference Assemblies within VS.NET"
uri: method-2-using-file-reference-assemblies-within-vsnet
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T05:53:00.000Z
guid: 8a8296f0-baa0-4ac7-9f7b-64a3f1946849
---
The following method of adding file references to a large solution was also attempted.

<!--endintro-->

![Figure: Adding a file reference](betterlargedotnet_fileref.gif)

This method involves projects referencing assemblies by looking into their reference path.

**Advantages**
The main advantage of referencing .dll's is that it is more flexible. Projects can reference assemblies from other solutions outside the current solution.

 - The solution's environment is "cleaner", allowing projects to be more expansive.
 - All you need to do is change the assembly to "shared".

**Disadvantages**
There are, however, many disadvantages including the fact that only one version of the proj file can be added to the solution.

- The .csproj file cannot be used.
- You cannot reference or one set of assemblies for debug and another for release. Only point to one.
- VS.NET only use the paths specified in the .proj file as a hint. VS.NET records the location of the assemblies as options for the project for each user.
- You cannot switch between versions.
- You also cannot use this method if there are 200 projects in one solution.
