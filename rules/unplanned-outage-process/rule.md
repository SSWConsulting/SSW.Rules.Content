---
type: rule
title: Outage - Do you have an unplanned outage process?
uri: unplanned-outage-process
authors:
  - title: Steven Andrews
    url: https://ssw.com.au/people/steven-andrews
  - title: Kiki Biancatti
    url: https://ssw.com.au/people/kaique-biancatti
related: []
redirects:
  - do-you-have-an-unplanned-outage-process
created: 2021-01-07T13:16:27.000Z
archivedreason: null
guid: d96278bc-f927-4079-ba6c-c0b3c9a49b0d
---
For planned outages, see https://www.ssw.com.au/rules/planned-outage-process

During your course of being a SysAdmin, you will come across many outages. Some of them will impact BAU (Business as usual) and others will just be minor service outages. Do you know what to do you have a plan in the event of these outages?

<!--endintro-->

Below is a process for these types of outages. Some amount of common sense is required here, an outage would be if services that would affect BAU work are disrupted for SSW and/or some hardware has failed.

Hardware Outage:

* Firewall
* Switch
* Blade Servers
* SAN Storage
* UPS

Service Outage:

* Active Directory Domain Services
* O365 Services; Teams, SharePoint, Exchange, OneDrive
* File Servers
* SQL Servers
* IIS Servers

### Determining What Services are Disrupted

Many services can be used for device monitoring e.g. WhatsUp Gold, Solarwinds, SCOM. You would do the following in any of them:

1. Login to monitoring service
2. Check to see what services are down

### First Contact

After you have determined what services have been disrupted it is time to call your SysAdmin team and organise a quick conference call. This will allow you to have a discussion prior to making any changes/fixes that could cause the outage to become worse.

**Key Discussion Points:** 

1. What services have been disrupted?
2. What is the impact of these services?
3. Is an email to everyone in your company required?
4. What are your next steps?

**What if you cannot reach anyone?**

If you cannot reach anyone move onto the Email section.

### Email

If from the previous discussion you have determined that an email needs to be sent to your entire company, or you have decided this is necessary if you cannot contact anyone above, send an email in the following format:

::: email-template
|          |     |
| -------- | --- |
| To:      | SSWAll |
| Subject: | SysAdmins – Outage Notice |
::: email-content  

### Hi All,

We are experiencing an outage and the following services have been affected:

* XXX
* YYY
* ZZZ

We are working on restoring these services and will keep you updated.

Thank you,
SysAdmins     

:::
:::  

A separate email needs to be sent to SysAdmins outlining what was discussed on the call. If no one was contactable, please proceed with what you have determined on your own.

::: email-template
|          |     |
| -------- | --- |
| To:      | SysAdmins |
| Subject: | SysAdmins – Outage Notice |
::: email-content  

### Hi Team,

As per our conversation,

The following services are disrupted:

* XXX
* YYY
* ZZZ

The impact of these services disrupted are:

* XXX
* YYY
* ZZZ
  We have decided that an email to ALL is/is not required.

   **To myself,** 

The next steps to resolving this are:

1. XXX
2. YYY
3. ZZZ

Thank you,
SysAdmin     

:::

:::  

### Next steps did NOT resolve the issue

If you have completed your tasks but the issue has not resolved, please try to make contact with the SysAdmin team again and send an updated To Myself email.

### Next steps resolved the issue

If your actions have resolved the issue, please notify ALL of the services being restored and update your To Myself email.
