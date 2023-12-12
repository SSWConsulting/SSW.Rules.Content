---
type: rule
archivedreason: Deprecated
title: Do you turn off auto update on your servers?
guid: 31e1abd1-5623-4f55-a31e-0ff068ae0084
uri: do-you-turn-off-auto-update-on-your-sharepoint-servers
created: 2010-06-24T01:43:02.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-turn-off-auto-update-on-your-servers

---

It is not a good idea to have Windows Update automatically updating your servers.  There are a few reasons.  

<!--endintro-->

1. The hotfix could bring down a production environment. (This issue previously happened)
2. In fact, even in a development environment this could be hours of lost work as the development team struggles to understand why only  **some** of the developers' servers  **magically and mysteriously** broke overnight.
3. Windows Update could restart your server, or put your server in a state where it requires restarting - preventing any urgent MSI installs without bringing down the server.

Windows Update remains the best thing for end-users to protect their systems.  But in a server, especially a production server environment - Windows Update patches are just like any new versions of the software that's built internally.  It should be tested and then deployed in a controlled manner.

So recommendations:

1. Windows Updates may be critical and should be kept relatively up to date.
2. Have a plan where your awesome Network Admins schedule time to keep the servers up to date - including testing that the servers still perform its functions.
3. Turn off Automatic Windows Update on Windows Servers
