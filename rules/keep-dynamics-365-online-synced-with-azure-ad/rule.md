---
type: rule
archivedreason: 
title: Do you keep your Dynamics 365 Online synced with Azure AD?
guid: acd3409e-f1df-4c8c-8326-0549dc7ba205
uri: keep-dynamics-365-online-synced-with-azure-ad
created: 2020-09-16T18:50:43.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Kaique Biancatti
  url: https://ssw.com.au/people/kaique-biancatti
related: []
redirects:
- do-you-keep-your-dynamics-365-online-synced-with-azure-ad

---

If you are using Microsoft Dynamics 365 Online as your CRM solution, you might have noticed that it syncs some Azure Active Directory (Azure AD) fields automatically.

<!--endintro-->

Dynamics 365 Online leverages Azure AD fields to import information to users, e.g.:

1. First Name;
2. Last Name;
3. Job Title;
4. Address

And, depending on your configuration, these Azure AD fields might be coming directly from on-premises Active Directory (AD), which means that any changes made in AD will go through all the way to Dynamics 365 Online!

That also means that if you change a field in Dynamics 365 directly, that might get overwritten by the value in Azure AD in the next sync (usually every 15-30 minutes), so make sure you make that field read-only so users are not led to error.

Recommended fields to keep as read-only in Dynamics 365:

1. Username;
2. Title (Job Title);
3. Address

You can find more information on official Microsoft documentation: [Azure active directory attributes that are synced to Dynamics 365 / CDS](https://community.dynamics.com/forums/thread/details/?threadid=e8e7e257-a477-4a0c-9b5b-17e192e69a06).
