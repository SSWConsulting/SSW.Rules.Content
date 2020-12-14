---
type: rule
archivedreason: 
title: Do you know the Code Health (Quality Gates) to add?
guid: 316c617a-3636-4c40-85dc-c94fdc98fbfa
uri: do-you-know-the-code-health-quality-gates-to-add
created: 2017-02-20T22:26:58.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 46
  title: Danijel Malik
related: []

---

Code health is all about quality and consistency. Here is how to use various auditors and linters not just in your development environment, but also on your VisualStudio.com build.

<!--endintro-->

Depending on your development environment and the type of project, you should utilise different auditing tools.
 1) Visual Studio - How to install and modify Visual Studio Analysers
 2) Visual Studio Code - How to include TSLint and CSSLint extensions
 3) VisualStudio.com - How to produce a build script which analyses code as part of the build process

Following the steps should take about 15 minutes to do, but longer to implement depending on the size of your solution. (Requires solution analysis in VS and at least one build on VisualStudio.com)

Version 1.2
- Added step to include "PrimaryBuild" variable as a pseudo id for the API
Version 1.1
- Removed CssLint from VisualStudio.com build definition
- Added Web Essentials to Visual Studio environment

### Visual Studio


Search & Install the NuGet packages:
"Roslyn Security Guard " https://www.nuget.org/packages/RoslynSecurityGuard/
"StyleCop.Analysers" https://www.nuget.org/packages/StyleCop.Analyzers/1.0.0
"tslint" https://www.nuget.org/packages/tslint/

For Visual Studio development on web applications, download Web Essentials, it will provide intellisense for JS, CSS, HTML, Less, Scss, and CoffeeScript. (https://marketplace.visualstudio.com/items?itemName=MadsKristensen.WebEssentials20153 )
<dl class="ssw15-rteElement-ImageArea"><img src="VS-InstallNuGetPackages.png" alt="VS-InstallNuGetPackages.png" style="margin:5px;width:808px;"></dl> **Figure: Steps to install NuGet Packages
** 
Here is a quick guide to the steps to install NuGet Packages to the entire solution:
 1) Right click solution
 2) Select "Manage NuGet packages for solution"
 3) Select "Browse"
 4) Search <package name=""><br> 5) Select <package name=""><br> 6) Check all projects<br> 7) Click "Install"<br><br>Issues from these will now be returned in the Visual Studio analyser error list.<br></package></package>
<dl class="ssw15-rteElement-ImageArea"><img src="VS-RoslynRules.png" alt="VS-RoslynRules.png" style="margin:5px;"><span style="color:#555555;font-size:0.9rem;font-weight:bold;"></span><span style="color:#555555;font-size:0.9rem;font-weight:bold;">Figure: New Roslyn Rule issues raised in Visual Studio Analyser</span></dl>
Run Code Analysis on the project. Check over all of the warnings, if they are unnecessary or inappropriate, disable them, otherwise modify their severity level to "Error". 
When the build is run, "Errors" will break the build, while "Warnings" will be reported, but not break the build.
Rules which have been flagged should also be checked once the build is completed

### Modify Visual Studio Analysis


The goal is to develop a shared ruleset across projects. (Currently this is just the default settings)
Any project specific rules should be documented in "\_Instructions-CodeHealth.docx" kept in the solution.
<mark>Please also copy the current version number of this rule into the "_Instructions-CodeHealth.docx" in order to track what version your existing solution adheres to.</mark>

<dl class="ssw15-rteElement-ImageArea"><dl class="ssw15-rteElement-ImageArea"><img src="VS-ModifyRules.png" alt="VS-ModifyRules.png" style="margin:5px;width:808px;"></dl> <strong>Figure: Steps to open Visual Studio Analyser rules customisation page<br></strong> <p class="ssw15-rteElement-P">Right Click project | Properties | Code Analysis | Open<br></p></dl><dl class="ssw15-rteElement-ImageArea"><dl class="ssw15-rteElement-ImageArea"><img src="VS-ModifyRules2.png" alt="VS-ModifyRules2.png" style="margin:5px;width:808px;"> <strong>Figure: How to customize rules. By either enabling / disabling rules or packages. Or by modifying the rule severity level.<br></strong> </dl></dl>
### Visual Studio Code


For web projects, we advocate the use of CSSLint for css files and TSLint for typescript files. ([Why you should be using TypeScript instead of JavaScript](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=d82703e0-6244-4fb6-9017-bac4e4b2361d))

Linters for these can be easily added to VS Code via extensions.
Simply select the "Extensions" tab, search for "CSSLint" and "TSLint" and click "Install" on each respectively.
<dl class="ssw15-rteElement-ImageArea"><img src="VSCode-Extensions.png" alt="VSCode-Extensions.png" style="margin:5px;width:808px;"></dl> **Figure: Addition of CssLint and TSLint to VS Code Project
** 
If you prefer not to use the Extensions (which are currently a bit out of date). You can install them using npm as normal.

CssLint https://www.npmjs.com/package/csslint
TSLint https://www.npmjs.com/package/tslint

### Automatically Check your Build in VisualStudio.com


<mark>Ensure utilisation of TeamBuild2015 or higher. (No support for XAML builds)</mark>
Edit the build definition
<dl class="ssw15-rteElement-ImageArea"><img src="VSO-EditBuild.png" alt="VSO-EditBuild.png" style="margin:5px;width:808px;"></dl> **Figure: Steps to edit an existing build definition on VisualStudio.com** 
Select "Build & Release" > Select "Builds" > Click on your existing build > Click "Edit"
<dl><dl class="ssw15-rteElement-ImageArea"><dl class="ssw15-rteElement-ImageArea"><img src="VSO-BuildDefinition-V3.png" alt="VSO-BuildDefinition-V3.png" style="margin:5px;width:808px;"></dl><span style="color:#555555;font-size:0.9rem;font-weight:bold;background-color:initial;">Figure: Example completed build definition.</span></dl></dl><dl><dl class="ssw15-rteElement-ImageArea"><dl class="ssw15-rteElement-ImageArea"><img src="VSO-DirectoryExampleV2.png" alt="VSO-DirectoryExampleV2.png" style="margin:5px;width:808px;"></dl></dl></dl> **Figure: Example directory for TSLint run commands
** 
Under advanced for the Command Line tasks, the Working Directory can be specified if necessary.

TsLint

**Npm** - Install tslint and typescript
 **Name:** npm install tslint
**Working Folder:** <top directory=""><br class="ssw15-rteStyle-IndentText"><span class="ssw15-rteStyle-IndentText"> <strong>Npm Command:</strong> install</span><br class="ssw15-rteStyle-IndentText"><span class="ssw15-rteStyle-IndentText"> <strong>Arguments:</strong> -g tslint typescript</span></top>

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
 **Arguments:** --force <solution directory="">/**/*.ts{,x}</solution>

If your build is being hosted, then the config file must be reloaded every time. If your build is running on premises, the config file will attempt to load over the existing one and break the build.
If this is the case, just add a step to delete your config file after the scan is complete.
<dl class="ssw15-rteElement-ImageArea"><img src="VSO-RemoveConfig.png" alt="VSO-RemoveConfig.png" style="margin:5px;width:808px;"> <strong>Figure: Command line step to remove the config file (tslint.json) after the linter has run<br></strong> </dl>
**Command Line** - Remove the tslint config file, as it will break future scan if the build is on premises if a config file already exists and an attempt to add another one is made.
 **Name:** Remove tslint config
 **Tool:** del
 **Arguments:** tslint.json

Once complete, save the build definition and run the build.
Then check the build is successful.
If the build fails (due to errors), these should be corrected in the development environment. 
If warnings exist, the rule should be disabled or set as an error. (If it is worth fixing, then it should be required for everyone)



If your project does not contain TypeScript files, then you do not need to include the TSLint build tasks.
<dl><dd class="ssw15-rteElement-FigureNormal"><img src="VSO-EnsureTSLintRuns.png" alt="VSO-EnsureTSLintRuns.png" style="margin:5px;width:808px;">Figure: Ensure TSLint actually finds files to scan (if the project includes TSLint files) otherwise it will pass without you noticing<br></dd><p class="ssw15-rteElement-P"><br></p><p class="ssw15-rteElement-P">For the purposes of reporting, a unique tag must be added to the build definition which the Code Health steps have been applied to. <br>This is done with the addition of a variable (Name = PrimaryBuild, Value = true)<span style="background-color:initial;"></span></p><dl class="ssw15-rteElement-ImageArea"><dd class="ssw15-rteElement-FigureNormal"><img src="VSO-AddVariableTag.png" alt="VSO-AddVariableTag.png" style="margin:5px;width:650px;">Figure: Steps to add PrimaryBuild variable to build definition<span style="background-color:initial;color:#333333;font-size:13px;"></span></dd></dl></dl><dl class="ssw15-rteElement-ImageArea"><dl class="ssw15-rteElement-ImageArea"><img src="VSO-BuildResult-BadV3.png" alt="VSO-BuildResult-BadV3.png" style="margin:5px;width:808px;"></dl></dl>

::: bad
Figure: Bad Example - Build broke due to compile errors. Must fix to proceed.

:::

<dl><dl><dl class="ssw15-rteElement-ImageArea"><img src="VSO-BuildResultV3.png" alt="VSO-BuildResultV3.png" style="margin:5px;width:808px;"></dl><br><br>::: bad<br>Figure: Bad Example - Successful build with warnings. Should be disabled or set as errors.<br><br>:::<br><br></dl><dl class="ssw15-rteElement-ImageArea"><dl class="ssw15-rteElement-ImageArea"><img src="VSO-BuildResult-GoodV3.png" alt="VSO-BuildResult-GoodV3.png" style="margin:5px;width:808px;"></dl></dl><br><br>::: good<br>Figure: Good Example - Successful build with no warnings.<br><br>:::<br><br></dl>
