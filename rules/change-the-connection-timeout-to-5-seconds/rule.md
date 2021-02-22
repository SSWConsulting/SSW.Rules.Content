---
type: rule
archivedreason: 
title: Do you change the connection timeout to 5 seconds?
guid: fbd22c8b-8a67-4ed9-be9a-1a7572df866d
uri: change-the-connection-timeout-to-5-seconds
created: 2018-04-25T20:09:55.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects:
- do-you-change-the-connection-timeout-to-5-seconds

---

By default, the connection timeout is 15 seconds. When it comes to testing if a connection is valid or not, 15 seconds is a long time for the user to wait. You should change the connection timeout inside your connection strings to 5 seconds.


<!--endintro-->



```
"Integrated Security=SSPI;Initial Catalog=SallyKnoxMedical;Data 
Source=TUNA"
```




::: bad
Figure: Bad Connection String

:::



```
"Integrated Security=SSPI;Initial Catalog=SallyKnoxMedical;Data Source=TUNA;
Connect Timeout=5"
```




::: good
Figure: Good Connection String with a 5-second connection timeout

:::
