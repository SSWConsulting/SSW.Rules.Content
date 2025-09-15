---
seoDescription: Use the Common Data Service connector instead of Dynamics 365 when creating Flows to ensure compatibility and scalability.
type: rule
archivedreason:
title: Do you use the Common Data Service connector instead of the Dynamics 365 connector when using flows?
guid: 57167b92-8ff7-4aac-bfa0-d0de627e17d2
uri: use-the-common-data-service-connector-instead-of-the-dynamics-365-connector
created: 2020-06-25T22:21:36.0000000Z
authors:
  - title: Mehmet Ozdemir
    url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects:
  - do-you-use-the-common-data-service-connector-instead-of-the-dynamics-365-connector-when-using-flows
---

When creating a Flow that connects to CRM, Flow gives you the choice of:

- Dynamics 365
- Common Data Service
- Common Data Service (Current Environment)

<!--endintro-->

While it may seem like the obvious choice to pick Dynamics 365, but this would be a bad choice. The Dynamics 365 is deprecated as of April 2019. Use the Common Data Service (Current Environment) connector, it supports more data types and broader trigger scenarios.

Common Data Services (Current Environment) is only available if the Flow being developed is inside a solution. The advantage of using "Current Environment" is when the Flow is deployed across environments (Dev, Test, Prod) the connection is sticky to the environment to which it is being deployed. If a Flow is being developed outside of a solution, then use Common Data Services.

::: bad  
![Bad Example: Using the deprecated Dynamics 365 connector](bad-connector-use.png)  
:::

::: good  
![Good Example: Using the Common Data Service connector](good-connector-use.png)  
:::
