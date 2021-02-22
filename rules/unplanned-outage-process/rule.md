---
type: rule
archivedreason: 
title: Do you have an unplanned outage process?
guid: d96278bc-f927-4079-ba6c-c0b3c9a49b0d
uri: unplanned-outage-process
created: 2021-01-07T13:16:27.0000000Z
authors:
- title: Steven Andrews
  url: https://ssw.com.au/people/steven-andrews
related: []
redirects:
- do-you-have-an-unplanned-outage-process

---

For planned outages see: [https://rules.ssw.com.au/have-a-server-reboot-restart-policy](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=e3a456b4-3513-4dbe-a958-0176c1dfa85d)

During your course of being a SysAdmin, you will come across many outages. Some of them will impact BAU (Business as usual) and others will just be minor service outages. Do you know what to do you have a plan in the event of these outages?

Below is a process for these types of outages. Some amount of common sense is required here, an outage would be if services that would affect BAU work are disrupted for SSW and/or some hardware has failed.

<!--endintro-->

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

At SSW we use WhatsUp Gold for our device monitoring, however, there are many tools for this, Solarwinds, SCOM, etc

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


::: greybox
To: ALL
Subject: Outage Notice
 
 **Hey All,** 
 
We are experiencing an outage and the following services have been affected:
·       Xxx
·       Yyy
·       Zzz
 
We are working on restoring these services and will keep you updated.
 
Thank you,
SysAdmins  
:::
 

A separate email needs to be sent to SysAdmins outlining what was discussed on the call. If no one was contactable, please proceed with what you have determined on your own.


::: greybox
To: SysAdmins
Subject: SysAdmins – Outage Notice
 
 **Hey team,** 

As per our conversation.
 
The following services are disrupted:
·       Xxx
·       Yyy
·       Zzz
 
The impact of these services disrupted are:
·       Xxx
·       Yyy
·       Zzz
We have decided that an email to ALL is/is not required.
 
 **To myself,** 
 
The next steps to resolving this are:
 
1.      Xxx
2.      Yyy
3.      Zzz
 
Thank you,
SysAdmin  
:::
 

### Next Steps did \*not\* resolve the issue

If you have completed your tasks but the issue has not resolved, please try to make contact with the SysAdmin team again and send an updated To Myself email.

### Next Steps resolved the issue


If your actions have resolved the issue, please notify ALL of the services being restored and update your To Myself email.
