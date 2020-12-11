---
type: rule
archivedreason: 
title: Do you monitor failed login attempts?
guid: 77c5c5ae-a0e6-4efe-8c90-c3818dbf1e4c
uri: do-you-monitor-failed-login-attempts
created: 2019-07-24T20:54:14.0000000Z
authors:
- id: 71
  title: Steven Andrews
related: []

---

It is important to monitor failed login attempts to determine if you are being attacked from an external source or are having failed attempts from users within your organisation. This can be achieved with Passive Whats Up Gold Monitor.

<!--endintro-->
<dl class="image">&lt;dt&gt;<img src="failed-login-whatsup-gold-1.png" alt="failed-login-whatsup-gold-1.png">&lt;/dt&gt;<dd>Figure: This Passive Monitor can then be applied to your Servers</dd></dl><dl class="image">&lt;dt&gt;<img src="failed-login-whatsup-gold-2.png" alt="failed-login-whatsup-gold-2.png">&lt;/dt&gt;<dd>Figure: Good example - This Passive Monitor will then record failed login attempts</dd></dl>It is important to also ensure that you have "Audit logon events" Group Policy applied to servers for source information on the login. 
See:     [Do you use Group Policy to enable auditing of logon attempts?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=aa9c011d-81de-4d79-82af-a80215ccb131)
