---
type: rule
archivedreason: 
title: Do you run the Code Health checks in your VisualStudio.com Continuous Integration Build?
guid: 049c8237-303a-43f1-b0b4-1432e8908c1c
uri: do-you-run-the-code-health-checks-in-your-visualstudio-com-continuous-integration-build
created: 2017-03-09T22:13:05.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Danijel Malik
  url: https://ssw.com.au/people/danijel-malik
related: []
redirects: []

---

The real value of the code health system is that is made improvements in code quality more visible to the team and managers. By including several steps to the build process, the results of the analysers included in previous steps can be extracted out and summarised in a report spanning the project's lifetime. 

<!--endintro-->

### Related Steps to Code Health:


* [Do you use the Code Health Extensions in VS Code?](/do-you-use-the-code-health-extensions-in-vs-code)
* [Do you use the Code Health Extensions in Visual Studio?](/do-you-use-the-code-health-extensions-in-visual-studio)


### What Steps to Include in the Build Definition

Summary:

1. Ensure "Restore NuGet Packages" & "Build Solution" are in the build definition to run the Roslyn analysers.
2. Add several npm and command line steps to the build definition to run tslint. (On premises builds require an additional step).
3. Include an identifying variable "PrimaryBuild" to the build definition.
4. Check the build is running without issues.


The resulting build should look like this:

::: good
![Figure: Good Example - Build Passing with no summary issues](VSO-Build-Good-1.png)
:::

<mark>Ensure utilisation of TeamBuild2015 or higher. (No support for XAML builds)</mark>
Edit the build definition on &lt;CompanyName&gt;.visualstudio.com, and add the following build tasks.
If your project does not contain TypeScript files, then you do not need to include the TSLint build tasks.

::: good
![Figure: Good Example - Steps added to build definition](VSO-BuildDefinition-V3.png)
:::

![Figure: Example directory for TSLint run commands](VSO-DirectoryExampleV2.png)

Under advanced for the Command Line tasks, the Working Directory can be specified if necessary.

```
TsLint
 **Npm** - Install tslint and typescript  
 **Name:** npm install tslint  
 **Working Folder:** &lt;Top Directory&gt;  
 **Npm Command:** install  
 **Arguments:** -g tslint typescript  
  
 **Command Line** - Check the version (Useful to determine rule discrepancies across builds)  
 **Name:** Check tslint version   
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
```

If your build is being hosted, then the config file must be reloaded every time. <mark>If your build is running on premises</mark>, the config file will attempt to load over the existing one and break the build.

If this is the case, just add a step to delete your config file after the scan is complete.

![Figure: Command line step to remove the config file (tslint.json) after the linter has run](VSO-RemoveConfig.png)

```
 **Command Line** - Remove the tslint config file, as it will break future scan if the build is on premises if a config file already exists and an attempt to add another one is made.  
 **Name:** Remove tslint config  
 **Tool:** del  
 **Arguments:** tslint.json  
```

Once complete, save the build definition and run the build.

Then check the build is successful.

If the build fails (due to errors), these should be corrected in the development environment.

### Include "PrimaryBuild" variable

For the purposes of reporting, a unique tag must be added to the build definition which the Code Health steps have been applied to. 
This is done with the <mark>addition of a variable (Name = PrimaryBuild, Value = true)</mark>

![Figure: Steps to add PrimaryBuild variable to build definition](VSO-AddVariableTag.png)

### Check the build is running without issues

::: bad
![Figure: Bad Code with a Good Code Health Implementation - Build broke due to compile errors. Must fix to proceed](VSO-Build-Bad-1.png)
:::

::: bad
![Figure: Bad Code with a Good Code Health Implementation - Successful build with warnings. These should be reprioritised as errors, or removed](VSO-Build-Ok-1.png)
:::

::: good
![Figure:  Good Code with a Good Code Health Implementation - Successful build with no warnings](VSO-Build-Good-1.png)
:::
