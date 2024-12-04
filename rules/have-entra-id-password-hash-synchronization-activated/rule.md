---
seoDescription: Synchronize Microsoft Entra ID passwords with your on-premises AD to enable seamless login and access cloud services.
type: rule
archivedreason:
title: Do you have Entra ID Password Hash Synchronization activated?
guid: 30b0179b-4a85-4aed-9f56-ada07a8ca067
uri: have-entra-id-password-hash-synchronization-activated
created: 2020-11-13T00:12:28.0000000Z
authors:
  - title: Kaique Biancatti
    url: https://ssw.com.au/people/kaique-biancatti
related: []
redirects:
  - have-azure-active-directory-password-hash-synchronization-activated
  - do-you-have-azure-active-directory-password-hash-synchronization-activated
---

Microsoft Entra ID - formerly Azure Active Directory, Password Hash Synchronization (PHS) is one of the methods you can use if you want to have your identities synced to the cloud, alongside Pass-through Authentication (PTA) and Federation with AD FS.
If you have a hybrid identity in place with Entra ID, chances are you are already synchronizing password hashes to the cloud with Microsoft Entra Connect formerly Azure AD Connect.

<!--endintro-->

Entra ID PHS synchronizes the password in on-premises Active Directory with Entra ID so you can use your on-premises password to login to cloud services, like Azure or Office 365. It also allows you to implement Seamless Sign-On for domain-joined machines, so users don't need to login twice when opening their emails in a browser, for example.

Entra ID PHS also allows you to have an absolute lean infrastructure on-premises, as the only needed moving part is Entra Connect to be installed in a server or Domain Controller. No agents or internet-facing machines necessary.

The web requests don't even come to your server, they are server by Microsoft's big pool of servers around the globe!

::: good  
![Figure: Good Example – Entra ID PHS infrastructure workflow](entra-id-phs.png)  
:::

You can check out a deep dive of Entra ID PHS in official Microsoft documentation at [What is password hash synchronization with Microsoft Entra ID?](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-phs)
