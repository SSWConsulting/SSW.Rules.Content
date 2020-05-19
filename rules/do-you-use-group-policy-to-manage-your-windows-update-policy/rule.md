---
type: rule
archivedreason: 
title: Do you use Group Policy to manage your Windows Update Policy?
guid: 19452101-3232-446e-9932-2e8486b410d4
uri: do-you-use-group-policy-to-manage-your-windows-update-policy
created: 2011-03-21T00:27:18.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins
- id: 1
  title: Adam Cogan
related: []

---


We all know it’s important to keep our servers updated. Unfortunately though, by default, Windows will automatically download and install all new Windows Updates on your servers. This will mean the servers will occasionally restart to install updates when you don’t want them too. You will also get annoying popups trying to get you to restart the computer. <br>
<br><excerpt class='endintro'></excerpt><br>
<div>Note&#58; This rule applied to both client PCs and servers.<br>It is also one more reason developers don’t like to join a company domain on their personal laptops!<br><br></div><div><img alt="Windows-Update-notification.png" src="/SiteAssets/do-you-use-group-policy-to-manage-your-windows-update-policy/Windows-Update-notification.png" style="margin&#58;5px;width&#58;808px;" /><dd class="ssw15-rteElement-FigureBad">Bad Example - Windows 10 shows a ‘Restart now’ – do not accidentally press it! Your production server and your users won't be happy!<br></dd></div><dl class="badImage"><dt>&#160;<img src="/PublishingImages/updates-restart.jpg" alt="Accidently press Restart Now on a Production server and your users won't be happy!" /> </dt><dd>Bad example – Remember this nasty one from Vista days?</dd></dl><p><b>Note&#58; </b>Server patching is also achievable via SCCM and you get more control over restarting windows like this. WSUS can also be used in conjunction with group policies to handle restart times better.</p><p>The best ensure you are still downloading updates but not installing them automatically is to use Group Policy.</p><ol><li>Create an Organization Unit (OU) in Active Directory, and put all your Production Servers in the OU<br>
      <dl class="image"><dt> <img src="/PublishingImages/updates-adou.jpg" alt="Add all your Production Servers to the Production Server OU" /> </dt><dd>Add all your Production Servers to the Production Server OU</dd></dl></li><li>Create a new Group Policy object and link it to the Production Server OU<br>
      <dl class="image"><dt> <img src="/PublishingImages/updates-gpo.jpg" alt="Create a new Group Policy for your Production Servers" /> </dt><dd>Create a new Group Policy for your Production Servers</dd></dl></li><li>Edit the new Group Policy object and drill down to <strong>Computer Configuration</strong> | <strong>Policies </strong>| <strong>Windows Components</strong> | <strong>Windows Update</strong> </li><li>Edit the <strong>Configure Automatic Update Properties</strong> item and <strong>enable </strong>it</li><li>Set the <strong>Configure Automatic Updating</strong> option to <strong>3 – Auto download and notify for install<br>
         <dl class="image"><dt> <img src="/PublishingImages/updates-editgp.jpg" alt="Edit Configure Automatic Updates Properties and enable Auto download and notify for install" /> </dt><dd>Edit Configure Automatic Updates Properties and enable 'Auto download and notify for install</dd></dl> </strong></li></ol><p>After the new Group Policy propagates, you will notice the update setting is now locked on the servers in the Production Server OU.</p><dl class="goodImage"><dt> <img src="/PublishingImages/updates-updatesforced.jpg" alt="The Group Policy locks the Windows Update setting" /> </dt><dd>The Group Policy locks the Windows Update setting</dd></dl><p></p><p>From now on your servers will be updated without unplanned reboots!<br></p><dl class="image"><dt> <img src="/Documents/Default%20domain%20policy1.png" alt="Default domain policy1.png" /></dt><dd class="ssw15-rteElement-FigureGood">&#160;&#160;&#160;&#160; Figure&#58; Good example - AD shows the Group Policy setting “3 – Auto download and notify for install”. This policy is applied to the specified OU eg. Production Servers joined to this domain <br></dd></dl>


