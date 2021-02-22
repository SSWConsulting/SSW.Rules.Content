---
type: rule
archivedreason: 
title: ​DBAs - Do you measure Up-Time?
guid: 47f4213d-5f3e-42f9-9bad-0cd051ee6f48
uri: measure-up-time
created: 2019-11-18T18:22:58.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- dbas-do-you-measure-up-time

---

If you measure up-time you can pro-actively inform your manager how successful you have been as a DBA. You can do this in 2 ways:

### Option 1: High Tech Solution - using System Center Operations Manager (SCOM)

SCOM allows you to monitor and generate reports on the total uptime of your SQL Server and other service level exceptions. You need the following for these reports:

1. System Center Operations Manager and SQL Server on the network when performing a network scan
2. Microsoft System Center Management Pack for SQL Server


<!--endintro-->
Option 2: Low Tech Solution - using a recurring select as a heartbeat
1. Run a query as a ping once every 5 minutes something that takes about 2 seconds
2. SELECT \* FROM Orders Five times
3. Log it with the time
4. Graph - See uptime
5. Graph - See performance
