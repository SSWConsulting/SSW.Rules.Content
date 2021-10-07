---
type: rule
archivedreason:
title: Do you control who can create and manage Power Platform environments using the admin centre?
guid: fdf48f2a-2292-4fab-9ffc-c3b439e4b1c0
uri: control-who-can-manage-power-platform-environments
created: 2021-06-01T17:30:01.0000000Z
authors:
- title: Mehmet Ozdemir
  url: https://ssw.com.au/people/mehmet
related:

---

Out of the box, any user with the correct licence can create environments. If you are managing Power Platform and would like to restrict environment creation and management only to admin then change the global settings:

<!--endintro-->

1.	Sign-in to the Microsoft Power Platform admin centre at https://admin.powerplatform.microsoft.com.
2.	Select the Gear icon (⚙️) in the upper-right corner of the Microsoft Power Platform site.
3.	Select Power Platform settings.
4.	Select Only specific admins.

![Figure: Set environment creation to admins only](power-platform-settings.png)

Once the settings are changed only Global Admin, Dynamics 365 Admins, Power Platform Admins will control the environments.
