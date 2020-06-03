---
type: rule
title: Do you know how to add a version number to setup package in Advanced Installer?
uri: do-you-know-how-to-add-a-version-number-to-setup-package-in-advanced-installer
created: 2014-09-18T20:02:53.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 46
  title: Danijel Malik

---



<span class='intro'> <p class="p1">​Developers should&#160;add a version number at the end of the out package.&#160;E.g. SSWCodeAuditor_<span class="ssw15-rteStyle-Highlight">v14.0.0</span>.exe</p><p class="p1">Here is how you do it in Advanced Installer&#58;</p> </span>

<ol class="ol1"><li class="li1">​In the navigation pane look for 
      <strong>Media</strong></li><li class="li1">Choose 
      <strong>Configuration</strong> tab and click in 
      <strong>MSI name</strong> text box which is located under 
      <strong>Output</strong> section</li><li class="li1">Next to the text add 
      <span class="s1">[|ProductVersion]</span>. If the text-box is empty you may want to start it with 
      <span class="s1">[|ProductName]</span></li></ol><dl class="image"><dt><img src="/PublishingImages/installer-add-version-number.jpg" alt="" /></dt><dd>Figure​&#58; Advanced Installer - Add version to output package</dd></dl>


