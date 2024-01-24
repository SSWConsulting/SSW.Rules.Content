---
type: rule
archivedreason: At that moment there is no clear guidance from Microsoft; the future of UI automation testing is uncertain for .NET MAUI.
title: Do you conduct cross-platform UI Tests?
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

Any changes you make to your app risk breaking existing functionality. Having a suite of automated tests that you can run prior to any release reduces the risk of releasing a product with new features that don't work, or that breaks existing features. It also means that you can run these tests as part of your CI/CD pipeline, or with a dedicated testing infrastructure such as Xamarin Test Cloud in Visual Studio App Center, which runs your tests on real devices.

<!--endintro-->

Xamarin comes with a [built-in UI testing framework - Xamarin.UITest](https://docs.microsoft.com/en-us/appcenter/test-cloud/frameworks/uitest). This allows you to write UI tests that ensure your app's UI behaves as expected. UI tests in Xamarin.Forms follow the Page Object Pattern (POP), see: [Page Object Pattern and UITest Best Practices](https://docs.microsoft.com/en-us/events/xamarin-xamarin-developer-summit-2019/page-object-pattern-and-uitest-best-practices)
