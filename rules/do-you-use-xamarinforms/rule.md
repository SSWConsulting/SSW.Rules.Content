---
type: rule
archivedreason: 
title: Do you use Xamarin.Forms?
guid: 954d9b68-7185-472b-917c-407aa1a7df26
uri: do-you-use-xamarinforms
created: 2020-10-05T22:18:32.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 97
  title: Matt Goldman
related: []

---

Xamarin has evolved beyond simply being an abstraction of the platform native APIs for iOS, Android, and UWP. Where previously you could write shared business logic in C# but would have had to have written your UI in either Xamarin.Android or Xamarin.iOS, now you can write cross-platform UI code in Xamarin.Forms. Theoretically, it is possible to write your code only once and share 100% of the code you write across all target platforms, and at least 96% - see [Adam Cogan's blog post](https://adamcogan.com/2015/01/14/getting-96-code-reuse-with-xamarin-forms/).

<!--endintro-->
<dl class="badImage">&lt;dt&gt;<img src="xamarin-platform-bad.png" alt="xamarin-platform-bad.png" style="width:750px;">&lt;/dt&gt;<dd>Figure: Bad Example - Xamarin project targeting a single platform</dd></dl>
It is possible to implement beautiful and complex UI designs in Xamarin.Forms, especially given the rich ecosystem of plugins and templates available (see rule: Do you know where to find the best Xamarin resources?). Using drawing APIs like [SkiaSharp](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/graphics/skiasharp/) or the [new shapes and path APIs](https://devblogs.microsoft.com/xamarin/xamarin-forms-shapes-and-paths/) built into Xamarin.Forms (Note: this is an experimental feature) there is no UI that you can't implement cross-platform. Even so, 100% of the platform native APIs are exposed in Xamarin, so if you wanted to you could still implement any UI natively on each platform and call it using your shared code with a [custom renderer](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/custom-renderer/).
<dl class="goodImage">&lt;dt&gt;<img src="xamarin-platform-good.png" alt="xamarin-platform-good.png" style="width:750px;">&lt;/dt&gt;<dd>Figure: Good Example - cross-platform mobile app targeting iOS and Android with a shared codebase</dd></dl>
