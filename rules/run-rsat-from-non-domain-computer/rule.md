---
seoDescription: Learn how to securely run Remote Server Administration Tools (RSAT) from a non-domain joined computer and manage your Active Directory environment with ease.
type: rule
title: Do you know how to run RSAT from a non-domain computer?
uri: run-rsat-from-non-domain-computer
redirects:
  - run-aduc-from-non-domain-computer
authors:
  - title: Chris Schultz
    url: https://www.ssw.com.au/people/chris-schultz/
related:
  - windows-admin-center
created: 2024-01-31T05:50:52.028Z
guid: 46bf37e1-2f9d-4f08-9281-8e58e4ca9157
---

With more companies adopting BYOD policies, it is important for SysAdmins to be able to connect to Remote Server Administrative Tools (RSAT) like Active Directory Users and Computers (ADUC) in a secure way, even if their computer is not connected to the domain.

<!--endintro-->

:::info
**Note:** You should make sure any personal devices connecting to your network are secure, with [Intune](/implementing-intune) or a similar solution.
:::

## RDP to the domain controller (don't do this!)

The least secure way is to use Remote Desktop Connection to make changes directly on the domain controller. Domain controllers should be locked down to only accept log ins from domain admin accounts - and should only be used when changes require these credentials.

:::bad
![Figure: Bad example - RDP directly to the domain controller](rdp-dc.png)
:::

Another option is to connect to a different computer or server that is on the domain, like a jump box. This is a more secure solution, but for many companies it adds infrastructure that is not necessary.

## Windows Admin Center

Microsoft have a browser-based server management tool called **Windows Admin Center**. It is very useful for managing servers, and it can also be used to manage your AD environment - as well as DHCP, DNS and other Windows Server services.

Since the tool is browser-based, you only need to allow access to one port for HTTPS communication.

::: good
![Figure: Managing AD in Windows Admin Center](admin-center-aduc.png)
:::

Read more about Windows Admin Center here: [Do you use Windows Admin Center?](/windows-admin-center)

## Running RSAT from a non-domain joined computer

While Windows Admin Center is a great solution, many SysAdmins prefer the extra functionality and classic interface of RSAT (Remote Server Administration Tools) in MMC (Microsoft Management Console) that you can easily run from a domain joined computer.

:::info
You can also use this if you have a domain-joined computer, but you need to use a different account to the one you log in with to access RSAT.
:::

To get RSAT connected on a non-domain joined computer, there are some extra steps:

1. Make sure you have the RSAT features you need: [Install RSAT Features](https://www.pdq.com/blog/how-to-install-remote-server-administration-tools-rsat/)
2. Run Command Prompt as Administrator
3. Run this command to open an empty MMC window (replace **admin@domain**):

   `runas.exe /netonly /noprofile /user:"admin@domain" mmc.exe`

4. Go to **File | Add/Remove Snap-in...** to add the tools you need, e.g. ADUC, DHCP, DNS, GPO Management
   ![Figure: MMC | Add or Remove Snap-ins](mmc-add-snapin.png)
5. For ADUC (and possibly other tools), you will need to specify the domain to connect to. Make sure you tick the box **Save this domain setting for the current console**.

   ![Figure: ADUC | Change domain](aduc-domain.png)

6. Go to **File | Save As...** and save the console somewhere appropriate, e.g. C:\work\rsat.msc
7. Create a batch file with this command - similar to the command above, but we specify the .msc file to use:

   `runas.exe /netonly /noprofile /user:"admin@domain" "mmc.exe "C:\work\rsat.msc""`

8. Save the batch file and run it as administrator.
9. Your MMC window will open with your snap-ins ready to go!
