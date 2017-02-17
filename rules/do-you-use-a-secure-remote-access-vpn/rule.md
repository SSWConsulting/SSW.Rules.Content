---
type: rule
title: Do you use a secure Remote-Access VPN?
uri: do-you-use-a-secure-remote-access-vpn
created: 2017-02-17T03:48:32.0000000Z
authors:
- id: 47
  title: Stanley Sidik

---



<span class='intro'> On the computer that you want to setup the VPN&#58;  </span>

<ol><li>Click on the Network icon which can be found at the bottom right hand corner of your screen and click on Network Settings<img class="ms-rteCustom-ImageArea" alt="Win10Network.jpg" src="/SiteAssets/do-you-know-how-to-setup-a-pptp-vpn-in-windows-10/Win10Network.jpg" style="margin&#58;5px;" />&#160;</li><li>Navigate to VPN and click on Add A VPN Connection<br><img class="ms-rteCustom-ImageArea" alt="windows10vpn.png" src="/SiteAssets/do-you-know-how-to-setup-a-pptp-vpn-in-windows-10/windows10vpn.png" style="margin&#58;5px;" />&#160;&#160; </li><li>&#160;Enter the VPN details (VPN Name and VPN Server/IP Address)<br><img class="ms-rteCustom-ImageArea" alt="windows10pptpsetup.png" src="/SiteAssets/do-you-know-how-to-setup-a-pptp-vpn-in-windows-10/windows10pptpsetup.png" style="margin&#58;5px;" /></li><li>Enter your&#160;VPN account details in the selection box (remember to click on &quot;Remember my sign-in info&quot;)<br><img class="ms-rteCustom-ImageArea" alt="windows10vpndetails.png" src="/SiteAssets/do-you-know-how-to-setup-a-pptp-vpn-in-windows-10/windows10vpndetails.png" style="margin&#58;5px;" /></li><li>Your VPN is almost&#160;ready to use, however you want to disable&#160;&quot;use default gateway on remote network&quot;. Unfortunately GUI has been removed from&#160;Windows 10, however this is easily done through PowerShell. Open up a PowerShell and run<br><strong>Get-vpnConnection</strong><br><strong><img alt="Windows10VPNPowerShell.png" src="/SiteAssets/do-you-know-how-to-setup-a-pptp-vpn-in-windows-10/Windows10VPNPowerShell.png" style="margin&#58;5px;" /></strong></li><li>Enable Split Tunneling on the VPN connection&#160;created&#160;with PowerShell command (replace [vpnname]&#160;below&#160;with SSW)<br><strong>Set-vpnConnection -Name &quot;[vpnname]&quot; -SplitTunneling $True </strong></li><li>You are now ready to use the VPN connection. Select the VPN connection that you have just created and click on connect<br><img class="ms-rteCustom-ImageArea" alt="windows10connectvpn.png" src="/SiteAssets/do-you-know-how-to-setup-a-pptp-vpn-in-windows-10/windows10connectvpn.png" style="margin&#58;5px;" /></li><li>The VPN will now attempt to connect&#160;and if successful, the VPN status will change to Connected<br><img class="ms-rteCustom-ImageArea" alt="windows10vpnconnected.png" src="/SiteAssets/do-you-know-how-to-setup-a-pptp-vpn-in-windows-10/windows10vpnconnected.png" style="margin&#58;5px;" /></li></ol><p>&#160;</p>


