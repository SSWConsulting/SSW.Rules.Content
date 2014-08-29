---
type: rule
archivedreason: 
title: Do you enable automatic Windows Update Installations?
guid: 28c099df-7d3c-42d7-8578-01aa41086c06
uri: do-you-enable-automatic-windows-update-installations
created: 2014-08-29T20:08:15.0000000Z
authors:
- id: 40
  title: Igor Goldobin
- id: 47
  title: Stanley Sidik
related: []

---


<p class="p1">Microsoft automatic updates can be dangerous.&#160;</p><p class="p1">Microsoft Update is a service that allows for the periodic patching of system files to address known issues with Microsoft products. Originally called Windows Update, it was specifically focused on Operating System patches for Windows. More recently however, it has been expanded to include all Microsoft products and the name has changed to Microsoft Update, allowing the automated patching of non-OS software such as Internet Explorer and Microsoft Office.&#160;</p>
<br><excerpt class='endintro'></excerpt><br>
<p>​<span style="line-height&#58;1.6;">It is important to keep your machine up-to-date, but Windows Update Automatic installation can be somewhat intrusive to your work flow. There is nothing worse than getting Windows Updates installing during important presentation. You should set Windows Updates to be installed manually.</span></p><p class="p1">Go to 
   <strong>Control Panel | Windows Update | Change Settings </strong>and set updates to 
   <b>Download updates but let me choose whether to install them</b>.</p><dl class="badImage"><dt><img src="/PublishingImages/win-update-1.jpg" alt="" /></dt><dd>Figure&#58; Bad example – Install updates automatically</dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/win-update-2.jpg" alt="" /></dt><dd>Figure&#58; Good example – Download updates but let user choose whether to install them</dd></dl><p class="p1">If you have a system administrator who manages your organization’s infrastructure, it is recommended to get you system administrator to push this setting via group policy.</p><dl class="goodImage"><dt><img src="/PublishingImages/win-update-3.jpg" alt="" /></dt><dd>Figure&#58; Better example – Windows Updates setting is pushed to *ALL* users via group policy</dd></dl>


