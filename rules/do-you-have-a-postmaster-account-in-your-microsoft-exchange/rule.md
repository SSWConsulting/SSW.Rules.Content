---
type: rule
archivedreason: 
title: Do you have a postmaster account in your Microsoft Exchange?
guid: 9e146833-e2da-4b07-9692-f3c6971f61fd
uri: do-you-have-a-postmaster-account-in-your-microsoft-exchange
created: 2015-04-10T18:59:46.0000000Z
authors:
- title: Stanley Sidik
  url: https://ssw.com.au/people/stanley-sidik
related: []
redirects: []

---

### What is a postmaster account? 

It is an RFC mandated specification email address use to identify the administrator of a mail server. Any errors in email processing are directed to the postmaster address.

The email received at this address is sent to the mail server administrator, in our case the SysAdmins.

<!--endintro-->

At SSW we have configured     postmaster@ssw.com.au as a distribution group, with mail server administrators as members of this distribution group.

![Figure: Group members of postmaster@ssw.com.au](postmaster.png)
