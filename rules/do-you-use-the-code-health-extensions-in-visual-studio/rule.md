---
type: rule
title: Do you use the Code Health Extensions in Visual Studio?
uri: do-you-use-the-code-health-extensions-in-visual-studio
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Danijel Malik
    url: https://ssw.com.au/people/danijel-malik
related: []
redirects: []
created: 2017-03-09T22:11:25.000Z
archivedreason: null
guid: b0048e8d-b6bb-4af3-9397-a9af6fac1a88
---
The code quality standard should extend the Visual Studio Analyzer. A wide variety of additional analyzers can be included via Nuget, the minimum standard should include Roslyn Security Guard.

<!--endintro-->

### Related Steps to Code Health

* [Do you use the Code Health Extensions in VS Code?](/do-you-use-the-code-health-extensions-in-vs-code)
* [Do you run the Code Health checks in your VisualStudio.com Continuous Integration Build?](/do-you-run-the-code-health-checks-in-your-visualstudio-com-continuous-integration-build)

### Which Packages to Install in Visual Studio

Search & Install the NuGet packages:

* "Roslyn Security Guard" ([Nuget page for Roslyn Security Guard](https://www.nuget.org/packages/RoslynSecurityGuard/)) - Security audit on .NET Applications.

![Figure: Steps to install NuGet Packages](VS-InstallNuGetPackages.png)

Issues from these will now be returned in the Visual Studio analyzer error list.
![Figure: New Roslyn Rule issues raised in Visual Studio Analyzer](VS-RoslynRules.png)

Your goal should be to get the issues in a solution down to zero.

If you believe the issues being raised are not important, please check the section below which outlines how to change the ruleset.

### Modify Visual Studio Analysis Ruleset

The goal is to develop a shared ruleset across projects. This will ensure the same standard and quality of code is maintained across all of the company's projects.

Any project specific rules should be documented in "_docs\Instructions-CodeHealth.md" which is to be kept in the solution as per [Do you make awesome documentation?](/awesome-documentation/)

You can configure the severity of analyzer rules in an EditorConfig file.

Follow the rule [Do you keep your code consistent using .editorconfig?
](/consistent-code-style/) to add EditorConfig file to your project or solution.
