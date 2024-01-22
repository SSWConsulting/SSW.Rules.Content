---
type: rule
title: Do you use .NET MAUI (was Xamarin)?
uri: use-net-maui
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Goldman
    url: https://ssw.com.au/people/matt-goldman
related: []
redirects:
  - do-you-use-xamarin-forms
  - use-xamarin-forms
created: 2020-10-05T22:18:32.000Z
archivedreason: Replaced by [https://www.ssw.com.au/rules/build-cross-platform-apps](/rules/build-cross-platform-apps)
guid: 954d9b68-7185-472b-917c-407aa1a7df26
---
Xamarin has evolved beyond simply being an abstraction of the platform native APIs for iOS, Android, and UWP. It is now the .NET Multi-platform App UI (.NET MAUI).

Where previously you could write shared business logic in C# but needed to write your UI in either Xamarin.Android or Xamarin.iOS, now you can write cross-platform UI code in a single .NET MAUI project.

<!--endintro-->

![](maui_blazor_mobile_desktop_web.png)

Theoretically, it is possible to write your code only once and share 100% of the code you write across all target platforms - see [Adam Cogan's blog post](https://adamcogan.com/2015/01/14/getting-96-code-reuse-with-xamarin-forms/) for a case study of achieving 96% code reuse.

::: bad
![Figure: Bad example - Xamarin project targeting a single platform](xamarin-platform-bad.png)
:::

It is possible to implement beautiful and complex UI designs in .NET MAUI, especially given the rich ecosystem of plugins and templates available (see rule: [Do you know where to find the best Xamarin resources?](/the-best-xamarin-resources)). You can use drawing APIs like [Microsoft.Maui.Graphics](https://docs.microsoft.com/en-us/dotnet/maui/user-interface/graphics/) or the [new .NET MAUI Community Toolkit](https://docs.microsoft.com/en-us/dotnet/communitytoolkit/maui/).

::: good
![Figure: Good example - Cross-platform .NET MAUI app targeting multiple platforms with a shared codebase](single-project-good.png)
:::

![Figure: .NET MAUI allows you to use C# and XAML to build your apps from a rich toolkit of more than 40 controls, layouts, and pages](controls_sample.png)
