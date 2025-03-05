---
seoDescription: Reduce spam and protect your organization's resources by using anti-spam protection and Microsoft Defender.
type: rule
title: Do you know how to reduce spam?
uri: do-you-know-how-to-reduce-spam
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Cameron Shaw
    url: https://ssw.com.au/people/cameron-shaw
  - title: Warwick Leahy
    url: https://ssw.com.au/people/warwick-leahy
  - title: Kaique Biancatti
    url: https://www.ssw.com.au/people/kaique-biancatti
related: []
redirects: []
created: 2009-04-07T07:49:39.000Z
archivedreason: null
guid: 5aa5ea9a-284b-4aae-96cb-e3d1a551c275
---

Spam. It wastes time and resources. In most cases, the amount of spam received by an organization far exceeds the amount of legitimate email.

E.g. Average volume of spam received daily:

| Total Email Received | Spam  | Phishing | Malware | Legitimate | Spam % |
| -------------------- | ----- | -------- | ------- | ---------- | ------ |
| 14539                | 12579 | 40       | 14      | 1906       | 86     |

<!--endintro-->

From a SysAdmin point of view, using anti-spam protection is the best way to go to protect your company against spam, and, if you are using Exchange or Exchange Online, one of the best options for you is to use Microsoft's answer to this: [Microsoft 365 Defender](https://security.microsoft.com)

There are also other non-Microsoft options e.g.

* Mimecast
* GFI MailEssentials
* N-able Mail Assure

When using Exchange and the Outlook client (or Outlook.com), Microsoft has an addon "Report Message" which helps users to report spam and phishing emails (This can be deployed by an Admin to everyone in your company):

* [Mark email as junk or phishing](https://support.microsoft.com/en-us/office/use-the-report-message-add-in-b5caa9f1-cdf3-4443-af8c-ff724ea719d2)

When on the Outlook desktop client, you should actively mark items as Junk and block their senders. Do the following:

1. Select the email | Click "Report Message" | Choose "Phishing" or "Junk"

::: good
![Figure: Good example - Report a message as "Junk"](2023-05-23_8-57-28.png)
:::

Doing this sends a copy of the email for analysis to Microsoft Defender and helps to train the model that detects Junk mail and Phishing Scams.

From time to time you may also receive an email telling you about quarantined emails.

::: good
![Figure: Good example - Quarantine Email - 'Review Message', 'Release' or 'Block Sender'](quarantine-email3.png)
:::

::: info
**Important - check very carefully and make sure you know the sender before releasing an email. Otherwise you may end up releasing an email that you shouldn't. If in doubt call your friendly SysAdmin who will help you to determine if it's safe to release.**
:::

::: good
![Figure: Good example - Release or delete quarantined emails](quarantine-email2.png)
:::

If your email is hosted by a **third-party provider other than Outlook, Office 365, or Gmail**, take the following precautions:

1. **Immediately change your password** – If you suspect your email account has been targeted, update your credentials to prevent unauthorized access.
2. **Enable two-factor authentication (2FA)** – This adds an extra layer of security to your email account.
3. **Consider migrating to a trusted provider** – Outlook, Office 365, and Gmail offer robust phishing and spam protection. If your current provider lacks strong security measures, switching to one of these services can reduce future phishing risks.
4. **Monitor your account for unusual activity** – Check your sent folder and recent login activity to ensure no unauthorized access has occurred.

**Warning:** If you receive a phishing attempt through a third-party email provider with poor filtering, your email account is at greater risk of being compromised. Migrating your email to a secure provider like Outlook or Gmail improves security and reduces phishing attempts.

By taking proactive measures, you can significantly reduce the chances of falling victim to phishing and spam emails.
