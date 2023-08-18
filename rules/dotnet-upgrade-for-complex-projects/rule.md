---
type: rule
title: Do you know how to handle complex .NET migrations?
uri: dotnet-upgrade-for-complex-projects
authors:
  - title: Jernej Kavka (JK)
    url: https://ssw.com.au/people/jk
    img: https://github.com/SSWConsulting/SSW.People.Profiles/raw/main/Jernej-Kavka/Images/Jernej-Kavka-Profile.jpg
  - title: Gordon Beeming
    url: https://www.ssw.com.au/people/gordon-beeming
related:
  - dotnet-upgrade-assistant
  - migrate-from-system-web-to-modern-alternatives
created: 2023-07-16T23:08:53.979Z
guid: 9de5ca88-a6aa-4fe5-af47-d6d2169cde86
---

There's not 1 single thing that makes a .NET project complicated to migrate to the latest .NET framework. Generally though it's a combination of the following:

- Long lived code base
- Lots of external dependencies
- Lots of application components (web, desktop, services, etc)
- etc

Your first action should always be to use the [.NET Upgrade Assistant](https://dotnet.microsoft.com/en-us/platform/upgrade-assistant). You can read more about the tool at [Do you know how to modernize your .NET applications?](https://www.ssw.com.au/rules/dotnet-upgrade-assistant/) It is strongly advised to consult this rule before progressing further, particularly if you haven't had the opportunity to do so yet. 

Below you will find some tips and tricks to help you with your more complicated migrations.

<!--endintro-->

# Preparation

### Upgrade the projects to use the sdk style csproj format

You can use the [try-convert](https://github.com/dotnet/try-convert) dotnet tool to convert your projects to the new sdk style csproj format. This will make it easier to upgrade the projects to the latest .net framework.

Install the tool using 

```bash
dotnet tool install -g try-convert
```
    
Upgrade your web projects using

```bash
try-convert --keep-current-tfms --force-web-conversion
```

and your other projects using

```bash
try-convert --keep-current-tfms
```

### Change all your projects to be able to target multiple Target framework monikers (TFM)

In all your project files change the `TargetFramework` to `TargetFrameworks`. You want to do  this early on to enable a smoother flow later to not need unload and reload projects or have to close and reopen Visual Studio.

What this will allow you to do is add your target framework and compile the code. This will allow you to see what code is not compatible with the new framework and fix those issues while still developing/deploying your project in the current target framework. 

# Upgrading

At this point the approach you will take will be to iterate through the following steps:

1. Add the target framework to your project
2. Compile to see what breaks
3. Fix what is easy to fix
   1. Remember to commit after each fix to help your reviewers 😉
4. Anything that is not easy to fix, create a PBI with details of the issue
   1. This allows another developer on your team to work on that PBI independently
5. If you have a project that is able to compile at this point you can leave the new TFM in your project and continue to the next project
   1. If not, you can remove the new TFM and continue to the next project
   2. Repeat these steps once the PBIs have been completed related to this project

Some of the PBIs you create may only be able to be fixed once all the projects have been upgraded. This is fine, just make sure you have a PBI for it and tag it to know it can only be done as a final migration step.

# Final Migration Steps

At some point you'll reach a point where it makes more sense to do the last of your PBIs in one go and switch your main branch over to the new TFM. This will be a judgement call based on how many PBIs you have left and how long they will take to complete.

Here are some tips for how you can make changes that are not compatible with both target TFM's.

## Using `#if` pragma statements

You can use `#if` statements to make code that is only compiled for a specific TFM. This is useful for code that is not compatible with both TFMs.

Wherever possible look at using a factory pattern or dependency injection to inject the correct implementation for the TFM you are targeting.

```csharp
public static class WebClientFactory
{
  public static IWebClient GetWebClient()
  {
#if NET472
    return new CustomWebClient();
#else
    return new CustomHttpClient();
#endif
  }
}
```

This would limit the post migration cleanup of these pragmas making it easier to remove them later.

## MSBuild conditions

You can use MSBuild conditions to add references to different libraries that are only compatible with a specific TFM.

```xml
<ItemGroup Condition="'$(TargetFramework)' == 'net472'">
    <Reference Include="System.Web" />
    <Reference Include="System.Web.Extensions" />
    <Reference Include="System.Web.ApplicationServices" />
</ItemGroup>
```

