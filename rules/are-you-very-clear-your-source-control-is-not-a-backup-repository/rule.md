---
type: rule
archivedreason: 
title: Are you very clear your Source Control is not a backup repository?
guid: 304b2ae7-ae68-4b3c-a8ec-00aef2fe7a1c
uri: are-you-very-clear-your-source-control-is-not-a-backup-repository
created: 2011-11-18T03:52:21.0000000Z
authors:
- id: 22
  title: David Klein
- id: 5
  title: Justin King
- id: 17
  title: Ryan Tee
- id: 6
  title: Tristan Kurniawan
related: []

---

Note: If you did not finish working:

* TFS put changes into shelveset
* SVN put changes into sandbox / branches

 Note: Another way to do this is to enable gated check-in and prevent check-ins that do not have build and tests passed.  
<!--endintro-->
