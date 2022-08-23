---
type: rule
title: Do you build cross-platform apps?
uri: build-cross-platform-apps
authors:
  - title: Matt Goldman
    url: https://www.ssw.com.au/people/matt-goldman
created: 2022-08-17T20:12:08.779Z
guid: 8d03f974-6e64-4d65-a3b2-04d7e78a52f1
---
If you’re building installable binary apps (as opposed to web apps), it makes sense to use a cross-platform framework so that you don’t need to maintain multiple code bases. 

Writing apps in a single-platform language or framework can lead to fragmentation and technical debt, while writing your app once using a cross-platform technology is the best way to apply [DRY](/do-you-look-for-duplicate-code) to your app as a whole.
  
<!--endintro-->
 
### Cross-Platform Approaches
 
There are two approaches to building cross-platform apps. One is to write a SPA and use a wrapper technology like Cordova or Electron to turn your SPA into an installable app. This is a good approach if you already have a fully functioning web app and want it to be available for users to install via an app store.
 
The other approach is to use an API that is a single, cross-platform abstraction that compiles to native code that is executable on your target platforms. This is the approach taken by .NET MAUI (previously Xamarin), Flutter and React Native.
 
### When to use a web wrapper
 
Use a web wrapper, like Cordova or Electron, if your SPA is already built and offers all (or almost all) of the functionality that you want your app to provide already.
 
### When to use an abstracted cross-platform API
 
Web wrapper technologies are good for apps that also work as web apps (and potentially already exist as web apps), but they also suffer from some of the limitations of web apps. If you need multi-threading, or access to hardware features, platform or operating system APIs, or system processes, using an abstracted cross-platform API is a better option.
 
### Which cross-platform framework to choose
 
If you need access to specific platform APIs, you may not find them available in the web wrapper options (and almost certainly not via 1st party support). In this case you could rule these out.
 
If you already have a .NET development team and your solution is built on .NET, it makes sense to use .NET MAUI. 

.NET MAUI lets you write your UI in XAML or Blazor, so if you already have a Blazor web solution, you can share your UI controls in a Razor Class Library. You could also share other things like DTOs and authentication logic between Blazor, ASP.NET Core, and .NET MAUI apps.
 
If you already have a strong React team, it may make sense to use React Native. There is still a bit of a learning curve to go from React to React Native, but it still builds upon your team’s existing skills.
 
Choose Flutter if you like Dart.
