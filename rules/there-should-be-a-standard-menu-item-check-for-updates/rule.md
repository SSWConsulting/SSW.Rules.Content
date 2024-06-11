---
seoDescription: Easily keep your system up to date by checking for updates within the Help menu.
type: rule
title: Do you have a standard menu item "Check for Updates"?
uri: there-should-be-a-standard-menu-item-check-for-updates
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T00:22:00.000Z
guid: 315ea8d3-b4b5-491c-938f-784f5a5d4c48
---

A standard menu item "Check for Updates" should be available in the Help menu. Its function is running SSW Diagnostics to check updates and keep the system up to date easily. More on [Do you allow users to check for a new version easily?](/do-you-allow-users-to-check-for-a-new-version-easily)

<!--endintro-->

![Figure: "Check for Updates" menu item](checkforupdatesmenu.gif)

Here's the code to run Diagnostics:

```cs
System.Diagnostics.Process.Start("http://us.ssw.com.au/ssw/diagnostics/download/SSWDiagnostics.application#SSWDiagnostics.application");
```
