---
type: rule
archivedreason: 
title: Do you know how to build for the right platforms?
guid: afa00ad3-8d6f-4d1b-9bad-df8f65d0ea20
uri: how-to-build-for-the-right-platforms
created: 2020-10-05T23:10:29.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Matt Goldman
  url: https://ssw.com.au/people/matt-goldman
related: []
redirects:
- do-you-know-how-to-build-for-the-right-platforms

---

Picking the right development environment is important, and which platforms you want to target will influence that decision.

<!--endintro-->

![Figure: The platforms you can target with each development environment – in most situations a Mac works best](dev-environments.png)  

**Note:** More platforms are coming in 2021 when Xamarin.Forms evolves into MAUI, see: [Introducing .NET Multi-platform App UI](https://devblogs.microsoft.com/dotnet/introducing-net-multi-platform-app-ui/).

If you want to develop for Android, wearOS, or Tizen, you can use Visual Studio on either Windows or macOS. If you want to target UWP, you must use Windows. If you want to develop for iOS, tvOS, macOS, or watchOS, you can now develop using Windows or Mac (using Hot Restart on Windows) but must use a Mac to publish your app to the App Store. If you want to target all these platforms you will need access to both Windows and Mac.

**Tip:** If you use a Mac you can run Windows through virtualization, using VMware Fusion, Parallels or VirtualBox. If you use Windows, there are cloud-based Mac services you can use for your Apple OS builds.
