---
seoDescription: Organize your .NET code with structured common code assemblies into Common, CommonWindows, and CommonWeb sections.
type: rule
title: Do you have a correctly structured common code assembly?
uri: do-you-have-a-correctly-structured-common-code-assembly
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T05:36:00.000Z
guid: 4810a4d6-e9fa-48f3-89af-77d309fcfe6c
---

Your common code assembly should be divided into the following sections:

 <!--endintro-->

- **Common** (e.g. SSW.Framework.Common)
  - Code which is not UI specific
  - Example: Code to convert a date into different formats
- **CommonWindows** (e.g. SSW.Framework.WindowsUI)
  - Example: Base forms which are the same for all products, wizard frameworks
- **CommonWeb** (e.g. SSW.Framework.WebUI)
  - Example: Generic XML-based navigation components

For more information see [Do you have a consistent .NET Solution Structure?](/do-you-have-a-consistent-net-solution-structure).
