---
seoDescription: Optimize Android builds and start-up times by leveraging .NET MAUI's native layer optimizations, such as AAB, R8, and AAPT2, and .NET-specific optimizations like Concurrent GC, AOT, LLVM, and IL Stripping.
type: rule
archivedreason:
title: Do you optimize your Android builds and start-up times?
guid: fa142c74-97bb-4150-be0d-abb997ea9d30
uri: optimize-android-builds-and-start-up-times
created: 2020-10-08T23:04:23.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Goldman
    url: https://ssw.com.au/people/matt-goldman
  - title: Anton Polkanov
    url: https://ssw.com.au/people/anton-polkanov
related: []
redirects:
  - do-you-optimise-your-android-builds-and-start-up-times
---

.NET MAUI provides several ways to optimize an Android application. Some of them complement each other while others can be mutually exclusive. It's important to understand what options you have at hands and how they affect your application.

<!--endintro-->

When it comes to app optimizations, developers usually try to strike the right balance between:

- App build time
- App size
- App performance (execution speed and memory)

Quite often improvements in one area lead to degradation in another. In most cases it's a tradeoff which developers need to take depending on their circumstances. Different Debug and Release configurations partially address this problem, but may lead to configuration-specific bugs.

.NET MAUI Android combines 2 worlds - native Android and .NET, which means that optimization can be performed in both worlds.

### Native Layer optimizations

These optimizations are not specific to .NET MAUI and are used in other cross-platform frameworks or native Android development.

#### Use AAB (Android App Bundle or just App Bundle)

❌ Debug  
✅ Release

.aab files are used only for publishing on Google Play and cannot be installed on Android devices. AAB allows smaller builds to be targeted to individual hardware specifications by packaging only required resources (e.g. icons, images). It also deligates app signing to Google Play.

App Bundle [is mandatory for Google Play since 2021](https://developer.android.com/guide/app-bundle).

#### Use R8 (instead of ProGuard)

❌ Debug
✅ Release

R8 is a code shrinker and obfuscator which processes **only** native java/kotlin code. It doesn't touch your .NET code.

As R8 increases build time it's only recommented for Release configuration.

#### Use AAPT2 (instead of AAPT)

✅ Debug  
✅ Release

AAPT2 parses, indexes, and compiles the resources into a binary format that is optimized for the Android platform.

### .NET Layer optimizations

These optimizations are .NET MAUI specific.

#### Concurrent GC

✅ Debug  
✅ Release

Concurrent GC improves app performance by collecting garbage alongside the running program. This approach prevents program from freeze which happen for non-concurrent GCs.

#### AOT

❌ Debug  
✅ Release

Whereas iOS enforces AOT (ahead of time) compilation, Android supports (and uses by default) JIT (just in time) compilation which happens at runtime, but AOT can be enabled on Android to improve performance. As the code will be pre-compiled, it comes at a cost of significantly larger app size and longer build times.

There are several types of AOT:

- Full AOT (comes from Mono)
- Profiled AOT (comes from Mono, a.k.a Startup Tracing)
- Native AOT (comes from .NET; not available for Android, but .NET MAUI team is experimenting with iOS)

Profiled AOT provides finer control over the trade-offs between Android APK size and startup time as compared to the Full AOT compilation option.
Instead of compiling as much of the app as possible to unmanaged code, Profiled AOT compiles only a particular set of managed methods that represent the most expensive parts of application startup in a blank app. This approach consumes less space in the APK compared to the Full AOT compilation option while still providing similar app startup performance improvements.

AOT increases app size and build time (especially Full AOT). Recommended for Release.

#### LLVM

❌ Debug  
✅ Release

Mono support 2 compilation engines, a fast, JIT-friendly compilation engine which does not generate very fast code, and a slower compilation engine based on the LLVM optimizing compiler that produces superior code.

When set LLVM will be used when Ahead-of-Time compiling assemblies into native code. If Full AOT is not enabled, this property is **ignored**.

Increases build time. Recommended for Release.

#### IL Stripping

❌ Debug  
✅ Release

$(AndroidStripILAfterAOT) removes IL code after performing AOT as it is no longer required.

---

### More information

- [Optimize Xamarin Android Builds](https://devblogs.microsoft.com/xamarin/optimize-xamarin-android-builds)
- [IL Stripping](https://devblogs.microsoft.com/dotnet/dotnet-8-performance-improvements-in-dotnet-maui/#androidstripilafteraot)
- [AOT and LLVM](https://devblogs.microsoft.com/dotnet/performance-improvements-in-dotnet-maui/#aot-and-llvm#aot-everything)
- [Profiled AOT](https://devblogs.microsoft.com/xamarin/faster-startup-times-with-startup-tracing-on-android)
- [Profiled ATO Release Notes](https://learn.microsoft.com/en-us/xamarin/android/release-notes/9/9.4#option-to-compile-app-startup-methods-to-unmanaged-code)
- [Mono AOT doc](https://www.mono-project.com/docs/advanced/aot)
- [Mono LLVM doc](https://www.mono-project.com/docs/advanced/mono-llvm)
