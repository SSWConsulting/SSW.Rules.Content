---
type: rule
title: Do you choose the best way to send emails for your application?
uri: do-you-choose-the-best-way-to-send-emails-for-application
authors:
  - title: Kiki Biancatti
    url: https://www.ssw.com.au/people/kiki
created: 2021-09-30T05:57:13.369Z
guid: 90c93099-f38d-4725-aeac-ab769e7dec6f
---
Sending email from your application is easy, most programming languages allow you to send an email. Formatting and getting proper feedback and data on your emails is a bit more complicated.            

<!--endintro-->

Enterprise software generally need to send emails for a range of reasons e.g. inviting users, multifactor authentication, registering users, marketing campaigns, so it is important to know the best ways to send an email.

**1. Built-In Email commands**

Generally, programming languages have a built-in way to send email e.g. PowerShell with Send-MailMessage and System.Net.Mail in .Net, and those commands generally use an SMTP server (external or internal).
If you need a quick and dirty email, this is a good way.

**2. Microsoft Graph API - Microsoft Recommended**

Microsoft's recommended way of sending mail is through the Graph API. This is much more secure than just using any built-in commands and the command itself to send it is not much more complicated.
You can check [how to send email through the Graph API](https://docs.microsoft.com/en-us/graph/api/user-sendmail?view=graph-rest-1.0&tabs=http)

**3. Sendgrid - Recommended if you need a lot of features**

Another way to send email is to use a third-party solution e.g. Sendgrid that gives you many more features over the normal email-sending mechanisms above e.g:

* Integrated API
* Click tracking
* Spam management
