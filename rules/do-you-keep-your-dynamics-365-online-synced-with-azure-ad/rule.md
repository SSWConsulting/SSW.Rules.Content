---
type: rule
archivedreason: 
title: Do you keep your Dynamics 365 Online synced with Azure AD?
guid: acd3409e-f1df-4c8c-8326-0549dc7ba205
uri: do-you-keep-your-dynamics-365-online-synced-with-azure-ad
created: 2020-09-16T18:50:43.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 73
  title: Kaique Biancatti
related: []

---


<p class="ssw15-rteElement-P">If you are using Microsoft Dynamics 365 Online as your CRM solution, you might have noticed that it syncs some Azure Active Directory (Azure AD) fields automatically.<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>​Dynamics 365 Online leverages Azure AD fields to import information to users, e.g.&#58;<br></p><ol><li>First Name;</li><li>Last Name;</li><li>Job Title;</li><li>Address</li></ol><p>And, depending on your configuration, these Azure AD fields might be coming directly from on-premises Active Directory (AD), which means that any changes made in AD will go through all the way to Dynamics 365 Online!</p><p>That also means that if you change a field in Dynamics 365 directly, that might get overwritten by the value in Azure AD in the next sync (usually every 15-30 minutes), so make sure you make that field read-only so users are not led to error.</p><p>Recommended fields to keep as read-only in Dynamics 365&#58;</p><ol><li>User Name;</li><li>Title (Job Title);</li><li>Address</li></ol><p>You can find more information on official Microsoft documentation&#58; 
   <a href="https&#58;//community.dynamics.com/crm/f/microsoft-dynamics-crm-forum/386022/info-azure-active-directory-attributes-that-are-synced-to-dynamics-365-cds">Azure active directory attributes that are synced to Dynamics 365 / CDS</a>​.<br></p>


