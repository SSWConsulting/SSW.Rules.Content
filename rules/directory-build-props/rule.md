---
seoDescription: Do you use Directory.Build.Props to simplify multi-project build configurations?
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

When working on large enterprise scale projects .NET Solutions can often become unwieldy and difficult to maintain. This is particulary true of `.csproj` files which end up repeating configuration across all projects.

<!--endintro-->

## Directory.Build.props

A [Directory.Build.props](https://learn.microsoft.com/en-us/visualstudio/msbuild/customize-by-directory?view=vs-2022) file can be used to simplify multi-project build configurations and keep common configuration in a single place.

## Usages

This can be used for:

- .NET framework version
- Nullability
- Implicit references
- Configuring warnings as errors
- Static code analysis

## ❌ Bad Example

Project1.csproj:
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

Project2.csproj:
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

## ✅ Good Example

Project1.csproj:
```xml
<Project Sdk="Microsoft.NET.Sdk.Web">
</Project>
```

Project2.csproj:
```xml
<Project Sdk="Microsoft.NET.Sdk.Web">
</Project>
```

Directory.Build.props:
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
