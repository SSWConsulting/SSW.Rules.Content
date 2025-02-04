---
seoDescription: Discover how Active Directory Federation Services (ADFS) enables Single Sign-On (SSO) for secure access to multiple systems like Office 365 and Dynamics 365.
type: rule
archivedreason: 
title: Do you have Active Directory Federation Services activated?
guid: 4fac6784-280a-41df-abb9-d7592a67fbcf
uri: have-active-directory-federation-services-activated
created: 2019-10-16T18:18:30.0000000Z
authors:
- title: Kaique Biancatti
  url: https://ssw.com.au/people/kaique-biancatti
related: []
redirects:
- do-you-have-active-directory-federation-services-activated

---

Using Active Directory Federation Services (ADFS) lets you use one account to log into multiple systems, through Single Sign-On (SSO).

<!--endintro-->

ADFS is built upon SAML 2.0 protocol (Security Assertion Markup Language), allowing secure exchange of authentication data.

With ADFS, you can use only one account (generally created on your on-premises Active Directory (AD) server) to log into multiple systems e.g. Dynamics 365 CRM, Office 365 and many others.

This implementation gives you security over which users are acessing which application with which accounts, and also reduces the surface for attacks on having many accounts with many different passwords:

![](sso.png)

::: good
Figure: Good Example - Using one account on many systems  
:::

ADFS also gives you a solution in other corner cases:

  1. When you want to use Office 365 and not store your password on the cloud;  2. When you want the authentication to take place on-premises;  3. When you want to create a trust between SharePoint on-premises and Entra ID;  4. Amongst many others.
![](adfs.jpg)

::: good
Figure: Good Example - Using SSO to log into CRM with your on-premises account

:::
