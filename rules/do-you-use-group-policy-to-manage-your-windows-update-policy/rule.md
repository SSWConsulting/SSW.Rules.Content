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
<dl class="badImage"><dt> <img alt=" Accidently press Restart Now on a Production server and your users won't be happy!" src="/PublishingImages/updates-restart.jpg" /> </dt><dd>Bad example – it is automatically installing and you want control over your patching. Accidentally press Restart Now on a Production server and your users won't be happy!</dd></dl><p><b>Note &#58; </b>Server patching is also achievable via SCCM and you get more control over restarting windows like this. WSUS can also be used in conjunction with group policies to handle restart times better.</p><p>The best ensure you are still downloading updates but not installing them automatically is to use Group Policy.</p><ol><li>Create an Organization Unit (OU) in Active Directory, and put all your Production Servers in the OU<br>
      <dl class="image"><dt> <img alt="Add all your Production Servers to the Production Server OU" src="/PublishingImages/updates-adou.jpg" /> </dt><dd>Add all your Production Servers to the Production Server OU</dd></dl></li><li>Create a new Group Policy object and link it to the Production Server OU<br>
      <dl class="image"><dt> <img alt="Create a new Group Policy for your Production Servers" src="/PublishingImages/updates-gpo.jpg" /> </dt><dd>Create a new Group Policy for your Production Servers</dd></dl></li><li>Edit the new Group Policy object and drill down to <strong>Computer Configuration</strong> | <strong>Policies </strong>| <strong>Windows Components</strong> | <strong>Windows Update</strong> </li><li>Edit the <strong>Configure Automatic Update Properties</strong> item and <strong>enable </strong>it</li><li>Set the <strong>Configure Automatic Updating</strong> option to <strong>3 – Auto download and notify for install<br>
         <dl class="image"><dt> <img alt="Edit Configure Automatic Updates Properties and enable Auto download and notify for install" src="/PublishingImages/updates-editgp.jpg" /> </dt><dd>Edit Configure Automatic Updates Properties and enable 'Auto download and notify for install</dd></dl> </strong></li></ol><p>After the new Group Policy propagates, you will notice the update setting is now locked on the servers in the Production Server OU.</p><dl class="goodImage"><dt> <img alt="The Group Policy locks the Windows Update setting" src="/PublishingImages/updates-updatesforced.jpg" /> </dt><dd>The Group Policy locks the Windows Update setting</dd></dl><p>Now the next time you plan to reboot your server you can install updates quickly and reboot – keeping your servers updated without unplanned reboots.</p><p>The following screenshot is the settings applied to the default domain policy for the same group policy settings but this will apply to all machines joined to the SSW domain. <br></p><dl class="image"><dt> <img alt="Default domain policy1.png" src="/Documents/Default%20domain%20policy1.png" /> </dt></dl>


