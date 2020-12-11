---
type: rule
archivedreason: 'Requested by Matt on RE: [SSW] Rules to Better Xamarin (mobile)'
title: Xamarin - Do you know the stuff to install?
guid: a167dacd-86d8-4ba7-8e6e-67a398b739a1
uri: xamarin---do-you-know-the-stuff-to-install
created: 2016-08-19T17:53:30.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

Installing Visual Studio is not enough.... There is another 2 hours plus of downloading and installing to get to your first successful Xamarin hello world app.

<!--endintro-->

### Step 1

Install VS 2015 + the Xamarin extension:  https://msdn.microsoft.com/en-us/library/mt613162.aspx
<dl class="image">&lt;dt&gt; <img src="xamarin-1.png" alt="xamarin-1.png"> &lt;/dt&gt;<dd>Figure: You need "C#/.NET (Xamarin v4.1.0)</dd></dl>
**Note:** Xamarin Studio doesn't exist on the PC anymore.

### Step 2 - Android SDK Manager (about 2 hours)

This one is painful...
<dl class="image">&lt;dt&gt; <img src="xamarin-2.png" alt="xamarin-2.png"> &lt;/dt&gt;</dl>
Then get all the ones that say "Installed" :
<dl class="image">&lt;dt&gt; <img src="xamarin-3.png" alt="xamarin-3.png"> &lt;/dt&gt;</dl>
### Step 3 - "Manage NuGet Packages for Solution" (about 30 minutes)  


Create a Blank App (xamarin.Forms Portable) project (this way it will trigger grabbing all extra stuff).
Check and ensure Nuget Packages are up to date .
<dl class="image">&lt;dt&gt; <img src="xamarin-4.png" alt="xamarin-4.png"> &lt;/dt&gt;</dl><dl class="image">&lt;dt&gt; <img src="xamarin-5.png" alt="xamarin-5.png"> &lt;/dt&gt;</dl>
### Step 4 - run the app


Actually run the application you’ve created. Ensure it builds. It won't =D well first time it often won't, if it does then congratulations you have got everything!
