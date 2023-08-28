---
type: rule
archivedreason: 
title: Do you monitor failed login attempts?
guid: 77c5c5ae-a0e6-4efe-8c90-c3818dbf1e4c
uri: monitor-failed-login-attempts
created: 2019-07-24T20:54:14.0000000Z
authors:
- title: Steven Andrews
  url: /people/steven-andrews
related: []
redirects:
- do-you-monitor-failed-login-attempts

---

It is important to monitor failed login attempts to determine if you are being attacked from an external source or are having failed attempts from users within your organization. This can be achieved with **Passive Whats Up Gold Monitor**.

<!--endintro-->

![Figure: This Passive Monitor can then be applied to your Servers](failed-login-whatsup-gold-1.png)  

::: good  
![Figure: Good example - This Passive Monitor will then record failed login attempts](failed-login-whatsup-gold-2.png)  
:::

It is important to also ensure that you have "Audit logon events" Group Policy applied to servers for source information on the login. 

See: [Do you use Group Policy to enable auditing of logon attempts?](/use-group-policy-to-enable-auditing-of-logon-attempts)
