---
seoDescription: Do you use the MVVM pattern in your .NET MAUI or Xamarin apps?
type: rule
archivedreason:
title: Do you use the MVVM Pattern?
guid: 4c5adf6a-bb9c-44b3-845b-94cbd7fa9dda
uri: use-mvvm-pattern
created: 2020-10-07T22:03:25.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Goldman
    url: https://ssw.com.au/people/matt-goldman
  - title: Anton Polkanov
    url: https://ssw.com.au/people/anton-polkanov
related: []
redirects:
  - do-you-use-the-mvvm-pattern
---

.NET MAUI and Xamarin has been adhering to the MVVM design pattern since their inception. While .NET MAUI provides developers with additional flexibility by adopting the MVU pattern (see: [Introducing .NET Multi-platform App UI](https://devblogs.microsoft.com/dotnet/introducing-net-multi-platform-app-ui/)), MVVM remains a widely popular approach for architecting mobile applications.

<!--endintro-->

MVVM allows for loose coupling between data, business logic, and UI. In .NET MAUI, UI is usually defined in XAML (although you can declaratively define your UI in C# code too). Your UI is called a 'view' - a view can be a page or a UI element, although UI elements that are not complete pages are more often referred to as _controls_.

::: bad  
![Figure: Bad Example - Logic and properties are in the code behind, which decreases maintainability and testability](mvvm-bad.png)  
:::

::: good  
![Figure: Good Example - Values are bound to properties of the ViewModel, and actions are bound to Commands in the ViewModel](mvvm-good.png)  
:::

.NET MAUI supports MVVM out of the box, but there are several MVVM frameworks available that enhance this functionality. For example, some MVVM frameworks support _"convention over configuration"_, allowing you to just code your View and ViewModel and let the framework hook them up for you. Some include:

- **[MVVM Toolkit](https://learn.microsoft.com/en-us/dotnet/communitytoolkit/mvvm/):** MVVM Toolkit is maintained and published by Microsoft. The framework significantly reduces the amount of boilerplate code by applying Roslyn source generators.
- **[Prism](https://github.com/PrismLibrary/Prism):** Prism is an MVVM framework that was developed initially for WPF but has since been ported to Xamarin Forms and then to .NET MAUI. It is stable and mature. For a long time Prism sustained itself through donations, with the founders contributing significant time and effort for free. However, they eventually shifted to a [paid model](https://prismlibrary.com/#pricing) (with a free option) to sustain and further develop the library.
- **[FreshMVVM](https://github.com/rid00z/FreshMvvm):** FreshMVVM is a framework that was built from the ground up specifically for Xamarin Forms and also migrated to .NET MAUI. It is open-source and maintained by a Microsoft MVP.
- **[MVVMLight](https://github.com/lbugnion/mvvmlight):** This framework, built especially for Xamarin, was archived in 2021 in favour of its successor, the MVVM Toolkit.
