---
type: rule
archivedreason: 
title: Do you know the right way to define a connection string?
guid: 61720f34-bf95-421e-90f6-238cfee9e7ad
uri: do-you-know-the-right-way-to-define-a-connection-string
created: 2018-04-26T22:05:50.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- know-the-right-way-to-define-a-connection-string

---

The bad practice below because the application can now do anything it wants to the SQL server (e.g. DROP other databases). 




```
Server=DRAGON;Database=SSWData2005;Uid=sa;Pwd=password;
```






::: bad
Bad example - The connection string use 'sa' in Uid 

:::


<!--endintro-->



```
If using SQL Authentication
Server=DRAGON;Database=SSWData2005;Uid=SSWWebsite;Pwd=password;Application Name=SSWWebsite 
If using Windows Authentication (Recommended)
Server=DRAGON;Database=SSWData2005;Integrated Security=True;Application Name=SSWWebsite
```




::: good
 Good example - The connection string with Application Name  
:::


* Application Name (e.g. SSWWebsite)

    * This makes profiling the database easier as you can filter by Application Name
* Application Specific Login/Windows Integrated security with a Domain Account for the application (e.g. SSWWebsite)
    * These logins should only have access to the databases they use (e.g. SSWData2005)
