---
type: rule
archivedreason: 
title: Do you know the right notification for backups?
guid: df70361d-0a85-43cd-bd24-f6b08455330f
uri: do-you-know-the-right-notification-for-backups
created: 2017-07-10T23:20:11.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- know-the-right-notification-for-backups

---

You need to log a record on success so you can check for backups that have failed. 

<!--endintro-->


::: bad  
![Figure: Bad example - an email is sent on completion](backup\_notification\_bad.jpg)  
:::


::: good  
![Figure: Good example - a record is logged on completion](backup\_notification\_good.jpg)  
:::

Now you are able to be aware of missing backups. You can make automatically notification based on above table e.g. [by SQL Reporting Services data-driven subscription](https://www.ssw.com.au/ssw/KB/KB.aspx?KBID=Q1455840)
