---
seoDescription: Do you build cross-platform apps? Learn about the benefits and approaches to building installable binary apps that run on multiple platforms.
type: rule
title: Do you build cross-platform apps?
uri: build-cross-platform-apps
authors:
  - title: Matt Goldman
    url: https://www.ssw.com.au/people/matt-goldman
related:
  - why-react-is-great
  - maui-cross-platform
created: 2022-08-17T20:12:08.779Z
guid: 8d03f974-6e64-4d65-a3b2-04d7e78a52f1
---

::: img-medium
![Figure: There are many cross-platform technology options available](cross-platform-options.png)
:::

If you're building installable binary apps (as opposed to web apps), it makes sense to use a cross-platform framework so that you don’t need to maintain multiple code bases.

Writing apps in a single-platform language or framework can lead to fragmentation and technical debt, while writing your app once using a cross-platform technology is the best way to apply [DRY](/do-you-look-for-duplicate-code) to your app as a whole.

<!--endintro-->

`youtube: https://www.youtube.com/embed/2IoFI3tCN5g`

### Cross-platform approaches

There are two approaches to building cross-platform apps. One is to write a single page application (SPA) and use a wrapper technology like Cordova or Electron to turn your SPA into an installable app. This is a good approach if you already have a fully functioning web app and want it to be available for users to install via an app store.

The other approach is to use an API that is a single, cross-platform abstraction that compiles to native code executable on your target platforms. This is the approach taken by .NET MAUI (previously Xamarin), Flutter, and React Native.

### When to use a web wrapper

Use a web wrapper, like Cordova or Electron, if your SPA is already built and offers all (or almost all) of the functionality that you want your app to provide.

### When to use an abstracted cross-platform API

Web wrapper technologies are good for apps that also work as web apps (and potentially already exist as web apps), but they also suffer from some of the limitations of web apps.

If you need multi-threading, or access to hardware features, platform or operating system APIs or system processes, then using an abstracted cross-platform API is a better option.

### Which cross-platform framework to choose

If you need access to specific platform APIs, you may not find them available in the web wrapper options (and almost certainly not via 1st party support). In this case, you could rule out using a web wrapper.

If you already have a .NET development team and your solution is built on .NET, it makes sense to use **[.NET MAUI](https://docs.microsoft.com/en-us/dotnet/maui/what-is-maui)**. .NET MAUI lets you write your UI in XAML or Blazor, so if you already have a Blazor web solution, you can share your UI controls in a Razor Class Library. You could also share other things like DTOs and authentication logic between Blazor, ASP.NET Core, and .NET MAUI apps.

If you already have a strong React team, it may make sense to use **[React Native](https://reactnative.dev/)**. There is a bit of a learning curve to go from React to React Native, but it still builds upon your team’s existing skills.

Choose **[Flutter](https://flutter.dev/)** if you like Dart.
