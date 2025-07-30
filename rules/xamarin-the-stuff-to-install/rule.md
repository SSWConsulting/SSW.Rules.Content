---
seoDescription: Xamarin developers can quickly set up their environment by installing VS 2015 and the Xamarin extension, followed by the Android SDK Manager, NuGet package updates, and a blank app project creation.
type: rule
archivedreason: "Requested by Matt on RE: [SSW] Rules to Better Xamarin (mobile)"
title: Xamarin - Do you know the stuff to install?
guid: a167dacd-86d8-4ba7-8e6e-67a398b739a1
uri: xamarin-the-stuff-to-install
created: 2016-08-19T17:53:30.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - xamarin-do-you-know-the-stuff-to-install
---

Installing Visual Studio is not enough.... There is another 2 hours plus of downloading and installing to get to your first successful Xamarin hello world app.

<!--endintro-->

### Step 1

Install VS 2015 + the Xamarin extension: https://msdn.microsoft.com/en-us/library/mt613162.aspx

![Figure: You need "C#/.NET (Xamarin v4.1.0)](xamarin-1.png)

**Note:** Xamarin Studio doesn't exist on the PC anymore.

### Step 2 - Android SDK Manager (about 2 hours)

This one is painful...

![](xamarin-2.png)

Then get all the ones that say "Installed" :

![](xamarin-3.png)

### Step 3 - "Manage NuGet Packages for Solution" (about 30 minutes)

Create a Blank App (xamarin.Forms Portable) project (this way it will trigger grabbing all extra stuff).
Check and ensure Nuget Packages are up to date .

![](xamarin-4.png)

![](xamarin-5.png)

### Step 4 - run the app

Actually run the application you’ve created. Ensure it builds. It won't =D well first time it often won't, if it does then congratulations you have got everything!
