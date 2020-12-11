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
<div>
   <b>Note:</b> This rule applied to both client PCs and servers.</div><div>
   <br>
</div><div>It is also one more reason developers don’t like to join a company domain on their personal laptops!<br><br></div><dl class="badImage"><dt> 
      <img alt="Windows-Update-notification.png" src="Windows-Update-notification.png" style="width:750px;" /> 
   </dt><dd>Bad Example - Windows 10 shows a ‘Restart now’ – do not accidentally press it! Your production server and your users won't be happy!</dd></dl><dl class="badImage"><dt>​<img src="updates-restart.jpg" alt="Accidently press Restart Now on a Production server and your users won't be happy!" /> </dt><dd>Bad example – Remember this nasty one from Vista days?</dd></dl><p>
   <b>Note: </b>Server patching is also achievable via SCCM and you get more control over restarting windows like this. WSUS can also be used in conjunction with group policies to handle restart times better.</p><p>The best ensure you are still downloading updates but not installing them automatically is to use Group Policy.</p><ol><li>Create an Organization Unit (OU) in Active Directory, and put all your Production Servers in the OU<br> 
      <dl class="image"><dt> 
            <img src="updates-adou.jpg" alt="Add all your Production Servers to the Production Server OU" /> 
         </dt><dd>Add all your Production Servers to the Production Server OU</dd></dl></li><li>Create a new Group Policy object and link it to the Production Server OU<br> 
      <dl class="image"><dt> 
            <img src="updates-gpo.jpg" alt="Create a new Group Policy for your Production Servers" /> 
         </dt><dd>Create a new Group Policy for your Production Servers</dd></dl></li><li>Edit the new Group Policy object and drill down to 
      <strong>Computer Configuration</strong> | 
      <strong>Policies </strong>| 
      <strong>Windows Components</strong> | 
      <strong>Windows Update</strong> </li><li>Edit the 
      <strong>Configure Automatic Update Properties</strong> item and 
      <strong>enable </strong>it</li><li>Set the 
      <strong>Configure Automatic Updating</strong> option to 
      <strong>3 – Auto download and notify for install<br> 
         <dl class="image"><dt> 
               <img src="updates-editgp.jpg" alt="Edit Configure Automatic Updates Properties and enable Auto download and notify for install" /> 
            </dt><dd>Edit Configure Automatic Updates Properties and enable 'Auto download and notify for install</dd></dl> </strong></li></ol><p>After the new Group Policy propagates, you will notice the update setting is now locked on the servers in the Production Server OU.</p><dl class="goodImage"><dt> 
      <img src="updates-updatesforced.jpg" alt="The Group Policy locks the Windows Update setting" /> 
   </dt><dd>The Group Policy locks the Windows Update setting</dd></dl><p></p><p>From now on your servers will be updated without unplanned reboots!<br></p><dl class="image"><dt> 
      <img src="Default domain policy1.png" alt="Default domain policy1.png" />
   </dt><dd class="ssw15-rteElement-FigureGood">     Figure: Good example - AD shows the Group Policy setting “3 – Auto download and notify for install”. This policy is applied to the specified OU eg. Production Servers joined to this domain 
      <br></dd></dl><p></p>
<h3> ​​Related Rules<br></h3><ul><li>
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=f5432cb4-40af-491b-8da5-33b8a80dcb0a">​Do you enable automatic Windows Update Installations?​</a> [for PCs] </li><li>
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=3b0722be-c3e3-4369-a590-258c7501a67a">Do you turn off auto-update on your servers?</a> [for Servers]​<br></li></ul>


