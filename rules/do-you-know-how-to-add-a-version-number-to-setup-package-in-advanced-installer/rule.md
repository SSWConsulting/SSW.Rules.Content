---
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


<p class="p1">​Developers should add a version number at the end of the out package. E.g. SSWCodeAuditor_<span class="ssw15-rteStyle-Highlight">v14.0.0</span>.exe</p><p class="p1">Here is how you do it in Advanced Installer:</p>
<br><excerpt class='endintro'></excerpt><br>
<ol class="ol1"><li class="li1">​In the navigation pane look for 
      <strong>Media</strong></li><li class="li1">Choose 
      <strong>Configuration</strong> tab and click in 
      <strong>MSI name</strong> text box which is located under 
      <strong>Output</strong> section</li><li class="li1">Next to the text add 
      <span class="s1">[|ProductVersion]</span>. If the text-box is empty you may want to start it with 
      <span class="s1">[|ProductName]</span></li></ol><dl class="image"><dt><img src="installer-add-version-number.jpg" alt="" /></dt><dd>Figure​: Advanced Installer - Add version to output package</dd></dl>


