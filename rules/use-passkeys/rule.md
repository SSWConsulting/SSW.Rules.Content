---
type: rule
archivedreason:
title: Authentication - Do you use Passkeys for stronger security?
seoDescription: Learn why Passkeys provide stronger security than passwords and MFA, offering phishing-resistant authentication with biometric verification and eliminating password reuse vulnerabilities.
guid: 76838a73-4219-4127-8033-f5f4edbf8091
uri: use-passkeys
created: 2024-09-17T00:00:00.000Z
authors:
  - title: Gordon Beeming
    url: https://www.ssw.com.au/people/gordon-beeming
  - title: Luke Cook
    url: https://ssw.com.au/people/luke-cook
  - title: Baba Kamyljanov
    url: https://ssw.com.au/people/baba-kamyljanov
related:
  - using-mfa
  - password-manager
  - multi-factor-authentication-enabled
  - choosing-authentication
  - modern-stateless-authentication
---

Passwords are a traditional technology that create security vulnerabilities through reuse, breaches, and phishing attacks. Passwords remain a weak point in your security chain.

Passkeys represent the next evolution in authentication, providing phishing-resistant, seamless integration with biometric technology, and passwordless security that's both more secure and more convenient than traditional methods.

<!--endintro-->

`youtube: https://www.youtube.com/embed/bdp8RdjV6PU`
**Video: What are passkeys? Explained in under 4 minutes (4 min)**

## Why Passkeys are superior to passwords

### Security benefits

1. **Phishing-resistant** - Unlike passwords and SMS codes, passkeys cannot currently be stolen through phishing attacks because they use cryptographic keys tied to specific domains
2. **No password reuse** - Each passkey is unique to a service
3. **Breach-proof** - Services only store your public key, so even if breached, attackers get nothing useful
4. **No interceptable codes** - Unlike SMS-based MFA, passkeys can't be intercepted or redirected

### User experience benefits

1. **Faster sign-in** - Authenticate with just your biometric (fingerprint, face, or PIN) - no typing passwords or waiting for SMS codes
2. **Synced across devices** - Passkeys created with major providers like Google, Apple, or Microsoft automatically sync across your devices using their secure cloud services (e.g.: Google Password Manager, iCloud Keychain). This means a passkey you create on your phone will be available on your tablet and laptop, as long as you're signed into the same account.
3. **No forgotten passwords** - Never forget a password again or get locked out of accounts

::: bad img-medium
![Figure: Bad example - Traditional password vulnerable to phishing, are often used across many accounts, and you may forget it over time](sign-in-with-password.png)
:::

::: good img-medium
![Figure: Good example - Passkey authentication is phishing-resistant and convenient (in this example using Windows PIN)](sign-in-with-passkey.png)
:::

## Wider adoption and social pressure

While passkeys have been around for many years, it's taken longer than we'd like for companies and services to adopt them. And even when they **are** adopted, passkeys are often treated as second-class citizens, and sites still default users to less secure authentication methods.

Some cybersecurity professionals are taking it upon themselves to drive an increase in the adoption rate of passkeys, by way of social pressure and public education on the topic.

One of the most prolific cybersecurity professionals - [Troy Hunt](https://www.troyhunt.com) - creator of [haveibeenpwned.com](https://haveibeenpwned.com/), publishes a "list of shame" of businesses and services that don't yet support passkeys as a form of authentication. This is the same tactic Troy used many years ago to pressure businesses to implement secure transport layer encryption (HTTPS) on their sites, to great effect. Go Troy!  

## How to set up passkeys for Microsoft Entra Account

### Prerequisites

* Set up the Microsoft Authenticator app with your account
  If you haven't yet, follow these steps:
   1. Go to [https://mysignins.microsoft.com/security-info](https://mysignins.microsoft.com/security-info)
   2. Select **+ Add sign-in method**
   3. Choose **Microsoft Authenticator** from the dropdown and select Add
   4. Open Authenticator on your phone, click the **+** and select **Work or school account**
   5. Then tap **Scan a QR Code**
* Use a device that supports biometric authentication (fingerprint, face recognition, or PIN)

### Steps to create a passkey

1. **Navigate to your Microsoft security settings**

   * Go to [https://mysignins.microsoft.com/security-info](https://mysignins.microsoft.com/security-info)
   * Sign in with your Microsoft account credentials

2. **Add a new sign-in method**

   * Click **+ Add sign-in method**

3. **Choose your passkey type**

   * Select **Passkey in Microsoft Authenticator**. This will create a passkey stored securely on your phone, which you can use to sign in on this or other devices.

4. **Set up through Microsoft Authenticator**

   * In Authenticator app select your Microsoft account
   * Then select **Create a passkey** and follow the instructions

   ::: img-medium
   ![Figure: Passkey created successfully](passkey-create-success.png)
   :::

5. **Test your passkey**

   * Sign out of your Microsoft account
   * When signing back in, select **Other ways to sign in**
   * Choose **Face, fingerprint, PIN, or security key** option
   * Use your biometric authentication to complete sign-in

::: info
**Pro tip:** Set up passkeys on multiple devices (phone, laptop, tablet) to ensure you always have access to your accounts even if one device is unavailable.
:::

::: info
**Note:** These steps are for a work or school Microsoft account (Microsoft Entra ID). For a personal Microsoft account, please visit your [security dashboard](https://account.microsoft.com/security).
:::

### Managing passkeys

* **View all passkeys** - Go to [https://mysignins.microsoft.com/security-info](https://mysignins.microsoft.com/security-info) to see all registered passkeys
  * **Removing passkeys** - Delete unused passkeys for old or lost devices

## The future is passwordless

Many companies, including SSW, are moving toward a passwordless future. By starting with passkeys today, you’re making logins safer and easier while getting ready for a time when passwords are no longer needed.

### References

* [FIDO Alliance - Passkeys](https://fidoalliance.org/passkeys/)
* [Microsoft Docs - Passwordless authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passwordless)
* [Microsoft Support - Signing in with a passkey](https://support.microsoft.com/en-us/account-billing/signing-in-with-a-passkey-09a49a86-ca47-406c-8acc-ed0e3c852c6d)
* [Learn more about Microsoft Authenticator app](https://support.microsoft.com/en-us/account-billing/about-microsoft-authenticator-9783c865-0308-42fb-a519-8cf666fe0acc)
* [Learn about WebAuthn](https://webauthn.io/)
* [FIDO2 .NET library for server side implementation of Passkeys](https://github.com/passwordless-lib/fido2-net-lib)
