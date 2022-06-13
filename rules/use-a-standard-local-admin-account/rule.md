---
type: rule
archivedreason:
title: Do you use a standard local admin account?
guid: 05f52cf3-4a92-447f-bfad-75d0903a3814
uri: use-a-standard-local-admin-account
created: 2021-03-15T09:45:07.0000000Z
authors:
- title: Kaique Biancatti (Kiki)
  url: https://ssw.com.au/people/kaique-biancatti
related:

---

Having a local admin account that is not the built-in admin account Windows creates at first is an important way to get access back to your system if any troubles arise.

<!--endintro-->

When first setting up, Windows creates a local administrator account that can change everything in the system – this account cannot be deleted, just disabled. It is good practice to disable this account and create a new one, following your own company password and naming standard, that is also a local administrator on the PC.
 
It is also good practice to use a script (or Group Policy) to set that admin account, fewer errors than doing it manually.

::: greybox
Have a look at SSW SysAdmins' script for that: https://github.com/SSWConsulting/SSWSysAdmins.LocalAdminAccount
:::

Having a local admin has many **benefits**, including:
1. “Backdoor” or offline access if no domain controller is available to serve login requests e.g. no internet, remote locations
2. Consistent admin user across all devices e.g. no need to guess which password or user was created for that machine
 
But it also has **cons**:
1. If an attacker gets the username and password for that admin account, it can control any machine – Important to have a different admin account for different types of services e.g. servers, BYO devices, laptops, desktops 
2. If a password is compromised, changing the password of all devices might be cumbersome
