---
type: rule
archivedreason: 
title: Do you know the Code Health (Quality Gates) to add?
guid: 316c617a-3636-4c40-85dc-c94fdc98fbfa
uri: do-you-know-the-code-health-quality-gates-to-add
created: 2017-02-20T22:26:58.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Danijel Malik
  url: https://ssw.com.au/people/danijel-malik
related: []
redirects:
- do-you-know-the-code-health-(quality-gates)-to-add

---

Code health is all about quality and consistency. Here is how to use various auditors and linters not just in your development environment, but also on your VisualStudio.com build.

<!--endintro-->

Depending on your development environment and the type of project, you should utilise different auditing tools.
1. Visual Studio - How to install and modify Visual Studio Analysers
2. Visual Studio Code - How to include TSLint and CSSLint extensions
3. VisualStudio.com - How to produce a build script which analyses code as part of the build process

Following the steps should take about 15 minutes to do, but longer to implement depending on the size of your solution. (Requires solution analysis in VS and at least one build on VisualStudio.com)

Version 1.2
- Added step to include "PrimaryBuild" variable as a pseudo id for the API
Version 1.1
- Removed CssLint from VisualStudio.com build definition
- Added Web Essentials to Visual Studio environment

### Visual Studio

Search & Install the NuGet packages:
"Roslyn Security Guard" - [https://www.nuget.org/packages/RoslynSecurityGuard/](https://www.nuget.org/packages/RoslynSecurityGuard/)
"StyleCop.Analysers" - [https://www.nuget.org/packages/StyleCop.Analyzers/1.0.0](https://www.nuget.org/packages/StyleCop.Analyzers/1.0.0)
"tslint" - [https://www.nuget.org/packages/tslint/](https://www.nuget.org/packages/tslint/)

For Visual Studio development on web applications, download Web Essentials, it will provide intellisense for JS, CSS, HTML, Less, Scss, and CoffeeScript. (https://marketplace.visualstudio.com/items?itemName=MadsKristensen.WebEssentials20153)

![Figure: Steps to install NuGet Packages](VS-InstallNuGetPackages.png) 

Here is a quick guide to the steps to install NuGet Packages to the entire solution:
1. Right click solution
2. Select "Manage NuGet packages for solution"
3. Select "Browse"
4. Search &lt;package name&gt;
5. Select &lt;package name&gt;
6. Check all projects
7. Click "Install"

Issues from these will now be returned in the Visual Studio analyser error list.

![Figure: New Roslyn Rule issues raised in Visual Studio Analyser](VS-RoslynRules.png)

Run Code Analysis on the project. Check over all of the warnings, if they are unnecessary or inappropriate, disable them, otherwise modify their severity level to "Error". 

When the build is run, "Errors" will break the build, while "Warnings" will be reported, but not break the build.
Rules which have been flagged should also be checked once the build is completed

### Modify Visual Studio Analysis

The goal is to develop a shared ruleset across projects. (Currently this is just the default settings)
Any project specific rules should be documented in "\_Instructions-CodeHealth.docx" kept in the solution.
<mark>Please also copy the current version number of this rule into the "_Instructions-CodeHealth.docx" in order to track what version your existing solution adheres to.</mark>

![Figure: Steps to open Visual Studio Analyser rules customization page](VS-ModifyRules.png)

Right Click project | Properties | Code Analysis | Open

![Figure: How to customize rules. By either enabling / disabling rules or packages. Or by modifying the rule severity level](VS-ModifyRules2.png)

### Visual Studio Code

For web projects, we advocate the use of CSSLint for css files and TSLint for typescript files. ([Why you should be using TypeScript instead of JavaScript](/do-you-know-when-to-use-typescript-vs-javascript-and-coffeescript))

Linters for these can be easily added to VS Code via extensions.
Simply select the "Extensions" tab, search for "CSSLint" and "TSLint" and click "Install" on each respectively.

![Figure: Addition of CssLint and TSLint to VS Code Project](VSCode-Extensions.png)

If you prefer not to use the Extensions (which are currently a bit out of date). You can install them using npm as normal.

CssLint [https://www.npmjs.com/package/csslint](https://www.npmjs.com/package/csslint)
TSLint [https://www.npmjs.com/package/tslint](https://www.npmjs.com/package/tslint)

### Automatically Check your Build in VisualStudio.com

<mark>Ensure utilisation of TeamBuild2015 or higher. (No support for XAML builds)</mark>

Edit the build definition

<img src="VSO-EditBuild.png" alt="VSO-EditBuild.png" style="margin:5px;width:808px;"> **Figure: Steps to edit an existing build definition on VisualStudio.com** 

Select "Build & Release" &gt; Select "Builds" &gt; Click on your existing build &gt; Click "Edit"

![Figure: Example completed build definition](VSO-BuildDefinition-V3.png)

![Figure: Example directory for TSLint run commands](VSO-DirectoryExampleV2.png)

Under advanced for the Command Line tasks, the Working Directory can be specified if necessary.

TsLint

**Npm** - Install tslint and typescript
**Name:** npm install tslint
**Working Folder:** &lt;Top Directory&gt;
**Npm Command:** install
**Arguments:** -g tslint typescript

**Command Line** - Check the version (Useful to determine rule discrepancies across builds)
**Name** : Check tslint version
**Tool:** tslint
**Arguments:** -v

**Command Line** - Builds a default configuration file for the build (Without it issues can differ between build and development environment
**Name:** Create tslint config file
**Tool:** tslint
**Arguments:** --init

**Command Line** - Run tslint, force is required to stop the build from crashing (TSLint will return and exit code of 1 regardless of if issues exist)
**Name:** Run tslint
**Tool:** TSLint
**Arguments:** --force &lt;Solution Directory&gt;/\*\*/\*.ts{,x}

If your build is being hosted, then the config file must be reloaded every time. If your build is running on premises, the config file will attempt to load over the existing one and break the build.

If this is the case, just add a step to delete your config file after the scan is complete.

![Figure: Command line step to remove the config file (tslint.json) after the linter has run](VSO-RemoveConfig.png)

**Command Line** - Remove the tslint config file, as it will break future scan if the build is on premises if a config file already exists and an attempt to add another one is made.
**Name:** Remove tslint config
**Tool:** del
**Arguments:** tslint.json

Once complete, save the build definition and run the build.

Then check the build is successful.

If the build fails (due to errors), these should be corrected in the development environment. 

If warnings exist, the rule should be disabled or set as an error. (If it is worth fixing, then it should be required for everyone)

If your project does not contain TypeScript files, then you do not need to include the TSLint build tasks.

![Figure: Ensure TSLint actually finds files to scan (if the project includes TSLint files) otherwise it will pass without you noticing](VSO-EnsureTSLintRuns.png)

For the purposes of reporting, a unique tag must be added to the build definition which the Code Health steps have been applied to. 

This is done with the addition of a variable (Name = PrimaryBuild, Value = true)

![Figure: Steps to add PrimaryBuild variable to build definition](VSO-AddVariableTag.png)

::: bad
![Figure: Bad Example - Build broke due to compile errors. Must fix to proceed](VSO-BuildResult-BadV3.png)
:::

::: bad
![Figure: Bad Example - Successful build with warnings. Should be disabled or set as errors](VSO-BuildResultV3.png)
:::

::: good
![Figure: Good Example - Successful build with no warnings](VSO-BuildResult-GoodV3.png)  
:::
