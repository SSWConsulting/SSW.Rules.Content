---
type: rule
archivedreason: 
title: Do you create your own IP Blacklist?
guid: a367534a-7fa0-424a-b842-8ac3e0dafb93
uri: do-you-create-your-own-ip-blacklist
created: 2019-10-01T21:59:55.0000000Z
authors:
- title: Steven Andrews
  url: https://ssw.com.au/people/steven-andrews
- title: Kaique Biancatti
  url: https://ssw.com.au/people/kaique-biancatti
related: []
redirects: []

---

Cisco's FirePower module is able to automatically get a list of suspicious IPs from Cisco, however the IPs that are attempting to break into your network may not be the same as Cisco's recommended Blacklist. That is why it is important to have your own IP Blacklist.


<!--endintro-->

This needs to be an internally accessible webpage that the FirePower module can access and use as it's Blacklist. An example script for this can be found on [GitHub](https&#58;//github.com/SSWConsulting/BlacklistChecker).

This script gathers IP Addresses from well-known internet lists, sanitizes them of internal IP addresses and adds them into a text document that is then accessible by the Cisco FirePower module.
Alternatively, you could also get failed login attempts and compare them against multiple IP reputation sites. If it looks suspicious on 3 or more sites, add it to the text document above.
