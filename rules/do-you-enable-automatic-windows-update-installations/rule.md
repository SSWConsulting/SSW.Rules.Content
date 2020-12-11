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

Microsoft Update is a service that allows for the periodic patching of system files to address known issues with Microsoft products. Originally called Windows Update, it was specifically focused on Operating System patches for Windows but has been expanded to include all Microsoft products and the name has changed to Microsoft Update, allowing the automated patching of non-OS software such as Internet Explorer and Microsoft Office.

<!--endintro-->

It is important to keep your machine up-to-date, but Windows Update Automatic installation can be somewhat intrusive to your workflow. There is nothing worse than getting Windows Updates installing during an important presentation. You should set Windows Updates to be installed manually.

**Note:** This is only for client machines, Windows Update for Servers should be handled differently see: [Do you use Group Policy to manage your Windows Update Policy?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=eb2f95c5-22c8-4568-9173-9e52e3087faf)

Go to      **Start** **| Windows Update Settings | Advanced Options** and set  **Restart this device as soon as possible...** to  **Off** and  **Update Notifications** to  **On.**
<dl class="badImage">&lt;dt&gt;
      <br>
      <img src="WindowsUpdateBadExample.jpg" alt="WindowsUpdateBadExample.jpg" style="margin:5px;width:623px;height:510px;">
      <br>
   &lt;/dt&gt;<dd>Figure: Bad example – Install updates automatically<br></dd></dl><dl class="goodImage">&lt;dt&gt;<img src="Windows Update Good Example.jpg" alt="Windows Update Good Example.jpg" style="margin:5px;width:623px;height:510px;"><br>&lt;/dt&gt;<dd>Figure: Good example – Download updates but let user choose whether to install them</dd></dl>
If you have a system administrator who manages your organization’s infrastructure, it is recommended to get you system administrator to push this setting via group policy.
<dl class="goodImage">&lt;dt&gt;
      <img src="win-update-3.jpg" alt="">
      <br>
   &lt;/dt&gt;<dd>Figure: Better example – Windows Updates setting is pushed to *ALL* users via group policy<br></dd></dl>
###  Related Rules


* 
* [Do you turn off auto-update on your servers?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=3b0722be-c3e3-4369-a590-258c7501a67a) [for Servers]
* [Do you use Group Policy to manage your Windows Update Policy?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=eb2f95c5-22c8-4568-9173-9e52e3087faf) [for both Servers and PCs]
