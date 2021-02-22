---
type: rule
archivedreason: 
title: Do you update your NuGet packages?
guid: 2fe6b65b-865c-4489-bcaf-bb70788b72b7
uri: do-you-update-your-nuget-packages
created: 2014-08-21T19:03:22.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Igor Goldobin
  url: https://ssw.com.au/people/igor-goldobin
related: []
redirects: []

---

NuGet packages can quickly get out of date and you may miss some important updates and/or features. Therefore, it is important to keep them up-to-date by updating on a regular basis. This can be done via the Package Manager UI or via the Package Manager Console.

<!--endintro-->


::: good  
![Figure: Good example -  NuGet packages via Package Manager are all up-to-date](nuget-update1.png)  
:::

![Figure: Update one package at a time eg. The command 'Update-Package EntityFramework' will update the one NuGet package via the Package Manager Console. Then test](nuget-update2.png)  

**\*\*WARNING\*\***

Some package updates may require extra care, such as packages containing content files or updated client script libraries. For example, the jQuery NuGet package update may break the UI of your web application due to some breaking changes introduced in a later version of the library (e.g. upgrading from v 1.10 to 2.0).

The impact of such upgrades can be greatly minimized by introducing Selenium or Coded UI tests into your solution. Running Selenium or Coded UI tests after performing a NuGet package update, can help to quickly identify problematic areas in your UI, which may be affected by the update.
