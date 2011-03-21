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


We all know it’s important to keep our servers updated. Unfortunately though, by default, Windows will automatically download and install all new Windows Updates on your servers. This will mean the servers will occasionally restart to install updates when you don’t want them too. You will also get annoying popups trying to get you to restart the computer. 

<br><excerpt class='endintro'></excerpt><br>

  <img alt=" Accidently press Restart Now on a Production server and your users won't be happy!" src="/ITAndNetworking/RulesToBetterWindowsServers/PublishingImages/updates-restart.jpg" /> <br>
<font class="ms-rteCustom-FigureBad" size="+0">Figure 1 - Accidently press Restart Now on a Production server and your users won't be happy!</font><br>
The best ensure you are still downloading updates but not installing them automatically is to use Group Policy.&#160;<br>
<br>
<ol>
    <li>Create an Organization Unit (OU) in Active Directory, and put all your Production Servers in the OU<br><img alt="Add all your Production Servers to the Production Server OU" src="/ITAndNetworking/RulesToBetterWindowsServers/PublishingImages/updates-adou.jpg" /><br>
    <font class="ms-rteCustom-FigureNormal" size="+0">Figure 2 - Add all your Production Servers to the Production Server OU</font> </li>
    <li>Create a new Group Policy object and link it to the Production Server OU<br>
    <img alt="Create a new Group Policy for your Production Servers" src="/ITAndNetworking/RulesToBetterWindowsServers/PublishingImages/updates-gpo.jpg" /><br>
    <font class="ms-rteCustom-FigureNormal" size="+0">Figure 3 - Create a new Group Policy for your Production Servers</font> </li>
    <li>Edit the new Group Policy object and drill down to <strong>Computer Configuration</strong> | <strong>Policies </strong>| <strong>Windows Components</strong> | <strong>Windows Update</strong> </li>
    <li>Edit the <strong>Configure Automatic Update Properties</strong> item and <strong>enable </strong>it </li>
    <li>Set the <strong>Configure Automatic Updating</strong> option to <strong>3 – Auto download and notify for install<br>
    <img alt="Edit Configure Automatic Updates Properties and enable 'Auto download and notify for install'" src="/ITAndNetworking/RulesToBetterWindowsServers/PublishingImages/updates-editgp.jpg" /><br>
    </strong><font class="ms-rteCustom-FigureNormal" size="+0">Figure 4 - Edit Configure Automatic Updates Properties and enable 'Auto download and notify for install</font> </li>
</ol>
After the new Group Policy propagates, you will notice the update setting is now locked on the servers in the Production Server OU.&#160;<br>
<br>
<img alt="The Group Policy locks the Windows Update setting" src="/ITAndNetworking/RulesToBetterWindowsServers/PublishingImages/updates-updatesforced.jpg" /><br>
<font class="ms-rteCustom-FigureGood" size="+0">Figure 5 - The Group Policy locks the Windows Update setting<br>
</font><br>
Now the next time you plan to reboot your server you can install updates quickly and reboot – keeping your servers updated without unplanned reboots. 



