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
A/B Testing is the process of testing different versions of an application on different users to gather empirical evidence about which version is better.

There are several ways this can be done...

<!--endintro-->

## Feature Flags (Recommended)
Feature flags are a modern way to toggle features for users. They are essentially a little bit of code that can be turned on and off at will. That means you can choose, when features are deployed, who gets them and can even turn them on or off at the flick of a switch.

Feature flags used to be a huge pain to deploy, but these days it is easy. Some of the major players include:
* [LaunchDarkly](https://launchdarkly.com/)
* [Azure App Configuration](https://docs.microsoft.com/en-us/azure/azure-app-configuration/overview)

Azure App Configuration is a favourite at SSW and there are some great tutorials that help developers get up and running in minutes:
* https://docs.microsoft.com/en-us/azure/azure-app-configuration/howto-feature-filters-aspnet-core
* https://docs.microsoft.com/en-us/azure/azure-app-configuration/use-feature-flags-dotnet-core?tabs=core5x 

## Azure Deployment Slots
Azure Deployment Slots are another way of doing A/B testing, you essentially deploy 2 versions of your app and then direct traffic to different versions.

See the [Microsoft Documentation](https://docs.microsoft.com/en-us/azure/app-service/deploy-staging-slots) for more info

## Azure FrontDoor
Azure FrontDoor is a newer offering that lets developers direct traffic to different versions of an app.

See the [Microsoft Documentation](https://docs.microsoft.com/en-us/azure/frontdoor/front-door-overview) for more info