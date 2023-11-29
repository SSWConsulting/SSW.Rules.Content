---
type: rule
title: Do you have a User Risk Policy?
uri: user-risk-policy
authors:
  - title: Kaique Biancatti
    url: https://ssw.com.au/people/kiki
related:
  - sign-in-risk-policy
created: 2022-04-29T02:13:58.669Z
guid: 0aef7548-1e06-4723-9f51-a6da5f564813

---

Azure Active Directory (AD) Identity Protection's user risk policy helps automatically protect your users from risky behaviour on their accounts.

<!--endintro-->

Azure AD has many built-in solutions to protect legitimate users from malicious actors trying to sign in to their accounts via Azure AD, one of them being user risk policy.

This policy can either fully block access or require a password reset for the user to be able to login, depending on the the sign-in risk level (High, Medium and above or Low and above).

The level is determined automatically by a series of factors, including:

1. Atypical travel e.g. If a user has logged in from Australia and then authenticates from Europe in the next 5 minutes, an impossible travel to physically make
2. Unfamiliar sign-in properties e.g. If a user has logged in from a location that he never logged on from before
3. And other, constantly updated factors

When setting this up, you can also choose to apply this to all your users, selected individuals or groups, and exclude users.

![Good example - All users with a risk of High will be blocked from signing in](userrisk.jpg)

You can read more on how to enable these policies on [configure and enable risk policies documentation](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/howto-identity-protection-configure-risk-policies).
