---
type: rule
title: Do you use Group Policy to manage your Windows Update Policy?
uri: do-you-use-group-policy-to-manage-your-windows-update-policy
authors:
  - title: Matthew Hodgkins
    url: https://ssw.com.au/people/matthew-hodgkins
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related:
  - do-you-disable-automatic-windows-update-installations
  - do-you-turn-off-auto-update-on-your-servers
redirects: []
created: 2011-03-21T00:27:18.000Z
archivedreason: null
guid: 19452101-3232-446e-9932-2e8486b410d4
---
We all know it’s important to keep our servers updated. Unfortunately though, by default, Windows will automatically download and install all new Windows Updates on your servers. This will mean the servers will occasionally restart to install updates when you don’t want them too. You will also get annoying popups trying to get you to restart the computer. 

<!--endintro-->

**Note:** This rule is applied to both client PCs and servers.

It is also one more reason developers don’t like to join a company domain on their personal laptops!

::: bad
![Figure: Bad example - Windows 10 shows a ‘Restart now’ – do not accidentally press it! Your production server and your users won't be happy!](Windows-Update-notification.png)
:::

::: bad
![Figure: Bad example – Remember this nasty one from Vista days?](updates-restart.jpg)
:::

**Note:** Server patching is also achievable via SCCM and you get more control over restarting windows like this. WSUS can also be used in conjunction with group policies to handle restart times better.

The best ensure you are still downloading updates but not installing them automatically is to use Group Policy.

1. Create an Organization Unit (OU) in Active Directory, and put all your Production Servers in the OU

![Add all your Production Servers to the Production Server OU](updates-adou.jpg)

2. Create a new Group Policy object and link it to the Production Server OU

![Create a new Group Policy for your Production Servers](updates-gpo.jpg)

3. Edit the new Group Policy object and drill down to  
   **Computer Configuration** | **Policies** | **Windows Components** | **Windows Update** 

4. Edit  
   **Configure Automatic Update Properties** item and **enable** it

5. Set **Configure Automatic Updating** option to **3 – Auto download and notify for install**

![Edit Configure Automatic Updates Properties and enable 'Auto download and notify for install](updates-editgp.jpg)

After the new Group Policy propagates, you will notice the update setting is now locked on the servers in the Production Server OU.

::: good
![Figure: Good example - The Group Policy locks the Windows Update setting](updates-updatesforced.jpg)
:::

From now on your servers will be updated without unplanned reboots!

::: good
![Figure: Good example - AD shows the Group Policy setting “3 – Auto download and notify for install”. This policy is applied to the specified OU eg. Production Servers joined to this domain](Default domain policy1.png)
:::

Check out "auto-update" rules for [PCs](/do-you-disable-automatic-windows-update-installations) and [Servers](/do-you-turn-off-auto-update-on-your-servers).
