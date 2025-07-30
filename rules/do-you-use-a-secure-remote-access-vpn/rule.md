---
seoDescription: Secure your Remote Access VPN by using Multi-Factor Authentication (MFA) and a secure protocol such as SSL or IPSec.
type: rule
title: Do you use a secure VPN with MFA?
uri: do-you-use-a-secure-remote-access-vpn
authors:
  - title: Stanley Sidik
    url: https://ssw.com.au/people/stanley-sidik
  - title: Chris Schultz
    url: https://www.ssw.com.au/people/chris-schultz
related: []
redirects:
  - do-you-know-how-to-setup-a-pptp-vpn-in-windows-10
created: 2017-02-17T03:48:32.000Z
archivedreason: null
guid: 787d54f9-0c88-4a97-99ba-75e9239cd1e2
---

If you have a Remote Access VPN, it is important to ensure that the VPN is secure. VPNs are a common point of attack in cyber security incidents - if a bad actor can get into your VPN, they're in your network.

<!--endintro-->

These days, the most important way to secure your VPN is to use MFA. The best way to set this up will depend on the VPN and current MFA solution you are using.

It is also important to make sure that your VPN uses a secure protocol. Previously PPTP was a popular method, but this is now a deprecated service as it can be hacked very quickly using online tools. It is recommended to go with a provider that uses SSL or IPSec protocols.

:::bad

![Bad example: PPTP should not be used, it is old and no longer secure](vpn-pptp.png)

:::

:::good

![Good example: Cisco AnyConnect configured with Azure AD SSO and MFA](cisco-vpn.png)

:::

:::good

![Good example: Fortinet have their own MFA solution for VPN, FortiToken](fortitoken-vpn.png)

:::

### More information on Cisco AnyConnect

If you're using Cisco AnyConnect and Azure AD, it is easy to set up authentication through SAML - so your Azure AD MFA will be applied to any VPN logins.

The basic steps are:

1. In Azure AD, setup AnyConnect as an Enterprise application
2. In Azure AD, add the users that you want to have VPN access
3. Configure your Cisco ASA to use SAML for VPN authentication

![Figure: Adding Cisco AnyConnect as an Enterprise Application in Azure AD](ciscosaml.jpg)

For more information, see Cisco's documentation [here](https://www.cisco.com/c/en/us/support/docs/security/anyconnect-secure-mobility-client/215935-configure-asa-anyconnect-vpn-with-micros.html).
