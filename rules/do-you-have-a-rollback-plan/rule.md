---
type: rule
archivedreason: 
title: Do you have a rollback plan?
guid: f13a6fd0-9137-4981-a613-3408b36c0229
uri: do-you-have-a-rollback-plan
created: 2009-11-02T22:38:45.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
related: []
redirects: []

---

Always [plan for a catastrophic disaster](http://www.ssw.com.au/SSW/Standards/Rules/RulesToBetterNetworks.aspx#assumeCatastrophic), in the event of errors when testing:

1. Take the TFS2010 server offline
2. Bring the TFS2008 server online
3. Change the DNS entries for tfs.northwind.com from the IP for the TFS2010 server to the IP for the TFS2008 server
    1. Internal DNS Server
    2. External DNS Server


![TFS In DNS](TFSDNS.png)
 Figure: DNS Pointer for TFS can be easily changed

<!--endintro-->
