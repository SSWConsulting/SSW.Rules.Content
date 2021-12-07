---
type: rule
archivedreason: 
title: Do you have a rollback plan for TFS 2010 migration?
guid: f13a6fd0-9137-4981-a613-3408b36c0229
uri: rollback-plan-tfs2010-migration
created: 2009-11-02T22:38:45.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
related: []
redirects: 
- do-you-have-a-rollback-plan

---

Always [plan for a catastrophic disaster](/disaster-recovery-plan), in the event of errors when testing:

<!--endintro-->

1. Take the TFS2010 server offline
2. Bring the TFS2008 server online
3. Change the DNS entries for tfs.northwind.com from the IP for the TFS2010 server to the IP for the TFS2008 server
    1. Internal DNS Server
    2. External DNS Server

![Figure: DNS Pointer for TFS can be easily changed](TFSDNS.png)
