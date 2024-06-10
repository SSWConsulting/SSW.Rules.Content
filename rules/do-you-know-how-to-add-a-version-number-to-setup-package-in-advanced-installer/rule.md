---
seoDescription: Add a version number to your setup package in Advanced Installer by modifying the MSI name configuration and adding [ProductVersion] or [ProductName].
type: rule
archivedreason:
title: Do you know how to add a version number to setup package in Advanced Installer?
guid: 6721c81e-a1da-474a-8b1a-22d2fb16710b
uri: do-you-know-how-to-add-a-version-number-to-setup-package-in-advanced-installer
created: 2014-09-18T20:02:53.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Danijel Malik
    url: https://ssw.com.au/people/danijel-malik
related: []
redirects: []
---

Developers should add a version number at the end of the out package. E.g. SSWCodeAuditor\_<mark>v14.0.0</mark>.exe

Here is how you do it in Advanced Installer:

<!--endintro-->

1. In the navigation pane look for
   **Media**
2. Choose
   **Configuration** tab and click in
   **MSI name** text box which is located under
   **Output** section
3. Next to the text add
   [|ProductVersion]. If the text-box is empty you may want to start it with
   [|ProductName]

![Figure: Advanced Installer - Add version to output package](installer-add-version-number.jpg)
