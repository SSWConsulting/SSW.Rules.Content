---
type: rule
title: Do you know the best way to do A/B testing?
uri: a-b-testing
authors:
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
created: 2022-04-20T05:56:17.498Z
guid: bb49a520-59fa-4190-b19e-b70a6b450975
---
A/B Testing is the process of testing different versions of an application on different users to gather empirical evidence to learn which version is better. 

Using A/B Testing enables you to get features tested and when used effectively means that **a bug will never be deployed to 100% of users.** Generally, new features should be tested on 20% of users and rolled out to others once they are reliable.

`youtube: https://www.youtube.com/embed/v=zFMgpxG-chM`

**Video: What is A/B Testing? | Data Science in Minutes** 

There are several ways this can be done...

<!--endintro-->

## Feature Flags (Recommended)

Feature flags are a modern way to toggle features for users. They are essentially a little bit of code that can be turned on and off at will. That means you can choose, when features are deployed and who gets them.

Feature flags are often implemented by developers writing their own code. However, there are better solutions today:
* [LaunchDarkly](https://launchdarkly.com/) 

    * [Video interview](https://tv.ssw.com/ndc-sydney-2017-ask-me-anything-with-adam-cogan-and-edith-harbaugh-launchdarkly-tripit-devops/) of LaunchDarkly CEO Edith Harbaugh
* [Azure App Configuration](https://docs.microsoft.com/en-us/azure/azure-app-configuration/overview) is the recommended solution and there are some great tutorials that help developers get up and running in minutes:

    * [Use feature filters to enable conditional feature flags](https://docs.microsoft.com/en-us/azure/azure-app-configuration/howto-feature-filters-aspnet-core)
    * [Tutorial: Use feature flags in an ASP.NET Core app](https://docs.microsoft.com/en-us/azure/azure-app-configuration/use-feature-flags-dotnet-core)

## Azure Deployment Slots

[Azure Deployment Slots](https://docs.microsoft.com/en-us/azure/app-service/deploy-staging-slots) are another way of doing A/B testing, you essentially deploy 2 versions of your app and then direct traffic to different versions.

## Azure FrontDoor

[Azure FrontDoor](https://docs.microsoft.com/en-us/azure/frontdoor/front-door-overview) is an offering that lets developers direct traffic to different versions of an app.