---
type: rule
title: Security - Do you have MFA (Multi Factor Authentication) enabled?
uri: do-you-have-mfa-multi-factor-authentication-enabled
authors:
  - title: Kaique Biancatti
    url: https://ssw.com.au/people/kaique-biancatti
  - title: Chris Schultz
    img: https://www.ssw.com.au/people/chris-schultz
related: []
redirects:
  - do-you-have-mfa-(multi-factor-authentication)-enabled
created: 2018-09-06T07:16:45.000Z
archivedreason: null
guid: fccb11d9-2ada-4f76-9b73-1f2b9be1e159
---
Do you protect your users and administrator accounts with more than one authentication method?

<!--endintro-->

### What is Multi-Factor Authentication (MFA)?

MFA is another layer of security for your users and administrators, it adds another code or approval that you can receive in a device that you possess - a phone, for example - to make it more difficult for attackers to steal your account. If they guess or brute-force your password, they still need the second code or approval to make it to your account. 

Generally, every time you log in on a service, it will ask for your normal password and an additional code or approval. This can be retrieved through:

* An authenticator app with passwordless **(secure), RECOMMENDED**
* An authenticator app with password **(secure)**
* A﻿ hardware token/key **(secure)**
* Email, SMS, or phone call **(less secure)**

### M﻿FA in Microsoft 365

I﻿f you have Microsoft 365 Premium, Azure P1 or higher licensing you should use Conditional Access to set up MFA - read more about conditional access here: [Do you use Conditional Access policies?](https://www.ssw.com.au/rules/conditional-access-policies)

O﻿nce MFA is set up, you can see which method your users are using - go to **Azure AD | Security | Authentication Methods | User registration details**.

* U﻿nder **Default authentication method**, you want to see **Microsoft Authenticator app**
* U﻿nder **Methods Registered**, you also want to see **Microsoft Passwordless phone sign-in**

::: bad  
![Bad example: no Microsoft Passwordless phone sign-in registered](azure-mfa-bad.png)
:::

::: good  
![Good example: Microsoft Passwordless phone sign-in registered](azure-mfa-good.png)
:::