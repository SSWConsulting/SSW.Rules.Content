---
type: rule
title: Migrating Web Apps to .NET
uri: migrating-web-apps-to-dotnet
authors:
  - title: Luke Cook
    url: https://ssw.com.au/people/luke-cook
  - title: Gordon Beeming
    url: https://www.ssw.com.au/people/gordon-beeming
  - title: Yazhi Chen
    url: https://www.ssw.com.au/people/yazhi-chen
  - title: Tom Iwainski
    url: https://www.ssw.com.au/people/tom-iwainski
  - title: Jernej Kavka
    url: https://www.ssw.com.au/people/jk
related:
  - dotnet-upgrade-assistant
  - migrate-from-system-web-to-modern-alternatives
  - migration-plans
  - modernize-your-app
created: 2023-09-12T23:08:53.979Z
guid: 75d6efc2-a8b8-4e0d-8310-ffa076c2bd27
---

The differences between a web app built with ASP.NET Framework and one built with ASP.NET Core are immense. The entire request pipeline underwent significant changes, and can often be impossible to migrate in-place. So how can you tackle these challenges the right way?

<!--endintro-->

## To YARP, or not to YARP

There exists, somewhere, a line that separates the "big bang" and "stranger fig" approach as being the *recommended* way to tackle web app migrations. While this decision point is unique to every project, you can examine a couple of metrics to help guide your decision.

* How many Sprints do you estimate the migration work will take?
* Will feature development continue during the migration process?
* Do you have plenty of leeway on both of the above?

If your [migration plan](https://ssw.com.au/rules/migration-plans) is solid, you should have a pretty clear idea of the effort involved in migrating your web app. If you're confident that you can get the migration done in a reasonable timeline, *and* you can implement a feature-freeze during that time, opting for the Big Bang approach may be a reasonable option.

If, however, you know that the migration is going to take a long time, or there are other developers/teams that will be working on other, non-migration work (e.g. feature development), then adopting the Strangler Fig pattern with YARP is often a better choice, and one that we at SSW have had great success with.

### Create a side-by-side Web App project

The first step is to create a brand new ASP.NET Core web application, where you will be migrating your pages/endpoints into incrementally.

The best way to do this is via the [.NET Upgrade Assistant](https://dotnet.microsoft.com/en-us/platform/upgrade-assistant).

This will create a new .NET 8 project *and* include YARP. For functionalities that have not yet been migrated, YARP will redirect them to the .NET Framework web application.

### Configure YARP

The next port of call is to configure YARP (Yet Another Reverse Proxy). This is the slice of code that will determine whether a request should be sent to your new ASP.NET Core web app (for routes that have been migrated) or your old .NET Framework web app (for the routes that have not yet been migrated).

Here's a quick look at a sample YARP route config:

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

**Figure: Example code for setting up different paths within YARP's configuration**

### Upgrading components using Upgrade Assistant

Once you have created the side-by-side project, select the project that needs migration and `right click` | `Upgrade` on it.

![Figure: Context menu on the project to be migrated.](https://github.com/SSWConsulting/SSW.Rules.Content/assets/3699937/3303daaf-0dea-4b34-9f59-53fd55acf2ef)

Upgrade Assistant will show you a Summary view and detect that the project is linked to your Yarp proxy.
You can also see the migration progress of your endpoints from .NET Framework to .NET as a pie chart.

![Figure: Upgrade Assistants Summary page](https://github.com/SSWConsulting/SSW.Rules.Content/assets/3699937/8564c9a7-b3a7-4b40-b002-be9c6fabcb16)

From here you can explore your endpoints through the `Endpoint explorer`, which will also indicate what endpoints have already been migrated and which ones are still outstanding.
The chain icon indicates that this endpoint has been migrated and is linked between the controller in the old project and the controller in the Yarp proxy project. ![Figure: Chain Icon](https://github.com/SSWConsulting/SSW.Rules.Content/assets/3699937/d89d7150-e0b3-4947-abeb-0e1f865ab6f8)

![Figure: Endpoint Explorer showing the endoints between the old .NET Framework project and the new .NET Core project](https://github.com/SSWConsulting/SSW.Rules.Content/assets/3699937/15377711-45a9-41dd-88b5-c555b64e6a87)

Use the `Upgrade` functionality to apply automatic code transformations and speed up the migration process.
In the best-case scenario, the controller has been fully ported across and does not require any manual work.
In most scenarios, you will need to review the controller and update any custom code that the Upgrade Assistant could not automatically transform.

![Figure: Upgrade Assistant progress upgrading a controller](https://github.com/SSWConsulting/SSW.Rules.Content/assets/3699937/51fab5b1-eed3-48b9-8bd3-5a611e568b20)

### Create PBIs to identify the upcoming tasks

When a web project is heavily reliant on .NET Framework dependencies, the first step in gauging the effort required for a complete migration is to thoroughly examine these dependencies. This involves a detailed investigation, followed by the creation of PBIs for each dependency. These PBIs serve to accurately scope out the total effort that will be needed for the migration process.

Listed below are rules crafted to aid in the project migration process. Please ensure to incorporate only those rules that are applicable to your specific project.

* [Do you know how to migrate Global.asax to ASP.NET Core?](/know-how-to-migrate-global-asax-to-asp-net-core/)
* [Do you know how to migrate OWIN to ASP.NET Core?](/know-how-to-migrate-owin-to-asp-net-core/)
* [Do you know how to migrate Web.config to ASP.NET Core?](/know-how-to-migrate-web-config-to-asp-net-core/)
