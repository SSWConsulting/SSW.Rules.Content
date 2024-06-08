---
type: rule
title: Do you integrate SCIM for Identity Management?
uri: use-scim-for-identity-management
authors:
  - title: Warwick Leahy
    url: https://ssw.com.au/people/warwick-leahy/
created: 2023-12-08T06:07:07.533Z
guid: 214b9c9f-5a9e-4b47-9389-b02bdeb660c6
---
Leveraging SCIM (System for Cross-domain Identity Management) in conjunction with Entra ID (or whatever Identity provider you use) is crucial for efficient and secure identity synchronization across cloud-based applications and services.

<!--endintro-->

## Why Integrate SCIM with Azure AD?

Integrating SCIM with Azure Active Directory automates the process of managing user identities in cloud applications. This integration streamlines user creation, modification, and deletion, reducing manual errors, saving administrative time, and enhancing security.

### Bad Example

Relying solely on manual identity management processes in Azure Active Directory without SCIM integration. This manual approach is inefficient, prone to errors, and can lead to security risks due to inconsistent identity data across applications.

::: bad

![Bad Example - SysAdmins have to provision each user separately in 3rd party products](bad-example-no-scim.jpg)

:::

### Good Example

Implementing SCIM to automate user provisioning and deprovisioning across various cloud services. This ensures consistent identity data, improves security, and reduces the administrative burden.

::: good

![Good Example: SysAdmins only provision into EntraId the SCIM provisioning does all the work](good-example-scim.jpg)

:::
By integrating SCIM with Azure Active Directory, organizations can achieve a more streamlined, secure, and efficient approach to identity management across their cloud ecosystem.
