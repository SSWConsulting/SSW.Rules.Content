---
type: rule
archivedreason: 
title: Do you use the Code Health Extensions in Visual Studio?
guid: b0048e8d-b6bb-4af3-9397-a9af6fac1a88
uri: do-you-use-the-code-health-extensions-in-visual-studio
created: 2017-03-09T22:11:25.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Danijel Malik
  url: https://ssw.com.au/people/danijel-malik
related: []
redirects: []

---

The code quality standard should extend the Visual Studio Analyser. A wide variety of additional analysers can be included via Nuget, the minimum standard should include Roslyn Security Guard, Stylecop.Analysers and TSLint.

<!--endintro-->

### Related Steps to Code Health:

* [Do you use the Code Health Extensions in VS Code?](/do-you-use-the-code-health-extensions-in-vs-code)
* [Do you run the Code Health checks in your VisualStudio.com Continuous Integration Build?](/do-you-run-the-code-health-checks-in-your-visualstudio-com-continuous-integration-build)

### Which Packages to Install in Visual Studio

Search & Install the NuGet packages:

* "Roslyn Security Guard" ([Nuget page for Roslyn Security Guard](https://www.nuget.org/packages/RoslynSecurityGuard/)) - Security audit on .NET Applications.
* "StyleCop.Analysers" ([Nuget page for StyleCop.Analysers](https://www.nuget.org/packages/StyleCop.Analyzers/1.0.0)) - Ensures C# code style conformity.
* "tslint" ([Nuget page for tslint](https://www.nuget.org/packages/tslint/)) - Allows for issue tracking of TypeScript projects.

![Figure: Steps to install NuGet Packages](VS-InstallNuGetPackages.png)

Issues from these will now be returned in the Visual Studio analyser error list.
![Figure: New Roslyn Rule issues raised in Visual Studio Analyser](VS-RoslynRules.png)

Your goal should be to get the issues in a solution down to zero.

If you believe the issues being raised are not important, please check the section below which outlines how to change the ruleset.

### Modify Visual Studio Analysis Ruleset

The goal is to develop a shared ruleset across projects. (Currently this is just the default settings). This will ensure the same standard and quality of code is maintained across all of the company's projects.
Any project specific rules should be documented in "\_Instructions-CodeHealth.docx" which is to be kept in the solution.
Please also copy the current version number of this rule into the "\_Instructions-CodeHealth.docx" in order to track what version your existing solution adheres to.

![Figure: Steps to open Visual Studio Analyser rules customisation page](VS-ModifyRules.png)
\
Steps to open Analyser customisation page:

Right Click project &gt; Properties &gt; Code Analysis &gt; Open

![Figure: How to customize rules. By either enabling / disabling rules or packages. Or by modifying the rule severity level](VS-ModifyRules2.png)

![Figure: How to apply custom ruleset to all projects in a solution](VS-ModifyRules3.png)
