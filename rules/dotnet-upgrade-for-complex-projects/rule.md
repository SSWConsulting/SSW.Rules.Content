---
type: rule
archivedreason: merged with a duplicate rule [https://www.ssw.com.au/rules/migration-plans/](/rules/migration-plans)
title: Do you know how to handle complex .NET migrations?
uri: dotnet-upgrade-for-complex-projects
authors:
  - title: Jernej Kavka (JK)
    url: https://ssw.com.au/people/jk
    img: https://github.com/SSWConsulting/SSW.People.Profiles/raw/main/Jernej-Kavka/Images/Jernej-Kavka-Profile.jpg
  - title: Gordon Beeming
    url: https://www.ssw.com.au/people/gordon-beeming
  - title: Yazhi Chen
    url: https://www.ssw.com.au/people/yazhi-chen
  - title: Thomas Iwainski
    url: https://www.ssw.com.au/people/thomas-iwainski/
related:
  - dotnet-upgrade-assistant
  - migrate-from-system-web-to-modern-alternatives
created: 2023-07-16T23:08:53.979Z
guid: 9de5ca88-a6aa-4fe5-af47-d6d2169cde86
---

There's not 1 single thing that makes a .NET project complex to migrate to the latest .NET Framework. Generally though it's a combination of the following:

* High complexity
* Lots of .NET Framework dependencies
* Outdated NuGet packages with no modern alternatives
* etc.

If your project doesn't meet any of the above criteria, you should consider using the [.NET Upgrade Assistant](https://dotnet.microsoft.com/en-us/platform/upgrade-assistant). You can read more about the tool at [Do you know how to modernize your .NET applications?](/dotnet-upgrade-assistant/) If the .NET Upgrade Assistant works for your project, you could save a significant amount of time. However, the level of success may vary across different projects.

While complex .NET migration has many steps and can be time-consuming, it offers significant benefits, including incremental migrations, improved risk management, and streamlined progress tracking.

The migration begins with an Evolutionary approach and then smoothly transitions to the Strangler Fig pattern, optimizing the advantages of both approaches. The Evolutionary approach ensures better compatibility with .NET 8 for the existing code, while the Strangler Fig pattern complete the full migration.

This strategy results in a codebase that functions within the old .NET Framework while progressively moving towards .NET 8. The majority of changes bring benefits to both platforms, allowing seamless deployment of these improvements to production. You can get more information about different migration approaches at [Do you know the different ways to modernize your application?](/modernize-your-app/)

Below you will find some tips and tricks to help you with your more complex migrations.

<!--endintro-->

# Preparation

### Upgrade the projects to use the sdk style csproj format

You can use the [try-convert](https://github.com/dotnet/try-convert) dotnet tool to convert your projects to the new sdk style csproj format. This will make it easier to upgrade the projects to the latest .NET Framework.

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

In all your project files change the `TargetFramework` to `TargetFrameworks`. You want to do this early on to enable a smoother flow later to not need unload and reload projects or have to close and reopen Visual Studio.

What this will allow you to do is add your target framework and compile the code. This will allow you to see what code is not compatible with the new framework and fix those issues while still developing/deploying your project in the current target framework.

```csharp
<TargetFrameworks>net472;net8.0</TargetFrameworks>
```

![Figure: Git changes for targeting to multiple target frameworks](target-to-multiple-TFMs.png)

# Upgrading

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

Outlined below are rules designed to assist in the project upgrade process during migration. Please note that the applicability of certain rules may vary based on individual project requirements.

* [Do you know how to migrate from System.Web to modern alternatives?](/migrate-from-system-web-to-modern-alternatives/)
* [Do you know how to migrate from EDMX to EF Core?](/migrate-from-edmx-to-ef-core/)

# Web application

There are several ways to migrate projects from ASP.NET to ASP.NET Core. We strongly recommend using the Strangler Fig pattern to incrementally migrate your project with [YARP](https://microsoft.github.io/reverse-proxy/).

### Create a side-by-side incremental project with [.NET Upgrade Assistant](https://dotnet.microsoft.com/en-us/platform/upgrade-assistant)

After you've [installed the .NET Upgrade Assistant extension](https://learn.microsoft.com/en-au/dotnet/core/porting/upgrade-assistant-install#install-the-visual-studio-extension),
Right-click on the project in the Solution Explorer window, and select Upgrade.

![Figure: Visual Studio context menu.](https://github.com/SSWConsulting/SSW.Rules.Content/assets/3699937/3303daaf-0dea-4b34-9f59-53fd55acf2ef)

A tab is opened which provides, based on your project type, different styles of upgrade:

* In-place project upgrade <br/>
This option upgrades your project without making a copy.

* Side-by-side project upgrade <br/>
Copies your project and upgrades the copy, leaving your original project alone.

* Side-by-side incremental <br/>
A good choice for complicated web apps. Upgrading from ASP.NET to ASP.NET Core requires quite a bit of work and at times manual refactoring. This mode puts a .NET project next to your existing .NET Framework project. If an endpoint is implemented in the .NET 8 project, any requests to that endpoint will be handled there and all other requests will be forwarded and handled by the .NET Framework project.

  This option lets you upgrade your ASP.NET app or class library project piece by piece.

On more complex projects you might find that Upgrade Assistant only provides you with the side-by-side incremental option. That is also the option that is covered here.

Once your app has been upgraded, a status screen is displayed which shows all of the artifacts related to your project that were associated with the upgrade. Each upgrade artifact can be expanded to read more information about the status. The following list describes the status icons:

* **Filled green checkmark**: The artifact was upgraded and completed successfully.
* **Unfilled green checkmark**: The tool didn't find anything about the artifact to upgrade.
* **Yellow warning sign**: The artifact was upgraded, but there's important information you should consider.
* **Red X**: The artifact was to be upgraded, but the upgrade failed.
  ![Figure: Example results from an Upgrade Assistant upgrade.](https://github.com/SSWConsulting/SSW.Rules.Content/assets/3699937/8dc7aaac-90cd-425b-bea6-5c74bea1ad57)

After the Upgrade Assistant completes the upgrade you will find a new project in the solution running .NET 8. Upgrade Assistant pre-configured the project and installed any necessary packages it required to run side-by-side using the Yarp proxy.

### Configure Yarp

 ![Figure: The new project architecture and request flow.](https://github.com/SSWConsulting/SSW.Rules.Content/assets/3699937/648be8b8-4c6a-47ae-99f0-9aa8c8d90432)

  As you can see in the above diagram, we want our UI to go through the .NET 8 project where the Yarp Proxy will either serve and fulfill the request or pass it through to the legacy project.

  When you look at the `Program.cs` in the newly created .NET 8 project, you will see that there is a configuration for the catch-all forwarder. You will need to update the configuration here with the address of your legacy project.

```csharp

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();
app.UseAuthorization();
app.UseSystemWebAdapters();

app.MapDefaultControllerRoute();
// This is responsible that requests are forwarded
// You need to change the configuration for ProxyTo to
// your legacy project's address

app.MapForwarder("/{**catch-all}", app.Configuration["ProxyTo"])
   .Add(static builder => ((RouteEndpointBuilder)builder).Order = int.MaxValue);

app.Run();

```

**Figure: Program.cs code showing the forward clause to the legacy project**

### Upgrading components using Upgrade Assistant

Once you have created the side-by-side project, select the project that needs migration and `right click` | `Upgrade` on it.

![Figure: Context menu on the project to be migrated.](https://github.com/SSWConsulting/SSW.Rules.Content/assets/3699937/3303daaf-0dea-4b34-9f59-53fd55acf2ef)

Upgrade Assistant will show you a Summary view and detect that the project is linked to your Yarp proxy.
You can also see the migration progress of your endpoints from .NET Framework to .NET as a pie chart.

![Figure: Upgrade Assistant's Summary page.](https://github.com/SSWConsulting/SSW.Rules.Content/assets/3699937/8564c9a7-b3a7-4b40-b002-be9c6fabcb16)

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

* [Do you know how to migrate Global.asax to ASP.NET Core?](/know-how-to-migrate-global-asax-to-asp-net-core/)
* [Do you know how to migrate OWIN to ASP.NET Core?](/know-how-to-migrate-owin-to-asp-net-core/)
* [Do you know how to migrate Web.config to ASP.NET Core?](/know-how-to-migrate-owin-to-asp-net-core/)

# .NET Upgrade Assistant

By now, you should have wrapped up the entire migration including the web applications. It's the perfect moment to use the .NET Upgrade Assistant. It'll guide you in cleaning up the codebase. The ultimate goal is to eliminate all the old .NET Framework components and keep only the code and the most up-to-date NuGet packages for .NET 8.
