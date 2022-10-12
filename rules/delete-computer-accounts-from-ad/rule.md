---
type: rule
title: Do you delete computer accounts from Active Directory?
uri: delete-computer-accounts-from-ad
authors:
  - title: Chris Schultz
    url: https://ssw.com.au/people/chris-schultz
related:
  - disable-leaving-employee-accounts
created: 2022-06-02T22:58:49.208Z
guid: 3c078816-1abb-456e-96be-28fd9fba2006
---
Keeping your Active Directory environment tidy is helpful to keep things running smoothly, but it is also important to improve your security posture.

<!--endintro-->

Computer accounts in AD are similar to user accounts - they can be used to access other systems and data in your domain. Since computer accounts do not hold any useful information, it is safe to delete them when a computer is decommissioned. It is also very easy to re-join a computer to the domain if needed, so there is no reason to leave computers in a "disabled" state.

:::bad

![Bad example: Disabled computers in AD](disabled-pcs.png)

:::

:::good

![Good example: Only enabled, current computers](enabled-pcs.png)

:::