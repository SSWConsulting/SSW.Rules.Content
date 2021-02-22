---
type: rule
archivedreason: 
title: Do you enable automatic Windows Update Installations?
guid: 28c099df-7d3c-42d7-8578-01aa41086c06
uri: do-you-disable-automatic-windows-update-installations
created: 2014-08-29T20:08:15.0000000Z
authors:
- title: Igor Goldobin
  url: https://ssw.com.au/people/igor-goldobin
- title: Stanley Sidik
  url: https://ssw.com.au/people/stanley-sidik
related: []
redirects:
- do-you-enable-automatic-windows-update-installations

---


<p class="p1">​Microsoft Update is a service that allows for the periodic patching of system files to address known issues with Microsoft products. Originally called Windows Update, it was specifically focused on Operating System patches for Windows but has been expanded to include all Microsoft products and the name has changed to Microsoft Update, allowing the automated patching of non-OS software such as Internet Explorer and Microsoft Office. <br><br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>​<span style="line-height:1.6;">It is important to keep your machine up-to-date, but Windows Update Automatic installation can be somewhat intrusive to your workflow. There is nothing worse than getting Windows Updates installing during an important presentation. You should set Windows Updates to be installed manually.</span></p><p>
   <span style="line-height:1.6;"><b>​Note: </b>This is only for client machines, Windows Update for Servers should be handled differently see: <a href=/do-you-use-group-policy-to-manage-your-windows-update-policy>Do you use Group Policy to manage your Windows Update Policy?<b></b></a><br><strong></strong><br></span></p><p class="p1">Go to 
   <strong>Start</strong><strong> | Windows Update Settings | Advanced Options </strong>and set <strong>Restart this device as soon as possible... </strong>to <strong>Off </strong>and <strong>Update Notifications </strong>to <strong>​On.</strong><br></p><dl class="badImage"><dt>
      <br>
      <img src="WindowsUpdateBadExample.jpg" alt="WindowsUpdateBadExample.jpg" style="margin:5px;width:623px;height:510px;" />
      <br>
   </dt><dd>Figure: Bad example – Install updates automatically​<br></dd></dl><dl class="goodImage"><dt>​<img src="Windows Update Good Example.jpg" alt="Windows Update Good Example.jpg" style="margin:5px;width:623px;height:510px;" /><br></dt><dd>Figure: Good example – Download updates but let user choose whether to install them</dd></dl><p class="p1">If you have a system administrator who manages your organization’s infrastructure, it is recommended to get you system administrator to push this setting via group policy.​​<br></p><dl class="goodImage"><dt>
      <img src="win-update-3.jpg" alt="" />
      <br>
   </dt><dd>Figure: Better example – Windows Updates setting is pushed to *ALL* users via group policy​<br></dd></dl><h3> ​​Related Rules<br></h3><ul><li></li><li>
      <a href=/do-you-turn-off-auto-update-on-your-servers>Do you turn off auto-update on your servers?</a> [for Servers]</li><li>
      <a href=/do-you-use-group-policy-to-manage-your-windows-update-policy>Do you use Group Policy to manage your Windows Update Policy?​</a> [for both Servers and PCs​]<br></li></ul>


