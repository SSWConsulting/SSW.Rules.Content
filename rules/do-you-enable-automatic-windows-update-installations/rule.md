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


<p class="p1">​M​icrosoft Update is a service that allows for the periodic patching of system files to address known issues with Microsoft products. Originally called Windows Update, it was specifically focused on Operating System patches for Windows but&#160;has been expanded to include all Microsoft products and the name has changed to Microsoft Update, allowing the automated patching of non-OS software such as Internet Explorer and Microsoft Office.&#160;<br><br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>​<span style="line-height&#58;1.6;">It is important to keep your machine up-to-date, but Windows Update Automatic installation can be somewhat intrusive to your work flow. There is nothing worse than getting Windows Updates installing during important presentation. You should set Windows Updates to be installed manually.</span></p><p><span style="line-height&#58;1.6;"><strong>​NOTE&#58; This is only for client machines, Windows Update for Servers should be handled differently see&#58;&#160;</strong><a href="/do-you-use-group-policy-to-manage-your-windows-update-policy"><strong>Do you use Group Policy to manage your Windows Update Policy?</strong></a><br><strong></strong><br></span></p><p class="p1">Go to <strong>Start</strong><strong>&#160;| Windows Update Settings&#160;| Advanced Options </strong>and set&#160;<strong>Restart this device as soon as possible...&#160;</strong>to&#160;<strong>Off&#160;</strong>and&#160;<strong>Update Notifications&#160;</strong>to&#160;<strong>​On.</strong><br></p><dl class="badImage"><dt><br><img src="/SiteAssets/do-you-disable-automatic-windows-update-installations/WindowsUpdateBadExample.jpg" alt="WindowsUpdateBadExample.jpg" style="margin&#58;5px;width&#58;623px;height&#58;510px;" /><br></dt><dd>Figure&#58; Bad example – Install updates automatically</dd></dl><dl class="goodImage"><dt><br>​<img src="/PublishingImages/Windows%20Update%20Good%20Example.jpg" alt="Windows Update Good Example.jpg" style="margin&#58;5px;width&#58;623px;height&#58;510px;" /><br></dt><dd>Figure&#58; Good example – Download updates but let user choose whether to install them</dd></dl><p class="p1">If you have a system administrator who manages your organization’s infrastructure, it is recommended to get you system administrator to push this setting via group policy.​​<br></p><dl class="goodImage"><dt><img src="/PublishingImages/win-update-3.jpg" alt="" /><br></dt><dd>Figure&#58; Better example – Windows Updates setting is pushed to *ALL* users via group policy<br><br><br></dd></dl>


