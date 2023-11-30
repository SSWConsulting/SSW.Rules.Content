---
type: rule
archivedreason: 
title: Login Security - Do you know the appropriate error message for an invalid username or password entry?
guid: 12631c53-8bcb-4a4b-99e3-0379a8639927
uri: login-security-do-you-know-the-correct-error-message-for-an-incorrect-user-name-or-password
created: 2015-02-16T03:17:47.0000000Z
authors: 
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

When a user fails to sign in due to an invalid email or password, you might have the well intention of letting them know by telling them exactly which one is invalid.

However, this is not secure. It makes it easier for bad guys (hackers) to get access to your account and do malicious things using your information.

A more secure and prudent approach involves delivering a message that simply states 'Invalid email or password.' This intentionally avoids disclosing which specific credential is incorrect, thereby enhancing security by limiting the information exposed to potential threats.

<!--endintro-->

::: good  
![Figure: Good example - For security reasons, leave it open if it was an invalid username or password](../../assets/GoodLoginError.png) 
:::
