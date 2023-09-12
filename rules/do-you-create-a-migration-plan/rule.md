---
type: rule
title: Do you create a migration plan?
uri: migration-plans
authors:
  - title: Luke Cook
    url: https://ssw.com.au/people/luke-cook
  - title: Gordon Beeming
    url: https://www.ssw.com.au/people/gordon-beeming
  - title: Yazhi Chen
    url: https://www.ssw.com.au/people/yazhi-chen
related:
  - dotnet-upgrade-assistant
  - migrate-from-system-web-to-modern-alternatives
created: 2023-09-06T23:08:53.979Z
guid: d47bb1e4-261f-436e-84fc-fdb1b21e0d36
---

Migrating from .NET Framework (4.x) to the latest .NET (5+) brings huge advantages to your app's performance, hosting fees, and maintainability. But it's important that you understand what the road to .NET 5+ looks like for your app *before* you start breaking things! So how do you ensure your migration is being done the right way? 

<!--endintro-->

# Preparation
The migration to a newer versions of .NET is the perfect opportunity for you to take stock of your current application architecture, and address any technical debt your app has accumulated. Trying to migrate an application that's poorly architected or carrying a lot of tech debt will make your migration **exponentially harder**. Therefore, now is the time to perform a full audit of your app and ensure you have PBIs to rectify these problems before you consider it "migration-ready".

### Dependency analysis
Imagine a typical N-tiered application. Over the course of that application's life, the lines between each tier will often get blurred (either accidentally or deliberately). This can result in certain dependencies appearing in places they shouldn't - such as `System.Web` references showing up in your application or data layer. This is a very common code smell and is a great starting point to cleaning up your app.

If your app has 3rd party dependencies (e.g. with a financial system, reporting system, etc.) - now is the time to do some investigation around those integration points to determine whether those services provide compatible libraries and how those libraries differ (if at all). Create PBIs for these as well. 

### Infrastructure
If you host your app on premise, it's also worth checking your infrastructure to ensure it's has the necessary runtimes.

# Breaking changes
Once you've addressed any technical debt or architectural concerns, you can start gauging the amount of work involved in the migration itself.

::: greybox
**Tip:** You want to work from the bottom up in N-tiered applications (or inside-out with Onion architecture). This will allow you to work through the migration incrementally, and address any breaking changes *upstream*. If you migrate top-down (or outside-in), you will find yourself having to rewrite *downstream* code multiple times. 
:::

### Upgrade the csproj files
The first thing you want to do is update your projects' `csproj` files to the new SDK-style format. This greatly simplifies the contents of the file, and will allow you to easily target multiple versions of .NET framework monikors simultaneously (more on this below).

::: greybox
**Tip:** You can use the [try-convert](https://github.com/dotnet/try-convert) dotnet tool to convert your projects to the new sdk style csproj format.

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
:::


### Change all your projects to be able to target multiple Target Framework Monikers (TFM)
Now you have shiny new SDK-style `csproj` files, it's time to see what breaks!

Targeting both your current .NET Framework version *and* your future .NET version will give you the following information:

* Expose any build errors you receive when trying to build for .NET
* Expose any build errors you receive when trying to build for .NET Framework

::: greybox
Why is this important?

Imagine you *don't* do this, and instead, you simply target .NET Core. You get a list of 100 build errors due to breaking changes - too many for 1 Sprint (or 2 Sprints, or 3).

You start fixing these build errors. You go from 100 errors to 50 - progress!
Then you're told there's an urgent bug/feature/whatever that needs fixing ASAP. But you've still got 50 build errors when you're targeting .NET Core.

"No problem", you say. "I'll just switch back to .NET Framework and do this fix, and push out a new deployment".

You switch to .NET Framework, build the project, and...25 build errors?!

While you were fixing those build errors, you wrote code that isn't compatible with .NET Framework. Now you have an urgent bug/feature/whatever, as well as 25 new build errors you have to solve ☠️.

Using multiple TFMs from day 1 ensures you are fixing the breaking changes for .NET Core, *without* introducing breaking changes in .NET Framework.

This allows you up to work on your migration PBIs **incrementally**, while still allowing you to deploy your app on the current .NET version - win/win!
:::

In all your project files, change the `TargetFramework` tag to `TargetFrameworks`. You want to do this early on to enable a smoother flow later to not need unload and reload projects or have to close and reopen Visual Studio.

```csharp
<TargetFrameworks>net472;net8.0</TargetFrameworks>
```
![Figure: Git changes for targeting to multiple target frameworks](target-to-multiple-TFMs.png)

### Creating the migration backlog

At this point, ensure your project can target both the .NET Framework and the new target .NET. Some of the projects might not support both platforms right away and you can follow these steps to fix the issues and have a better understanding of how much work it might lies ahead.

1. Add the target framework to your project
2. Compile to see what breaks
3. Fix what is easy to fix
   1. Remember to commit after each fix to help your reviewers 😉
4. Anything that is not easy to fix, create a PBI with details of the issue
   1. This allows another developer on your team to work on that PBI independently
5. If you have a project that is able to compile at this point you can leave the new TFM in your project and continue to the next project
   1. If not, you can remove the new TFM and continue to the next project
   2. Repeat these steps once the PBIs have been completed related to this project

By the end of this process, you'll have a much clearer view (and backlog!) of your path to .NET Core:

* PBIs for technical debt
* PBIs for architectural concerns
* PBIs for breaking changes

# What's next?
While this guide aims to give you a high-level view of migrating your app to .NET Core, there are other some special considerations when dealing with complex applications and web apps. Check out these othe rules:

- [Migrating web apps to .NET Core](https://www.ssw.com.au/rules/migrating-web-apps-to-dotnet-core)
- [Do you know how to migrate from System.Web to modern alternatives?](https://www.ssw.com.au/rules/migrate-from-system-web-to-modern-alternatives/)
- [Do you know how to migrate from EDMX to EF Core?](https://www.ssw.com.au/rules/migrate-from-edmx-to-ef-core/)



# Web application

There are several ways to migrate project from ASP.NET to ASP.NET Core. We strongly recommend using the Strangler Fig pattern to incrementally migrate your project with [YARP](https://microsoft.github.io/reverse-proxy/).

### Create side-by-side incremental project with [.NET Upgrade Assistant](https://dotnet.microsoft.com/en-us/platform/upgrade-assistant)

This will create a new .NET 8 project. For functionalities that have not yet been migrated, YARP will redirect them to the .NET Framework web application.

### Configure YARP

```csharp
var webRoutes = new List<RouteConfig>
{
    // Route for token
    new()
    {
        RouteId = "tokenServePath",
        ClusterId = tokenClusterId,
        Match = new RouteMatch
        {
            Path = "/token/{**catch-all}",
        },
    },

    // Route for WebUI App
    new RouteConfig
    {
        RouteId = "webUIServePath",
        ClusterId = webUiClusterId,
        Match = new RouteMatch
        {
            Path = "/api/v2/{**catch-all}",
        },
    },

    // Route for WebApp App
    new RouteConfig
    {
        RouteId = "webAppServePath",
        ClusterId = webAppClusterId,
        Match = new RouteMatch
        {
            Path = "/api/{**catch-all}",
        },
    },

    // Route for Angular
    new RouteConfig
    {
        RouteId = "angularUIServePath",
        ClusterId = angularClusterId,
        Match = new RouteMatch
        {
            Path = "{**catch-all}",
        },
    }
};

```

**Figure: Example code for setting up different paths within YARP's configuration.**

### Upgrading components using Upgrade Assistant

Once you have created the side-by-side project, select the project that needs migration and `right click` | `Upgrade` on it.

![Figure: Context menu on the project to be migrated.](https://github.com/SSWConsulting/SSW.Rules.Content/assets/3699937/3303daaf-0dea-4b34-9f59-53fd55acf2ef)

Upgrade Assistant will show you a Summary view and detect that the project is linked to your Yarp proxy.
You can also see the migration progress of your endpoints from .NET Framework to .NET as a pie chart.

![Figure: Upgrade Assistants Summary page.](https://github.com/SSWConsulting/SSW.Rules.Content/assets/3699937/8564c9a7-b3a7-4b40-b002-be9c6fabcb16)

From here you can explore your endpoints through the `Endpoint explorer`, which will also indicate what endpoints have already been migrated and which ones are still outstanding.
The chain icon indicates that this endpoint has been migrated and is linked between the controller in the old project and the controller in the Yarp proxy project. ![Figure: Chain Icon](https://github.com/SSWConsulting/SSW.Rules.Content/assets/3699937/d89d7150-e0b3-4947-abeb-0e1f865ab6f8) 

![Figure: Endpoint Explorer showing the endoints between the old .NET Framework project and the new .NET Core project.](https://github.com/SSWConsulting/SSW.Rules.Content/assets/3699937/15377711-45a9-41dd-88b5-c555b64e6a87)

Use the `Upgrade` functionality to apply automatic code transformations and speed up the migration process.
In the best-case scenario, the controller has been fully ported across and does not require any manual work.
In most scenarios, you will need to review the controller and update any custom code that the Upgrade Assistant could not automatically transform.

![Figure: Upgrade Assistant progress upgrading a controller.](https://github.com/SSWConsulting/SSW.Rules.Content/assets/3699937/51fab5b1-eed3-48b9-8bd3-5a611e568b20)

### Create PBIs to identify the upcoming tasks

When a web project is heavily reliant on .NET Framework dependencies, the first step in gauging the effort required for a complete migration is to thoroughly examine these dependencies. This involves a detailed investigation, followed by the creation of PBIs for each dependency. These PBIs serve to accurately scope out the total effort that will be needed for the migration process.

Listed below are rules crafted to aid in the project migration process. Please ensure to incorporate only those rules that are applicable to your specific project.

- [Do you know how to migrate Global.asax to ASP.NET Core?](https://www.ssw.com.au/rules/know-how-to-migrate-global-asax-to-asp-net-core/)
- [Do you know how to migrate OWIN to ASP.NET Core?](https://www.ssw.com.au/rules/know-how-to-migrate-owin-to-asp-net-core/)
- [Do you know how to migrate Web.config to ASP.NET Core?](https://www.ssw.com.au/rules/know-how-to-migrate-owin-to-asp-net-core/)

# .NET Upgrade Assistant

By now, you should have wrapped up the entire migration including the web applications. It's the perfect moment to use the .NET Upgrade Assistant. It'll guide you in cleaning up the codebase. The ultimate goal is to eliminate all the old .NET Framework components and keep only the code and the most up-to-date NuGet packages for .NET 8.
