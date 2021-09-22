---
type: rule
title: Servers - Do you monitor the uptimes of all your servers daily?
uri: monitor-the-uptimes-of-all-your-servers-daily
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Kiki Biancatti
    url: https://ssw.com.au/people/kaique-biancatti
related: []
redirects:
  - do-you-monitor-the-uptimes-of-all-your-servers-daily
created: 2017-07-10T23:10:04.000Z
archivedreason: null
guid: b031777e-12e8-4a0d-8930-d3920ab5cfcd
---
It is important that the system administrator can easily find out how reliable his servers are. This can be achieved using tools like What's Up Gold https://www.whatsupgold.com to monitor many statistics e.g.:

* Uptime - Ping, Interface monitor
* Performance - RAM usage, CPU usage
* Network - Bandwidth, Interface throughput
* Storage - Disk usage, health

It is also possible to create SQL Reporting Services to create a nicely formatted and branded report showing the above stats.

For example, here is a report that SSW uses to monitor their servers on a daily basis:

<!--endintro-->

::: good\
![Figure: Good example - Green indicates servers are healthy](WuGReport.png)
:::