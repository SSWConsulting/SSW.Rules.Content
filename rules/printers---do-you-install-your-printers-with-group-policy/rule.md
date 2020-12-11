---
type: rule
archivedreason: 
title: Printers - Do You Install Your Printers With Group Policy?
guid: 57d9fad8-e0c7-4ed2-ad3b-d362299d118e
uri: printers---do-you-install-your-printers-with-group-policy
created: 2012-03-05T15:03:34.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

It is important install your printers automatically to all clients that logon to the domain.

<!--endintro-->

This can be achieved via Group Policy. This can be set up easily in a Microsoft Windows 2008 Server R2:


::: greybox
 **Note:** It is better to deploy printers via GPO preferences to end users and also for large-scale environments. There are third-party products eg. Tricerat or Printer Logic which makes centralizing printer queues and servers more efficiently.

:::


* From Server Manager add the Print Services role

![Install the Print Services role* When the role has installed, open Print Management from Administrative Tools](install-print-roles.jpg)
* Install all your printers by right clicking on Printers and clicking Add Printer

![Add all of your printers to the server* Right click on Drivers and choose Add Drivers. From here you will be able to install the x86 and x64 drivers for your printers so all workstations in your organization get the printer drives automatically](add-printers.jpg)

![Add the additional drivers for both x86 and x64* Click on Printers in the menu to get a list of your installed printers](add-drivers.jpg)
* Right click on the first printer you want to install via group policy and click on Deploy with Group Policy

![Deploying your printer with Group Policy* Next, you need to choose a Group Policy Object](deploy-printer.jpg)(GPO) to add the printers too. You may wish to create a new GPO specifically for the printers, which you can do through the Group Policy Management tool in Administrative Tools

![Select the Group Policy Object (GPO) to add the printers to](select-gpo.jpg)**Figure: Select the Group Policy Object (GPO) to add the printers to*** Repeat the last 2 steps for each printer you want to add automatically using Group Policy
* Reboot your workstations and the new printers will be added upon login
