---
seoDescription: Simplify and streamline your .NET projects by using the Directory.Build.props file. Learn how this MSBuild feature centralizes configuration for multiple projects, reduces redundancy, and improves maintainability for enterprise-level .NET solutions. Discover how to manage common settings like .NET framework version, nullability, implicit references, and static code analysis efficiently across your solution.
type: rule
title: Do you use Directory.Build.Props to simplify multi-project build configurations?
uri: directory-build-props
authors:
  - title: Daniel Mackay
    url: https://www.ssw.com.au/people/daniel-mackay
  - title: Luke Cook
    url: https://www.ssw.com.au/people/luke-cook
created: 2024-10-28T17:00:00.000Z
guid: E3F562C1-30FF-4982-B96F-2AA0A716E842
---

When working on large enterprise scale projects .NET Solutions can often become unwieldy and difficult to maintain. This is particularly true of `.csproj` files which end up repeating configuration across all projects. How can one file save you hours of maintenance by keeping project configuration DRY?

<!--endintro-->

## What is a Directory.Build.props file?

A [Directory.Build.props](https://learn.microsoft.com/en-us/visualstudio/msbuild/customize-by-directory?view=vs-2022&WT.mc_id=DT-MVP-33518) file is an MSBuild file used in .NET projects to define common properties and configurations that apply to multiple projects within a directory tree. This file helps centralize the configuration and reduce redundancy by allowing you to specify settings that will be inherited by all projects under the directory where the file is located.

### Usages

This can be used for:

* .NET framework version
* Nullability
* Implicit references
* Configuring warnings as errors
* Static code analysis
* Author / Company

### Examples

::: greybox

**Project1.csproj:**

```xml
<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>

    <!-- Configure code analysis. -->
    <AnalysisLevel>latest</AnalysisLevel>
    <AnalysisMode>Recommended</AnalysisMode>
    <TreatWarningsAsErrors Condition="'$(Configuration)' == 'Release'">true</TreatWarningsAsErrors>
    <CodeAnalysisTreatWarningsAsErrors Condition="'$(Configuration)' == 'Release'">true</CodeAnalysisTreatWarningsAsErrors>
    <EnforceCodeStyleInBuild>true</EnforceCodeStyleInBuild>
  </PropertyGroup>

</Project>
```

**Project2.csproj:**

```xml
<Project Sdk="Microsoft.NET.Sdk.Web">

    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <Nullable>enable</Nullable>
        <ImplicitUsings>enable</ImplicitUsings>

        <!-- Configure code analysis. -->
        <AnalysisLevel>latest</AnalysisLevel>
        <AnalysisMode>Recommended</AnalysisMode>
        <TreatWarningsAsErrors Condition="'$(Configuration)' == 'Release'">true</TreatWarningsAsErrors>
        <CodeAnalysisTreatWarningsAsErrors Condition="'$(Configuration)' == 'Release'">true</CodeAnalysisTreatWarningsAsErrors>
        <EnforceCodeStyleInBuild>true</EnforceCodeStyleInBuild>
    </PropertyGroup>

</Project>
```

:::
::: bad
Bad example - Redundant configuration
:::

::: good
**Project1.csproj:**

```xml
<Project Sdk="Microsoft.NET.Sdk.Web">
</Project>
```

**Project2.csproj:**

```xml
<Project Sdk="Microsoft.NET.Sdk.Web">
</Project>
```

**Directory.Build.props:**

```xml
<Project>
    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <ImplicitUsings>enable</ImplicitUsings>
        <Nullable>enable</Nullable>

        <!-- Configure code analysis. -->
        <AnalysisLevel>latest</AnalysisLevel>
        <AnalysisMode>Recommended</AnalysisMode>
        <TreatWarningsAsErrors Condition="'$(Configuration)' == 'Release'">true</TreatWarningsAsErrors>
        <CodeAnalysisTreatWarningsAsErrors Condition="'$(Configuration)' == 'Release'">true</CodeAnalysisTreatWarningsAsErrors>
        <EnforceCodeStyleInBuild>true</EnforceCodeStyleInBuild>
    </PropertyGroup>
</Project>
```

:::
::: good
Good example - Centralized configuration
:::
