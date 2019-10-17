---
type: rule
archivedreason: 
title: Do you have Active Directory Federation Services activated?
guid: 4fac6784-280a-41df-abb9-d7592a67fbcf
uri: do-you-have-active-directory-federation-services-activated
created: 2019-10-16T18:18:30.0000000Z
authors:
- id: 73
  title: Kaique Biancatti
related: []

---


Using Active Directory Federation Services (ADFS) lets you use one account to log into multiple systems, through Single Sign-On (SSO).<br>
<br><excerpt class='endintro'></excerpt><br>
<p>​ADFS is built upon SAML 2.0 protocol (Security Assertion Markup Language), allowing secure exchange of authentication data.</p><p>With ADFS, you can use only one account (generally created on your on-premises Active Directory (AD) server) to log into multiple systems e.g. Dynamics 365 CRM, Office 365 and many others.</p><p>This implementantion gives you security over which users are acessing which application with which accounts, and also reduces the surface for attacks on having many accounts with many different passwords&#58;</p><p><img src="/PublishingImages/sso.png" alt="sso.png" style="margin&#58;5px;" />&#160;</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example - Using one account on many systems</dd><dt><br></dt><dt>ADFS also gives you a solution in other corner cases&#58;</dt><dd><br></dd><dd>&#160; 1. When you want to use Office 365 and not store your password on the cloud;</dd><dt>&#160; 2. When you want the authentication to take place on-premises;</dt><dd>&#160; 3. When you want to create a trust between SharePoint on-premises and Azure AD;</dd><dt>&#160; 4. Amongst many others.</dt><dd><br></dd><dd><img src="/PublishingImages/adfs.jpg" alt="adfs.jpg" style="margin&#58;5px;width&#58;808px;" /></dd><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example - Using SSO to log into CRM with your on-premises account<br></dd>


