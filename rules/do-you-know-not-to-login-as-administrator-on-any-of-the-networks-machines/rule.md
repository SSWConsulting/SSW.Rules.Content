---
type: rule
archivedreason: 
title: Do you know not to login as Administrator on any of the networks machines?
guid: 08228540-250a-4ccb-a22d-b0b434949fdb
uri: do-you-know-not-to-login-as-administrator-on-any-of-the-networks-machines
created: 2014-09-03T18:22:13.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

We've seen this happen too many times - a user wants to do something on a network server machine, and because the user hasn't got a profile setup on that machine, he end up using the Administrator password to log on as administrator.

<!--endintro-->

This is not a good thing because:

1. We cannot tell who currently is logged in remotely, so if another developer wants to change something on the server, we can't work out who is on it.
2. This is particularly the case where a lot of the servers don't allow multiple concurrent<br>                        users, so we need to know who to disconnect or kick to free up a remote connection<br>                        license.
3. A lot of applications are installed as 'administrator', and no one end up remembering<br>                        what they installed, and thus the administrator profile is loaded with applications<br>                        that most people don't use.
4. If you check in/check out files from Source Safe, it may end up using the administrator<br>                        account - which means we can't work out who made a change in source safe.


So log on using your own domain account.
