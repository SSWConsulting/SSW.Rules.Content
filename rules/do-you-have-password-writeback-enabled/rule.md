---
type: rule
title: Security - Do you have Password Writeback enabled?
uri: do-you-have-password-writeback-enabled
authors:
  - title: Kaique Biancatti
    url: https://ssw.com.au/people/kaique-biancatti
related: []
redirects: []
created: 2018-11-13T04:10:57.000Z
archivedreason: null
guid: 7b11d493-7025-4f67-94a7-592ad109b1c3
---

Do you have Password Writeback enabled in your Azure AD Connect?

<!--endintro-->

If you want to let your users reset their own, on-premises passwords directly from the cloud, you need to have Password Writeback enabled in Azure AD Connect!

You can read more about Password Writeback from the Microsoft Documentation: https://docs.microsoft.com/en-us/azure/active-directory/authentication/howto-sspr-writeback

When setting up Azure AD Connect, you need to set the "Password Writeback" option:

![](enablepasswordwriteback.png)


::: good
Good Example: Setting up Password Writeback in Azure AD Connect  
:::
