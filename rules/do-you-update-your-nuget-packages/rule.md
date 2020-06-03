---
type: rule
title: Do you update your NuGet packages?
uri: do-you-update-your-nuget-packages
created: 2014-08-21T19:03:22.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 40
  title: Igor Goldobin

---



<span class='intro'> <p>NuGet packages can quickly get out of date and you may miss some important updates and/or features. Therefore, it is important to keep them up-to-date by updating on a regular basis. This can be done via the Package Manager UI or via the Package Manager Console.&#160;</p> </span>

<dl class="goodImage"><dt>​​<img src="/PublishingImages/nuget-update1.png" alt="nuget-update1.png" style="width&#58;550px;" /></dt><dd>Figure&#58; Good example -  NuGet packages via Package Manager are all up-to-date</dd></dl><dl class="image"><dt>​​<img src="/PublishingImages/nuget-update2.png" alt="nuget-update2.png" /></dt><dd>Figure&#58; Update one package at a time eg. The command 'Update-Package EntityFramework' will update the one NuGet package via the Package Manager Console. Then test​   </dd></dl><p>
   <strong style="color&#58;red;">**WARNING**</strong></p><p>Some package updates may require extra care, such as packages containing content files or updated client script libraries. For example, the jQuery NuGet package update may break the UI of your web application due to some breaking changes introduced in a later version of the library (e.g. upgrading from v 1.10 to 2.0).&#160;​​</p><p>The impact of such upgrades can be greatly minimized by introducing Selenium or Coded UI tests into your solution. Running Selenium or Coded UI tests after performing a NuGet package update, can help to quickly identify problematic areas in your UI, which may be affected by the update.&#160;</p>


