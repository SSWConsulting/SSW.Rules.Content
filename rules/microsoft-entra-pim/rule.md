---
seoDescription: Microsoft Entra Privileged Identity Management (PIM) secures and simplifies privileged access management for your organization.
type: rule
title: Security - Do you use Microsoft Entra Privileged Identity Management?
uri: microsoft-entra-pim
redirects:
  - azure-ad-pim
authors:
  - title: Kiki Biancatti
    url: https://ssw.com.au/people/kaique-biancatti
    img: https://raw.githubusercontent.com/SSWConsulting/SSW.People.Profiles/main/Kaique-Biancatti/Images/Kaique-Biancatti-Profile.jpg
created: 2022-07-14T05:19:20.642Z
guid: c302c328-10b4-410c-ba99-0d9ebb19a95f
---

Microsoft Entra Privileged Identity Management (PIM) - formerly Azure Active Directory PIM enables a more secure, manageable and monitorable approach to assigning privileged permissions in your organization.

<!--endintro-->

PIM enables just-in-time privileged access for users that are eligible for it, reducing the chance of privileged actions being done by malicious (or unaware) actors.

Things that we can do with PIM (taken from [What is Microsoft Entra Privileged Identity Management?](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure)):

* Provide **just-in-time** privileged access to Entra ID and Azure resources
* Assign **time-bound** access to resources using start and end dates
* Require **approval** to activate privileged roles
* Enforce **multi-factor authentication** to activate any role
* Use **justification** to understand why users activate
* Get **notifications** when privileged roles are activated
* Conduct **access reviews** to ensure users still need roles
* Download **audit history** for internal or external audit
* Prevents removal of the **last active Global Administrator** and **Privileged Role Administrator** role assignments

### Adding assignments in PIM

As best practice, your company should use PIM to give access to new SysAdmins.

Do the following:

1. Go to PIM at <https://portal.azure.com/#view/Microsoft_Azure_PIMCommon/ResourceMenuBlade/~/MyActions/resourceId//resourceType/tenant/provider/aadroles>
2. Go to Assignments | Add Assignment:
   ::: good
   ![Figure: Good example - Assigning roles in PIM](pim1.jpg)
   :::

3. Select Role | Select members | Next
4. Here, you have 2 options:

   1. Eligible: The member is **eligible** for activating the permissions, permanently or for a set period of time. Every time they activate, they will have the permissions for up to 8 hours, then they will lose it and will need to activate again. Activating is a manual process of going to PIM and clicking "Activate"
   2. Active: The member has the permissions **active**, forever or for a set period of time. They don't need to perform any manual steps to activate anything

5. Select the correct one | Add a justification | Assign:

   ::: good
   ![Figure: Good example - Having the option of Eligible and Active makes PIM flexible](pim2.jpg)
   :::

   You are now assigned roles in PIM.

### Activating assignments in PIM

If you are eligible for assignments, you can activate them by doing the following:

1. Go to [https://portal.azure.com/#view/Microsoft_Azure_PIMCommon/ResourceMenuBlade/~/MyActions/resourceId//resourceType/tenant/provider/aadroles](https://portal.azure.com/#view/Microsoft_Azure_PIMCommon/ResourceMenuBlade/~/MyActions/resourceId//resourceType/tenant/provider/aadroles)

2. Click on My Roles | Role | Activate:
   ::: good
   ![Figure: Good example - Activate just-in-time roles only when you need it](how-to-activate-pim.png)
   :::

3. Go through the steps to add a justification and time you need that access for.

You now have that role active for you, for up to 8 hours.

### Receiving PIM alerts on your email

PIM has built-in alerts that will send an email when assignments are activated, together with its justification, who activated it, the role activated, and extra information:

::: good
![Figure: Good example - PIM emails you when assignments and roles are activated, you can see straight away if something's wrong!](pimalert.jpg)
:::
