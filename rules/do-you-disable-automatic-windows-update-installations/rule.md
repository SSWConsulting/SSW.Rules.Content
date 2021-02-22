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

Microsoft Update is a service that allows for the periodic patching of system files to address known issues with Microsoft products. Originally called Windows Update, it was specifically focused on Operating System patches for Windows but has been expanded to include all Microsoft products and the name has changed to Microsoft Update, allowing the automated patching of non-OS software such as Internet Explorer and Microsoft Office.

<!--endintro-->

It is important to keep your machine up-to-date, but Windows Update Automatic installation can be somewhat intrusive to your workflow. There is nothing worse than getting Windows Updates installing during an important presentation. You should set Windows Updates to be installed manually.

**Note:** This is only for client machines, Windows Update for Servers should be handled differently see: [Do you use Group Policy to manage your Windows Update Policy?](/do-you-use-group-policy-to-manage-your-windows-update-policy)

Go to      **Start** **| Windows Update Settings | Advanced Options** and set  **Restart this device as soon as possible...** to  **Off** and  **Update Notifications** to  **On.**


::: bad  
![Figure: Bad example – Install updates automatically](WindowsUpdateBadExample.jpg)  
:::


::: good  
![Figure: Good example – Download updates but let user choose whether to install them](Windows Update Good Example.jpg)  
:::

If you have a system administrator who manages your organization’s infrastructure, it is recommended to get you system administrator to push this setting via group policy.


::: good  
![Figure: Better example – Windows Updates setting is pushed to \*ALL\* users via group policy](win-update-3.jpg)  
:::

###  Related Rules


* 
* [Do you turn off auto-update on your servers?](/do-you-turn-off-auto-update-on-your-servers) [for Servers]
* [Do you use Group Policy to manage your Windows Update Policy?](/do-you-use-group-policy-to-manage-your-windows-update-policy) [for both Servers and PCs]
