---
seoDescription: Configure email settings for Dynamics CRM by enabling Serverside Sync, replacing the deprecated Email router.
type: rule
archivedreason:
title: Do you know how to configure email sending?
guid: 32d3646d-20fb-467b-be8d-a9b5c3e30020
uri: how-to-configure-email-sending
created: 2017-11-06T22:51:47.0000000Z
authors:
  - title: Liam Elliott
    url: https://ssw.com.au/people/liam-elliott
related: []
redirects:
  - do-you-know-how-to-configure-email-sending
---

When configuring your email settings for Dynamics CRM, make sure you configure Serverside Sync.

<!--endintro-->

As per CRM Tip of the Day <https://crmtipoftheday.com/979/start-planning-farewell-party-for-email-router/>, the CRM Email router is to be deprecated. You should use the Serverside Sync now instead.

::: bad  
![Figure: Bad example - Deprecated Mail routed Enabled](CRM Email Router.png)  
:::

::: good  
![Figure: Good example - Serverside Sync configured as per Connect Dynamics 365 to POP3/SMTP servers](CRM ServerSideSync.png)  
:::

Learn more on [Connect Dynamics 365 to POP3/SMTP servers](https://learn.microsoft.com/en-us/previous-versions/dynamicscrm-2016/administering-dynamics-365/mt622063(v=crm.8)?redirectedfrom=MSDN).

