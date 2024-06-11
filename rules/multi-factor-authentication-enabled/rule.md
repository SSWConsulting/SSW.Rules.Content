---
seoDescription: Ensure you have robust multi-factor authentication (MFA) enabled to protect your users and administrator accounts from unauthorized access.
type: rule
title: Security - Do you have MFA (Multi-Factor Authentication) enabled?
uri: multi-factor-authentication-enabled
authors:
  - title: Kaique Biancatti
    url: https://ssw.com.au/people/kaique-biancatti
  - title: Chris Schultz
    url: https://www.ssw.com.au/people/chris-schultz
  - title: Andrew Harris
    url: https://www.ssw.com.au/people/andrew-harris
related: []
redirects:
  - do-you-have-mfa-(multi-factor-authentication)-enabled
  - do-you-have-mfa-multi-factor-authentication-enabled
created: 2018-09-06T07:16:45.000Z
archivedreason: null
guid: fccb11d9-2ada-4f76-9b73-1f2b9be1e159
---

You should protect your users and administrator accounts with **more than one** authentication method.

<!--endintro-->

### What is Multi-Factor Authentication (MFA)?

MFA is another layer of security for your users and administrators, it adds another code or approval that you can receive in a device that you possess - a phone, for example - to make it more difficult for attackers to steal your account. If they guess or brute-force your password, they still need the second code or approval to make it to your account.

Generally, every time you log in on a service, it will ask for your normal password and an additional code or approval. This can be retrieved through:

- RECOMMENDED - An authenticator app with passwordless **(secure)**
- An authenticator app with password **(secure)**
- A hardware token/key **(secure)**
- Email, SMS, or phone call **(less secure)**

### MFA in Microsoft 365

If you have Microsoft 365 Premium, Azure P1 or higher licensing you should use Conditional Access to set up MFA - read more about conditional access here: [Do you use Conditional Access policies?](/conditional-access-policies)

Once MFA is set up, you can see which method your users are using - go to **Azure AD | Security | Authentication Methods | User registration details**.

- Under **Default authentication method**, you want to see **Microsoft Authenticator app**
- Under **Methods Registered**, you also want to see **Microsoft Passwordless phone sign-in**

::: bad
![Figure: Bad example - No Microsoft Passwordless phone sign-in registered](azure-mfa-bad.png)
:::

::: good
![Figure: Good example - Microsoft Passwordless phone sign-in registered](azure-mfa-good.png)
:::

### Recovering your Authenticator App

Your Authenticator App becomes a critical part of your day and being without it can seriously hamper your ability to work. The following steps can ensure that if for whatever reason you lose your setup, your can get back up and running as quickly as possible.

1. **Ensure you are backing up your Authenticator App** - For the Microsoft Authenticator app, you can find more details about [setting up backup and all the gotchas to be aware of](https://support.microsoft.com/en-au/account-billing/back-up-and-recover-account-credentials-in-the-authenticator-app-bb939936-7a8d-4e88-bc43-49bc1a700a40)

::: img-medium good
![Figure: Turning on Authenticator app backup on iCloud (or equivalent on Android)](backup-authenticator.jpg)
:::

2. **Ensure you have a Sign-in method other than your Authenticator App** - Backups have a lot of gotchas so this is probably the most important thing you can do. Note that if you use email, it's important that you do **not** use the email associated with the sign-in. Better yet, investigate a security key like the [YubiKey](https://www.yubico.com/au/product/yubikey-5-series/yubikey-5-nfc/)

::: good
![Figure: Good example - Email as a backup to Microsoft Authenticator App](securityinfo-email.png)
:::
