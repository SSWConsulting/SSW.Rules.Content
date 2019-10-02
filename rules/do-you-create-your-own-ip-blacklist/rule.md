

---
authors:
  - id: 71
    title: Steven Andrews
  - id: 73
    title: Kaique Biancatti
---




<span class='intro'> Cisco's FirePower module is able to automatically get a list of suspicious IPs from Cisco, however the IPs that are attempting to break into your network may not be the same as Cisco's recommended Blacklist. That is why it is important to have your own IP Blacklist.<br><br> </span>

<p>​This needs to be an internally accessible webpage that the FirePower module can access and use as it's Blacklist. An example script for this can be found on&#160;<a href="https&#58;//github.com/SSWConsulting/BlacklistChecker">GitHub</a>.&#160;​<br><br></p><p>This script gathers IP Addresses from failed login attempts and compares them against multiple IP reputation sites. If it looks suspicious on 3 or more site this will be added into a text document that is then accessible by the Cisco FirePower module.​<br></p>


