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


It is important install your printers automatically to all clients that logon to the domain.<br>
<br><excerpt class='endintro'></excerpt><br>
<p>This can be achieved via Group Policy. This can be set up easily in​ a Microsoft Windows 2008 Server R2:<br></p><p class="ssw15-rteElement-GreyBox"><b>Note: </b>It is better to deploy printers via GPO preferences to end users and also for large-scale environments. There are third-party products eg. Tricerat or Printer Logic which makes centralizing printer queues and servers more efficiently.<br></p>
<ul>
<li>From Server Manager add the Print Services role</li>
<img class="ms-rteCustom-ImageArea" alt="Install the Print Services role" src="install-print-roles.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure: Install the Print Services role</span>
<li>When the role has installed, open Print Management from Administrative Tools</li>
<li>Install all your printers by right clicking on Printers and clicking Add Printer</li>
<img class="ms-rteCustom-ImageArea" alt="Add all of your printers to the server" src="add-printers.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure: Add all of your printers to the server</span>
<li>Right click on Drivers and choose Add Drivers. From here you will be able to install the x86 and x64 drivers for your printers so all workstations in your organization get the printer drives automatically</li>
<img class="ms-rteCustom-ImageArea" alt="Add the additional drivers for both x86 and x64" src="add-drivers.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure: Add the additional drivers for both x86 and x64</span>
<li>Click on Printers in the menu to get a list of your installed printers</li>
<li>Right click on the first printer you want to install via group policy and click on Deploy with Group Policy</li>
<img class="ms-rteCustom-ImageArea" alt="Deploying your printer with Group Policy" src="deploy-printer.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure: Deploying your printer with Group Policy</span>
<li>Next, you need to choose a Group Policy Object (GPO) to add the printers too. You may wish to create a new GPO specifically for the printers, which you can do through the Group Policy Management tool in Administrative Tools</li>
<img class="ms-rteCustom-ImageArea" alt="Select the Group Policy Object (GPO) to add the printers to" src="select-gpo.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure: Select the Group Policy Object (GPO) to add the printers to</span>
<li>Repeat the last 2 steps for each printer you want to add automatically using Group Policy</li>
<li>Reboot your workstations and the new printers will be added upon login</li>
</ul>



