---
type: rule
archivedreason: 
title: Do you know how to add a version number to setup package in Advanced Installer?
guid: 6721c81e-a1da-474a-8b1a-22d2fb16710b
uri: do-you-know-how-to-add-a-version-number-to-setup-package-in-advanced-installer
created: 2014-09-18T20:02:53.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 46
  title: Danijel Malik
related: []

---

Developers should add a version number at the end of the out package. E.g. SSWCodeAuditor\_<mark>v14.0.0</mark>.exe

Here is how you do it in Advanced Installer:

<!--endintro-->

1. In the navigation pane look for <br>       **Media**
2. Choose <br>       **Configuration** tab and click in <br>       **MSI name** text box which is located under <br>       **Output** section
3. Next to the text add <br>      [|ProductVersion]. If the text-box is empty you may want to start it with <br>      [|ProductName]

<dl class="image">&lt;dt&gt;<img src="installer-add-version-number.jpg" alt="">&lt;/dt&gt;<dd>Figure: Advanced Installer - Add version to output package</dd></dl>
