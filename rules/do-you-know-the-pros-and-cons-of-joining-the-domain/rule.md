---
type: rule
archivedreason: 
title: Do you know the pros and cons of joining the domain?
guid: 68db3fb1-c43a-456d-9288-ababd8832f67
uri: do-you-know-the-pros-and-cons-of-joining-the-domain
created: 2018-11-20T00:56:28.0000000Z
authors:
- title: Kaique Biancatti
  url: https://ssw.com.au/people/kaique-biancatti
related: []
redirects: []

---

Do you know if your computer should be joined to the domain or not?

<!--endintro-->

Joining your company's domain is a trade-off. If you join the domain, the company is the one responsible for managing your device, so all company rules and policies will be applied to it (Windows Update frequency, users, password resets, etc) and you will need to go through your SysAdmins if you have troubles with it.

If you choose to not join the domain, the machine management is all yours, giving you more freedom on the machine, but any automatic scripts would need to be done manually.

Below some pros and cons of joining the domain:


| |  **Pros (+)** 
 |  **Cons (-)** 
 |
| --- | --- | --- |
| Machine Management
 | Client management through GPOs (Group Policy Objects)
 | Lack of autonomy
 |
| Resource Access
 | Direct access to resources (e.g. fileserver)
 | Needs to sign in first, or be attached to a VPN or the network to access resources
 |
| Automatic Scripts
 | GPOs apply automatic scripts like the Login Script and Backup Scripts
 | Need to run Login and Backup scripts manually
 |
| Support Level 
 | More support from your SysAdmins, you have someone to rely on for any troubleshooting on all computer applications
 | Less support from SysAdmins, you can run any obscure application on your computer but that may not be supported by your company 
 |
| 
 | 
 | 
 |
