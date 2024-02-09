---
type: rule
archivedreason: 
title: Bounces - Do you know what to do with bounced email?
guid: e21a0c88-e1a5-4b66-acc6-0dfb7fffbf12
uri: bounces-do-you-know-what-to-do-with-bounced-email
created: 2011-08-25T19:54:59.0000000Z
authors: 
  - title: Christian Morford-Waite
    url: https://ssw.com.au/people/christian-morford-waite
related: []
redirects: []

---

Having people report bounce back emails is frustrating and time consuming. The first thing to try when you get a report is to check that your mail server isn’t on a spam blacklist. An easy way to check this is via [MX Toolbox](http://mxtoolbox.com/).

<!--endintro-->

![Figure: Enter the domain to check](MXToolbox-1.jpg)

![Figure: Then select "Blacklist Check"](MXToolbox-2.jpg)

![Figure: Getting a zero is good, so you know that you are not blacklisted... so Step 1 is good](MXToolbox-3.jpg)

Next step check that you have primary and secondary (and even better tertiary) MX records setup and working.

![Figure: Seeing at least 2 MX records is good... Run an SMTP Test to test mail servers. So Step 2 is good](MXToolbox-4.jpg)

If success on both steps the error is most likely on the senders side. Send them the an email to check their mail settings.

::: greybox

Dear xxx,

As per this rule on bounced emails [https://www.ssw.com.au/rules/bounces-do-you-know-what-to-do-with-bounced-email](/bounces-do-you-know-what-to-do-with-bounced-email)

* I have checked Step 1 – it is good
* I have checked Step 2 – it is good

The problem is likely your end

:::
**Figure: What to send the person**
