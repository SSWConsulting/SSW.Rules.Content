---
seoDescription: Conducting cross-platform UI tests for .NET MAUI applications with Appium and NUnit.
type: rule
title: Testing - Do you conduct cross-platform UI Tests?
guid: 8949d1b5-ff9d-4ffc-be57-87976af5b7c3
uri: conduct-cross-platform-ui-tests
created: 2020-10-07T23:30:41.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Goldman
    url: https://ssw.com.au/people/matt-goldman
related: []
redirects:
  - do-you-conduct-cross-platform-ui-tests
---

Any changes you make to your app risks breaking existing functionality. Having a suite of automated tests that you can run prior to any release reduces the risk of releasing a product with new features that don't work, or that breaks existing features. It also means that you can run these tests as part of your CI/CD pipeline.

<!--endintro-->

Every control in .NET MAUI exposes the `AutomationId` property, which allows a UI testing framework to find and interact with contols. See [how you can write and run your UI tests with Appium](https://learn.microsoft.com/en-us/samples/dotnet/maui-samples/uitest-appium-nunit/).

Unlike Xamarin, .NET MAUI doesn't come with a [built-in UI testing framework - Xamarin.UITest](https://docs.microsoft.com/en-us/appcenter/test-cloud/frameworks/uitest). Technically, you still can use Xamarin.UITest with .NET MAUI, but only to unblock your team to migrate from Xamarin. For details, [see this video by Gerald Versluis](https://www.youtube.com/watch?v=0c2U-TzmTnQ).
