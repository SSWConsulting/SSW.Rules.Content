---
type: rule
archivedreason: 
title: Do you know the right notification for backups?
guid: df70361d-0a85-43cd-bd24-f6b08455330f
uri: do-you-know-the-right-notification-for-backups
created: 2017-07-10T23:20:11.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

You need to log a record on success so you can check for backups that have failed. 

<!--endintro-->
<dl class="badImage">&lt;dt&gt;<img src="backup_notification_bad.jpg" alt="backup_notification_bad.jpg">&lt;/dt&gt;<dd>Figure: Bad example - an email is sent on completion</dd></dl><dl class="goodImage">&lt;dt&gt;<img src="backup_notification_good.jpg" alt="backup_notification_good.jpg">&lt;/dt&gt;<dd>Figure: Good example - a record is logged on completion</dd></dl>
Now you are able to be aware of missing backups. You can make automatically notification based on above table e.g. [by SQL Reporting Services data-driven subscription](https://www.ssw.com.au/ssw/KB/KB.aspx?KBID=Q1455840)
