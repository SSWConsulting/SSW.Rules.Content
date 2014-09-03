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


<p class="p1">We've seen this happen too many times - a user wants to do something on a network<span style="line-height&#58;1.6;">&#160;</span><span style="line-height&#58;1.6;">server machine, and because the user hasn't got a profile setup on that machine, he end up using the Administrator password to log on as administrator.&#160;</span></p>
<br><excerpt class='endintro'></excerpt><br>
<p>​This is not a good thing because&#58;​</p><ol><li>We cannot tell who currently is logged in remotely, so if another developer wants to change something on the server, we can't work out who is on it.</li><li>This is particularly the case where a lot of the servers don't allow multiple concurrent
                        users, so we need to know who to disconnect or kick to free up a remote connection
                        license.</li><li>A lot of applications are installed as 'administrator', and no one end up remembering
                        what they installed, and thus the administrator profile is loaded with applications
                        that most people don't use.</li><li>If you check in/check out files from Source Safe, it may end up using the administrator
                        account - which means we can't work out who made a change in source safe.</li></ol><p>So log on using your own domain account.</p>


